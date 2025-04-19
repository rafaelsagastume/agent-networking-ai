import json

from agno.tools import tool
from nornir_napalm.plugins.tasks import napalm_get

from src.nornir_network_inventory import nr
from src.result_processor import process_network_results


@tool(
    name="collect_network_data_ntp_peers",
    description="Recopila información de pares NTP de los dispositivos de red",
    cache_results=True,
    cache_dir="/tmp/netai_cache",
    cache_ttl=3600
)
def collect_network_data_ntp_peers():
    """
    Recopila información de pares NTP utilizando nornir y napalm, procesa los resultados
    y devuelve un string JSON con los datos formateados.

    El getter 'ntp_peers' recopila información sobre los pares NTP configurados, incluyendo:
    - Direcciones IP de pares NTP
    - Relaciones entre pares (peer, server, etc.)

    Returns:
        str: Información de pares NTP en formato JSON
    """
    results = nr.run(
        task=napalm_get, getters=["ntp_peers"]
    )

    # Procesar los resultados usando la función de src/result_processor.py
    final_results = process_network_results(results)

    # Convertir el diccionario a string JSON con formato
    return json.dumps(final_results, indent=4)
