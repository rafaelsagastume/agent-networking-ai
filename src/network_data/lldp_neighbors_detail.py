import json

from agno.tools import tool
from nornir_napalm.plugins.tasks import napalm_get

from src.nornir_network_inventory import nr
from src.result_processor import process_network_results


@tool(
    name="collect_network_data_lldp_neighbors_detail",
    description="Recopila información detallada de vecinos LLDP de los dispositivos de red",
    cache_results=True,
    cache_dir="/tmp/netai_cache",
    cache_ttl=3600
)
def collect_network_data_lldp_neighbors_detail():
    """
    Recopila información detallada de vecinos LLDP utilizando nornir y napalm, procesa los resultados
    y devuelve un string JSON con los datos formateados.

    El getter 'lldp_neighbors_detail' recopila información extendida sobre los vecinos LLDP, incluyendo:
    - Nombres de host e IDs de los sistemas vecinos
    - Descripción del sistema
    - Capacidades del sistema
    - Información detallada de puerto
    - Versión del sistema operativo
    - Dirección de gestión
    - Tiempo de vida de la información

    Returns:
        str: Información detallada de vecinos LLDP en formato JSON
    """
    results = nr.run(
        task=napalm_get, getters=["lldp_neighbors_detail"]
    )

    # Procesar los resultados usando la función de src/result_processor.py
    final_results = process_network_results(results)

    # Convertir el diccionario a string JSON con formato
    return json.dumps(final_results, indent=4)
