import json

from agno.tools import tool
from nornir_napalm.plugins.tasks import napalm_get

from src.nornir_network_inventory import nr
from src.result_processor import process_network_results


@tool(
    name="collect_network_data_probes_config",
    description="Recopila configuración de sondas de monitoreo de los dispositivos de red",
    cache_results=True,
    cache_dir="/tmp/netai_cache",
    cache_ttl=3600
)
def collect_network_data_probes_config():
    """
    Recopila configuración de sondas de monitoreo utilizando nornir y napalm, procesa los resultados
    y devuelve un string JSON con los datos formateados.

    El getter 'probes_config' recopila información sobre la configuración de sondas de monitoreo, incluyendo:
    - Sondas IP SLA configuradas
    - Parámetros de sondeo
    - Objetivos de monitorización
    - Intervalos de sondeo
    - Umbrales configurados
    - Operaciones de monitoreo programadas

    Returns:
        str: Configuración de sondas de monitoreo en formato JSON
    """
    results = nr.run(
        task=napalm_get, getters=["probes_config"]
    )

    # Procesar los resultados usando la función de src/result_processor.py
    final_results = process_network_results(results)

    # Convertir el diccionario a string JSON con formato
    return json.dumps(final_results, indent=4)
