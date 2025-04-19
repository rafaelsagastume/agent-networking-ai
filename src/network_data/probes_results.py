import json

from agno.tools import tool
from nornir_napalm.plugins.tasks import napalm_get

from src.nornir_network_inventory import nr
from src.result_processor import process_network_results


@tool(
    name="collect_network_data_probes_results",
    description="Recopila resultados de las sondas de monitoreo de los dispositivos de red",
    cache_results=True,
    cache_dir="/tmp/netai_cache",
    cache_ttl=3600
)
def collect_network_data_probes_results():
    """
    Recopila resultados de sondas de monitoreo utilizando nornir y napalm, procesa los resultados
    y devuelve un string JSON con los datos formateados.

    El getter 'probes_results' recopila información sobre los resultados de las sondas de monitoreo, incluyendo:
    - Resultados actuales de sondas IP SLA
    - Métricas de rendimiento
    - Latencia
    - Pérdida de paquetes
    - Jitter
    - Estado operativo (activo/inactivo)
    - Tiempo desde la última prueba

    Returns:
        str: Resultados de las sondas de monitoreo en formato JSON
    """
    results = nr.run(
        task=napalm_get, getters=["probes_results"]
    )

    # Procesar los resultados usando la función de src/result_processor.py
    final_results = process_network_results(results)

    # Convertir el diccionario a string JSON con formato
    return json.dumps(final_results, indent=4)
