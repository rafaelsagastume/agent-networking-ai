import json

from agno.tools import tool
from nornir_napalm.plugins.tasks import napalm_get

from src.nornir_network_inventory import nr
from src.result_processor import process_network_results


@tool(
    name="collect_network_data_mac_address_table",
    description="Recopila la tabla de direcciones MAC de los dispositivos de red",
    cache_results=True,
    cache_dir="/tmp/netai_cache",
    cache_ttl=3600
)
def collect_network_data_mac_address_table():
    """
    Recopila la tabla de direcciones MAC utilizando nornir y napalm, procesa los resultados
    y devuelve un string JSON con los datos formateados.

    El getter 'mac_address_table' recopila información sobre las direcciones MAC aprendidas, incluyendo:
    - Direcciones MAC
    - Interfaces asociadas
    - VLANs asociadas
    - Si es estática o dinámica
    - Tiempo de actividad de la entrada

    Returns:
        str: Tabla de direcciones MAC en formato JSON
    """
    results = nr.run(
        task=napalm_get, getters=["mac_address_table"]
    )

    # Procesar los resultados usando la función de src/result_processor.py
    final_results = process_network_results(results)

    # Convertir el diccionario a string JSON con formato
    return json.dumps(final_results, indent=4)
