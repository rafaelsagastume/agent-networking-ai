import json

from agno.tools import tool
from nornir_napalm.plugins.tasks import napalm_get

from src.nornir_network_inventory import nr
from src.result_processor import process_network_results


@tool(
    name="collect_network_data_network_instances",
    description="Recopila instancias de red virtuales de los dispositivos de red",
    cache_results=True,
    cache_dir="/tmp/netai_cache",
    cache_ttl=3600
)
def collect_network_data_network_instances():
    """
    Recopila instancias de red virtuales utilizando nornir y napalm, procesa los resultados
    y devuelve un string JSON con los datos formateados.

    El getter 'network_instances' recopila información sobre instancias de red virtuales, incluyendo:
    - VRFs configuradas
    - Instancias de enrutamiento
    - Tables de enrutamiento asociadas
    - Interfaces asociadas a cada instancia
    - Configuración de protocolos de enrutamiento por instancia

    Returns:
        str: Información de instancias de red virtuales en formato JSON
    """
    results = nr.run(
        task=napalm_get, getters=["network_instances"]
    )

    # Procesar los resultados usando la función de src/result_processor.py
    final_results = process_network_results(results)

    # Convertir el diccionario a string JSON con formato
    return json.dumps(final_results, indent=4)
