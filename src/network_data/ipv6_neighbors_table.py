import json

from agno.tools import tool
from nornir_napalm.plugins.tasks import napalm_get

from src.nornir_network_inventory import nr
from src.result_processor import process_network_results


@tool(
    name="collect_network_data_ipv6_neighbors_table",
    description="Recopila la tabla de vecinos IPv6 de los dispositivos de red",
    cache_results=True,
    cache_dir="/tmp/netai_cache",
    cache_ttl=3600
)
def collect_network_data_ipv6_neighbors_table():
    """
    Recopila la tabla de vecinos IPv6 utilizando nornir y napalm, procesa los resultados
    y devuelve un string JSON con los datos formateados.

    El getter 'ipv6_neighbors_table' recopila información sobre los vecinos IPv6 (similar a la tabla ARP para IPv4), incluyendo:
    - Direcciones IPv6 de vecinos
    - Direcciones MAC correspondientes
    - Interfaces a través de las cuales se accede a los vecinos
    - Estado de los vecinos (alcanzable, obsoleto, etc.)
    - Tiempo de vida de la entrada

    Returns:
        str: Tabla de vecinos IPv6 en formato JSON
    """
    results = nr.run(
        task=napalm_get, getters=["ipv6_neighbors_table"]
    )

    # Procesar los resultados usando la función de src/result_processor.py
    final_results = process_network_results(results)

    # Convertir el diccionario a string JSON con formato
    return json.dumps(final_results, indent=4)
