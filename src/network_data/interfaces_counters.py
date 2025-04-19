import json

from agno.tools import tool
from nornir_napalm.plugins.tasks import napalm_get

from src.nornir_network_inventory import nr
from src.result_processor import process_network_results


@tool(
    name="collect_network_data_interfaces_counters",
    description="Recopila contadores de interfaces de los dispositivos de red",
    cache_results=True,
    cache_dir="/tmp/netai_cache",
    cache_ttl=3600
)
def collect_network_data_interfaces_counters():
    """
    Recopila contadores de interfaces utilizando nornir y napalm, procesa los resultados
    y devuelve un string JSON con los datos formateados.

    El getter 'interfaces_counters' recopila estadísticas de tráfico de las interfaces, incluyendo:
    - Paquetes recibidos y enviados
    - Bytes recibidos y enviados
    - Errores de entrada y salida
    - Descartes de entrada y salida
    - Multicast recibidos
    - Broadcast enviados

    Returns:
        str: Contadores de interfaces en formato JSON
    """
    results = nr.run(
        task=napalm_get, getters=["interfaces_counters"]
    )

    # Procesar los resultados usando la función de src/result_processor.py
    final_results = process_network_results(results)

    # Convertir el diccionario a string JSON con formato
    return json.dumps(final_results, indent=4)
