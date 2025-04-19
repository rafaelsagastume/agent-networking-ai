from agno.agent import Agent
from agno.models.openai import OpenAIChat

from src.network_data_collector import collect_network_data

agent = Agent(
    name="Ingeniero de Redes",
    description="Ingeniero de Redes con acceso a datos de red",
    model=OpenAIChat(id="o4-mini"),
    tools=[collect_network_data],
    instructions="""
    1. Please provide network data for analysis.
    2. Present information to the user in table format whenever possible.
    """,
    markdown=True
)
