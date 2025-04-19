import json

from agno.tools import tool
from nornir_napalm.plugins.tasks import napalm_get

from src.nornir_network_inventory import nr
from src.result_processor import process_network_results


@tool(
    name="collect_network_data_ntp_servers",
    description="Recopila información de servidores NTP de los dispositivos de red",
    cache_results=True,
    cache_dir="/tmp/netai_cache",
    cache_ttl=3600
)
def collect_network_data_ntp_servers():
    """
    Recopila información de servidores NTP utilizando nornir y napalm, procesa los resultados
    y devuelve un string JSON con los datos formateados.

    El getter 'ntp_servers' recopila información sobre los servidores NTP configurados, incluyendo:
    - Direcciones IP de servidores NTP
    - Preferencia de servidor
    - Configuración de autenticación (si aplica)
    - Versión de NTP configurada

    Returns:
        str: Información de servidores NTP en formato JSON
    """
    results = nr.run(
        task=napalm_get, getters=["ntp_servers"]
    )

    # Procesar los resultados usando la función de src/result_processor.py
    final_results = process_network_results(results)

    # Convertir el diccionario a string JSON con formato
    return json.dumps(final_results, indent=4)
