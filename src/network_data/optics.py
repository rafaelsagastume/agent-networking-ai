import json

from agno.tools import tool
from nornir_napalm.plugins.tasks import napalm_get

from src.nornir_network_inventory import nr
from src.result_processor import process_network_results


@tool(
    name="collect_network_data_optics",
    description="Recopila información de módulos ópticos de los dispositivos de red",
    cache_results=True,
    cache_dir="/tmp/netai_cache",
    cache_ttl=3600
)
def collect_network_data_optics():
    """
    Recopila información de módulos ópticos utilizando nornir y napalm, procesa los resultados
    y devuelve un string JSON con los datos formateados.

    El getter 'optics' recopila información sobre los módulos ópticos, incluyendo:
    - Niveles de potencia de transmisión y recepción
    - Umbrales de alarma
    - Estado de alarmas
    - Tipo de módulo
    - Información del fabricante
    - Número de serie
    - Temperatura del módulo

    Returns:
        str: Información de módulos ópticos en formato JSON
    """
    results = nr.run(
        task=napalm_get, getters=["optics"]
    )

    # Procesar los resultados usando la función de src/result_processor.py
    final_results = process_network_results(results)

    # Convertir el diccionario a string JSON con formato
    return json.dumps(final_results, indent=4)
