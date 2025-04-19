import json

from agno.tools import tool
from nornir_napalm.plugins.tasks import napalm_get

from src.nornir_network_inventory import nr
from src.result_processor import process_network_results


@tool(
    name="collect_network_data_bgp_neighbors_detail",
    description="Recopila información detallada de los vecinos BGP de los dispositivos de red",
    cache_results=True,
    cache_dir="/tmp/netai_cache",
    cache_ttl=3600
)
def collect_network_data_bgp_neighbors_detail():
    """
    Recopila datos detallados de los vecinos BGP utilizando nornir y napalm, procesa los resultados
    y devuelve un string JSON con los datos formateados.

    El getter 'bgp_neighbors_detail' recopila información extendida sobre los vecinos BGP, incluyendo:
    - Información detallada de cada sesión BGP
    - Mensajes de estado y notificaciones
    - Estadísticas de recepción y envío de mensajes
    - Temporizadores de sesión
    - Información detallada sobre prefijos anunciados y recibidos
    - Capacidades BGP negociadas
    - Parámetros de configuración detallados

    Returns:
        str: Datos detallados de vecinos BGP en formato JSON
    """
    results = nr.run(
        task=napalm_get, getters=["bgp_neighbors_detail"]
    )

    # Procesar los resultados usando la función de src/result_processor.py
    final_results = process_network_results(results)

    # Convertir el diccionario a string JSON con formato
    return json.dumps(final_results, indent=4)
