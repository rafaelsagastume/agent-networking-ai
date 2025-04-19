import json

from agno.tools import tool
from nornir_napalm.plugins.tasks import napalm_get

from src.nornir_network_inventory import nr
from src.result_processor import process_network_results


@tool(
    name="collect_network_data_bgp_config",
    description="Recopila la configuración BGP de los dispositivos de red",
    cache_results=True,
    cache_dir="/tmp/netai_cache",
    cache_ttl=3600
)
def collect_network_data_bgp_config():
    """
    Recopila datos de configuración BGP utilizando nornir y napalm, procesa los resultados
    y devuelve un string JSON con los datos formateados.

    El getter 'bgp_config' recopila información detallada sobre la configuración BGP, incluyendo:
    - Configuración global de BGP
    - Grupos de pares BGP
    - Configuración de vecinos BGP individuales
    - Políticas de enrutamiento aplicadas
    - Configuraciones de filtrado
    - Configuraciones de comunidad BGP

    Returns:
        str: Datos de configuración BGP en formato JSON
    """
    results = nr.run(
        task=napalm_get, getters=["bgp_config"]
    )

    # Procesar los resultados usando la función de src/result_processor.py
    final_results = process_network_results(results)

    # Convertir el diccionario a string JSON con formato
    return json.dumps(final_results, indent=4)
