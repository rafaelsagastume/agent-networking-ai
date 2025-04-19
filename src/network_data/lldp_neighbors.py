import json

from agno.tools import tool
from nornir_napalm.plugins.tasks import napalm_get

from src.nornir_network_inventory import nr
from src.result_processor import process_network_results


@tool(
    name="collect_network_data_lldp_neighbors",
    description="Recopila información básica de vecinos LLDP de los dispositivos de red",
    cache_results=True,
    cache_dir="/tmp/netai_cache",
    cache_ttl=3600
)
def collect_network_data_lldp_neighbors():
    """
    Recopila información básica de vecinos LLDP utilizando nornir y napalm, procesa los resultados
    y devuelve un string JSON con los datos formateados.

    El getter 'lldp_neighbors' recopila información básica sobre los vecinos LLDP, incluyendo:
    - Nombres de host de dispositivos vecinos
    - Interfaces locales conectadas a vecinos
    - Interfaces remotas de los vecinos
    - Identificación de dispositivos adyacentes

    Returns:
        str: Información básica de vecinos LLDP en formato JSON
    """
    results = nr.run(
        task=napalm_get, getters=["lldp_neighbors"]
    )

    # Procesar los resultados usando la función de src/result_processor.py
    final_results = process_network_results(results)

    # Convertir el diccionario a string JSON con formato
    return json.dumps(final_results, indent=4)
