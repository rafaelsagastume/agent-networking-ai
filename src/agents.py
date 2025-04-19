from agno.agent import Agent
from agno.models.openai import OpenAIChat

from src.network_data.arp_table import collect_network_data_arp_table
from src.network_data.bgp import collect_network_data_bgp_neighbors
from src.network_data.facts import collect_network_data_facts
from src.network_data.interfaces import collect_network_data_interfaces

agent = Agent(
    name="Ingeniero de Redes",
    description="Ingeniero de Redes con acceso a datos de red",
    model=OpenAIChat(id="gpt-4.1-mini"),
    tools=[
        collect_network_data_facts,
        collect_network_data_interfaces,
        collect_network_data_bgp_neighbors,
        collect_network_data_arp_table,
    ],
    instructions="""
    0. Listen carefully to the user's query before executing any functions.
    1. Only execute network data collection functions when necessary for answering the query.
    2. If the user's question can be answered without collecting network data, avoid running those functions.
    3. Present information to the user in table format whenever possible.
    """,
    markdown=True
)
