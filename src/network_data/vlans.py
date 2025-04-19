import json

from agno.tools import tool
from nornir_napalm.plugins.tasks import napalm_get

from src.nornir_network_inventory import nr
from src.result_processor import process_network_results


@tool(
    name="collect_network_data_vlans",
    description="Recopila información de VLANs configuradas en los dispositivos de red",
    cache_results=True,
    cache_dir="/tmp/netai_cache",
    cache_ttl=3600
)
def collect_network_data_vlans():
    """
    Recopila información de VLANs utilizando nornir y napalm, procesa los resultados
    y devuelve un string JSON con los datos formateados.

    El getter 'vlans' recopila información detallada sobre las VLANs configuradas, incluyendo:
    - IDs de VLAN
    - Nombres de VLAN
    - Estado operativo
    - Interfaces asignadas
    - Información de spanning-tree
    - Direcciones MAC asociadas
    - Configuración de trunking

    Returns:
        str: Información de VLANs en formato JSON
    """
    results = nr.run(
        task=napalm_get, getters=["vlans"]
    )

    # Procesar los resultados usando la función de src/result_processor.py
    final_results = process_network_results(results)

    # Convertir el diccionario a string JSON con formato
    return json.dumps(final_results, indent=4)
