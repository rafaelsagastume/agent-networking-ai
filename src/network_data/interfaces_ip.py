import json

from agno.tools import tool
from nornir_napalm.plugins.tasks import napalm_get

from src.nornir_network_inventory import nr
from src.result_processor import process_network_results


@tool(
    name="collect_network_data_interfaces_ip",
    description="Recopila información IP de las interfaces de los dispositivos de red",
    cache_results=True,
    cache_dir="/tmp/netai_cache",
    cache_ttl=3600
)
def collect_network_data_interfaces_ip():
    """
    Recopila información de IPs de interfaces utilizando nornir y napalm, procesa los resultados
    y devuelve un string JSON con los datos formateados.

    El getter 'interfaces_ip' recopila información detallada sobre las direcciones IP, incluyendo:
    - Direcciones IPv4 y IPv6 configuradas
    - Máscaras de subred
    - Prefijos
    - Direcciones secundarias
    - Información de VLAN asociada (cuando aplica)

    Returns:
        str: Información IP de interfaces en formato JSON
    """
    results = nr.run(
        task=napalm_get, getters=["interfaces_ip"]
    )

    # Procesar los resultados usando la función de src/result_processor.py
    final_results = process_network_results(results)

    # Convertir el diccionario a string JSON con formato
    return json.dumps(final_results, indent=4)
