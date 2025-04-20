import json

from agno.tools import tool
from nornir_napalm.plugins.tasks import napalm_get

from src.nornir_network_inventory import nr
from src.result_processor import process_network_results


@tool(
    name="collect_network_data_route_to",
    description="Recopila información de rutas específicas desde los dispositivos de red",
)
def collect_network_data_route_to(destination: str = "8.8.8.8"):
    """
    Recopila información de rutas específicas utilizando nornir y napalm, procesa los resultados
    y devuelve un string JSON con los datos formateados.

    El getter 'route_to' recopila información detallada sobre la ruta hacia un destino específico, incluyendo:
    - Próximo salto
    - Interfaces de salida
    - Protocolo de enrutamiento
    - Métricas de ruta
    - Preferencias de ruta
    - Rutas alternativas

    Args:
        destination: La dirección IP de destino para consultar la ruta (por defecto: 8.8.8.8)

    Returns:
        str: Información de rutas en formato JSON
    """
    results = nr.run(
        task=napalm_get, getters=["route_to"], destination=destination
    )

    # Procesar los resultados usando la función de src/result_processor.py
    final_results = process_network_results(results)

    # Convertir el diccionario a string JSON con formato
    return json.dumps(final_results, indent=4)
