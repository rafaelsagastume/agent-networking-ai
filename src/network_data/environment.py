import json

from agno.tools import tool
from nornir_napalm.plugins.tasks import napalm_get

from src.nornir_network_inventory import nr
from src.result_processor import process_network_results


@tool(
    name="collect_network_data_environment",
    description="Recopila datos ambientales de los dispositivos de red",
)
def collect_network_data_environment():
    """
    Recopila datos ambientales utilizando nornir y napalm, procesa los resultados
    y devuelve un string JSON con los datos formateados.

    El getter 'environment' recopila información sobre el entorno físico del dispositivo, incluyendo:
    - Temperaturas de componentes
    - Estado de los ventiladores
    - Estado de la fuente de alimentación
    - Uso de CPU
    - Uso de memoria
    - Alertas ambientales

    Returns:
        str: Datos ambientales del dispositivo en formato JSON
    """
    results = nr.run(
        task=napalm_get, getters=["environment"]
    )

    # Procesar los resultados usando la función de src/result_processor.py
    final_results = process_network_results(results)

    # Convertir el diccionario a string JSON con formato
    return json.dumps(final_results, indent=4)
