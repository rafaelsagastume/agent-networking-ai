import json
import logging

from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result

from src.result_processor import process_network_results

nr = InitNornir(config_file="config.yaml")

print(nr.inventory.hosts)
results = nr.run(
    task=napalm_get, getters=["facts", "interfaces"]
)

# Procesar los resultados usando la función de src/result_processor.py
final_results = process_network_results(results)

# Print the final dictionary with all results
print(json.dumps(final_results, indent=4))
