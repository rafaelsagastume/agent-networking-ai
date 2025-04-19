import json

from agno.tools import tool
from nornir_napalm.plugins.tasks import napalm_get

from src.nornir_network_inventory import nr
from src.result_processor import process_network_results


@tool(
    name="collect_network_data_users",
    description="Recopila información de usuarios configurados en los dispositivos de red",
    cache_results=True,
    cache_dir="/tmp/netai_cache",
    cache_ttl=3600
)
def collect_network_data_users():
    """
    Recopila información de usuarios utilizando nornir y napalm, procesa los resultados
    y devuelve un string JSON con los datos formateados.

    El getter 'users' recopila información detallada sobre los usuarios configurados, incluyendo:
    - Nombres de usuario
    - Nivel de privilegio
    - Configuración de contraseña (hash)
    - Roles asignados
    - Estado de la cuenta
    - Configuración SSH y claves públicas

    Returns:
        str: Información de usuarios configurados en formato JSON
    """
    results = nr.run(
        task=napalm_get, getters=["users"]
    )

    # Procesar los resultados usando la función de src/result_processor.py
    final_results = process_network_results(results)

    # Convertir el diccionario a string JSON con formato
    return json.dumps(final_results, indent=4)
