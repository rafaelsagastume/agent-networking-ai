import json

from agno.tools import tool
from nornir_napalm.plugins.tasks import napalm_get

from src.nornir_network_inventory import nr
from src.result_processor import process_network_results


@tool(
    name="collect_network_data_firewall_policies",
    description="Recopila políticas de firewall de los dispositivos de red",
    cache_results=True,
    cache_dir="/tmp/netai_cache",
    cache_ttl=3600
)
def collect_network_data_firewall_policies():
    """
    Recopila políticas de firewall utilizando nornir y napalm, procesa los resultados
    y devuelve un string JSON con los datos formateados.

    El getter 'firewall_policies' recopila información sobre las políticas de firewall configuradas, incluyendo:
    - Reglas de firewall
    - Políticas de acceso
    - Filtrado de tráfico
    - Estadísticas de coincidencia
    - Acciones configuradas
    - Prioridades de reglas

    Returns:
        str: Políticas de firewall en formato JSON
    """
    results = nr.run(
        task=napalm_get, getters=["firewall_policies"]
    )

    # Procesar los resultados usando la función de src/result_processor.py
    final_results = process_network_results(results)

    # Convertir el diccionario a string JSON con formato
    return json.dumps(final_results, indent=4)
