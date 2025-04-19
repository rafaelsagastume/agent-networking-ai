import json

from agno.tools import tool
from nornir_napalm.plugins.tasks import napalm_get

from src.nornir_network_inventory import nr
from src.result_processor import process_network_results


@tool(
    name="collect_network_data_arp_table",
    description="Recopila datos de la tabla ARP de los dispositivos de red",
    cache_results=True,
    cache_dir="/tmp/netai_cache/arp_table",
    cache_ttl=3600
)
def collect_network_data_arp_table():
    """
    Recopila datos de la tabla ARP utilizando nornir y napalm, procesa los resultados
    y devuelve un string JSON con los datos formateados.

    El getter 'get_arp_table' recopila información detallada sobre las entradas ARP, incluyendo:
    - Direcciones IP: Direcciones IP de dispositivos en la red local
    - Direcciones MAC: Direcciones MAC asociadas con cada dirección IP
    - Interfaces: Interfaces de red a través de las cuales se accede a cada dispositivo
    - Edad: Tiempo transcurrido desde la última actualización de la entrada ARP (en algunos dispositivos)

    Returns:
        str: Datos de la tabla ARP en formato JSON
    """
    results = nr.run(
        task=napalm_get, getters=["get_arp_table"]
    )

    # Procesar los resultados usando la función de src/result_processor.py
    final_results = process_network_results(results)

    # Convertir el diccionario a string JSON con formato
    return json.dumps(final_results, indent=4)
