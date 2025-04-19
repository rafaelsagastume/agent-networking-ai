import json

from nornir_napalm.plugins.tasks import napalm_get

from src.nornir_network_inventory import nr
from src.result_processor import process_network_results


def collect_network_data_bgp_neighbors():
    """
    Recopila datos de sesiones (bgp_neighbors) utilizando nornir y napalm, procesa los resultados
    y devuelve un string JSON con los datos formateados.

    El getter 'bgp_neighbors' recopila información detallada sobre las sesiones BGP, incluyendo:
    - Vecinos BGP: Dispositivos conectados mediante BGP
    - ASN: Números de Sistema Autónomo
    - Estado de las sesiones: Establecidas, conectando, inactivas, etc.
    - Prefijos recibidos: Número de rutas recibidas de cada vecino
    - Prefijos enviados: Número de rutas anunciadas a cada vecino
    - Descripción: Información configurada sobre el vecino
    - Tiempo de actividad: Duración de la sesión BGP actual
    - Política de enrutamiento: Configuraciones de filtrado aplicadas

    Returns:
        str: Datos de sesiones BGP en formato JSON
    """
    results = nr.run(
        task=napalm_get, getters=["bgp_neighbors"]
    )

    # Procesar los resultados usando la función de src/result_processor.py
    final_results = process_network_results(results)

    # Convertir el diccionario a string JSON con formato
    return json.dumps(final_results, indent=4)
