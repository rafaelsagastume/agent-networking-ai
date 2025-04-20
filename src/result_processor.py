import json


def process_network_results(results):
    """
    Procesa los resultados de tareas de red de Nornir, extrayendo y 
    parseando cualquier cadena JSON encontrada en los datos.

    Args:
        results: Los resultados de la ejecución de tareas de Nornir

    Returns:
        Un diccionario con los resultados procesados para cada host
    """
    def parse_json_str(data):
        """Parse any JSON strings found in the data structure recursively"""
        if isinstance(data, dict):
            return {k: parse_json_str(v) for k, v in data.items()}
        elif isinstance(data, list):
            return [parse_json_str(item) for item in data]
        elif isinstance(data, str):
            try:
                return json.loads(data)
            except json.JSONDecodeError:
                return data
        else:
            return data

    # Create a dictionary to store results for each host
    final_results = {}

    try:
        for host, multi_result in results.items():
            host_data = {}
            if not multi_result:
                # Si no hay resultados para este host
                host_data["error"] = "No hay resultados disponibles"
                final_results[host] = host_data
                continue

            for result in multi_result:
                try:
                    if result.failed:
                        host_data[result.name] = f"Failed: {result.exception}"
                    else:
                        # Transform any JSON strings in the result
                        host_data[result.name] = parse_json_str(result.result)
                except Exception as e:
                    # Capturar cualquier excepción durante el procesamiento
                    host_data[result.name if hasattr(
                        result, "name") else "unknown"] = f"Error procesando resultado: {str(e)}"

            # Add this host's data to the final results dictionary
            final_results[host] = host_data
    except Exception as e:
        # Capturar cualquier excepción general durante el procesamiento
        final_results["error"] = f"Error general procesando resultados: {str(e)}"

    return final_results
