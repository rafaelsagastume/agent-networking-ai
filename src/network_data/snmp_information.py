import json

from agno.tools import tool
from nornir_napalm.plugins.tasks import napalm_get

from src.nornir_network_inventory import nr
from src.result_processor import process_network_results


@tool(
    name="collect_network_data_snmp_information",
    description="Recopila información SNMP de los dispositivos de red",
    cache_results=True,
    cache_dir="/tmp/netai_cache",
    cache_ttl=3600
)
def collect_network_data_snmp_information():
    """
    Recopila información SNMP utilizando nornir y napalm, procesa los resultados
    y devuelve un string JSON con los datos formateados.

    El getter 'snmp_information' recopila información detallada sobre la configuración SNMP, incluyendo:
    - Comunidades SNMP configuradas
    - Permisos de comunidad
    - Configuración de SNMP v3
    - Configuración de traps y notificaciones
    - Ubicación y contacto del sistema
    - Grupos y vistas de SNMP

    Returns:
        str: Información SNMP en formato JSON
    """
    results = nr.run(
        task=napalm_get, getters=["snmp_information"]
    )

    # Procesar los resultados usando la función de src/result_processor.py
    final_results = process_network_results(results)

    # Convertir el diccionario a string JSON con formato
    return json.dumps(final_results, indent=4)
