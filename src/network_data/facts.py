import json

from nornir_napalm.plugins.tasks import napalm_get

from src.nornir_network_inventory import nr
from src.result_processor import process_network_results


def collect_network_data_facts():
    """
    Recopila datos de red utilizando nornir y napalm, procesa los resultados
    y devuelve un string JSON con los datos formateados.

    El getter 'facts' recopila información básica sobre los dispositivos, incluyendo:
    - Hostname: Nombre del dispositivo
    - FQDN: Nombre de dominio completo
    - Modelo: Modelo del hardware
    - Número de serie: Identificador único del dispositivo
    - OS Version: Versión del sistema operativo
    - Interfaces: Lista de interfaces del dispositivo
    - Uptime: Tiempo de funcionamiento desde el último reinicio
    - Vendor: Fabricante del dispositivo

    Returns:
        str: Datos de red en formato JSON
    """
    results = nr.run(
        task=napalm_get, getters=["facts"]
    )

    # Procesar los resultados usando la función de src/result_processor.py
    final_results = process_network_results(results)

    # Convertir el diccionario a string JSON con formato
    return json.dumps(final_results, indent=4)
