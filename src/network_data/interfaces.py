import json
import logging

from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result

from src.nornir_network_inventory import nr
from src.result_processor import process_network_results


def collect_network_data_interfaces():
    """
    Recopila datos de interfaces de red utilizando nornir y napalm, procesa los resultados
    y devuelve un string JSON con los datos formateados.

    El getter 'interfaces' recopila información detallada sobre las interfaces de red, incluyendo:
    - Nombre de la interfaz: Identificador de la interfaz
    - Estado administrativo: si la interfaz está habilitada o deshabilitada
    - Estado operativo: si la interfaz está activa o inactiva
    - Dirección MAC: Dirección física de la interfaz
    - Dirección IP/Máscara: Configuración IP de la interfaz
    - Velocidad: Velocidad de la interfaz en Mbps
    - MTU: Unidad máxima de transferencia
    - Descripción: Descripción configurada para la interfaz (nombre, datos extras, proposito)
    - Último cambio: Tiempo desde el último cambio de estado

    Returns:
        str: Datos de interfaces de red en formato JSON
    """
    results = nr.run(
        task=napalm_get, getters=["interfaces"]
    )

    # Procesar los resultados usando la función de src/result_processor.py
    final_results = process_network_results(results)

    # Convertir el diccionario a string JSON con formato
    return json.dumps(final_results, indent=4)
