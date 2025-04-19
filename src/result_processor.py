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

    for host, multi_result in results.items():
        host_data = {}
        for result in multi_result:
            if result.failed:
                host_data[result.name] = f"Failed: {result.exception}"
            else:
                # Transform any JSON strings in the result
                host_data[result.name] = parse_json_str(result.result)

        # Add this host's data to the final results dictionary
        final_results[host] = host_data

    return final_results
