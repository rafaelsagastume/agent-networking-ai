from agno.agent import Agent
from agno.models.openai import OpenAIChat

from src.network_data.arp_table import collect_network_data_arp_table
from src.network_data.bgp import collect_network_data_bgp_neighbors
from src.network_data.bgp_config import collect_network_data_bgp_config
from src.network_data.bgp_neighbors_detail import \
    collect_network_data_bgp_neighbors_detail
from src.network_data.config import collect_network_data_config
from src.network_data.environment import collect_network_data_environment
from src.network_data.facts import collect_network_data_facts
from src.network_data.firewall_policies import \
    collect_network_data_firewall_policies
from src.network_data.interfaces import collect_network_data_interfaces
from src.network_data.interfaces_counters import \
    collect_network_data_interfaces_counters
from src.network_data.interfaces_ip import collect_network_data_interfaces_ip
from src.network_data.ipv6_neighbors_table import \
    collect_network_data_ipv6_neighbors_table
from src.network_data.lldp_neighbors import collect_network_data_lldp_neighbors
from src.network_data.lldp_neighbors_detail import \
    collect_network_data_lldp_neighbors_detail
from src.network_data.mac_address_table import \
    collect_network_data_mac_address_table
from src.network_data.network_instances import \
    collect_network_data_network_instances
from src.network_data.ntp_peers import collect_network_data_ntp_peers
from src.network_data.ntp_servers import collect_network_data_ntp_servers
from src.network_data.ntp_stats import collect_network_data_ntp_stats
from src.network_data.optics import collect_network_data_optics
from src.network_data.probes_config import collect_network_data_probes_config
from src.network_data.probes_results import collect_network_data_probes_results
from src.network_data.route_to import collect_network_data_route_to
from src.network_data.snmp_information import \
    collect_network_data_snmp_information
from src.network_data.users import collect_network_data_users
from src.network_data.vlans import collect_network_data_vlans

agent = Agent(
    name="Network Engineer",
    description="A network engineer with access to comprehensive network data",
    model=OpenAIChat(id="o4-mini"),
    tools=[
        # Original getters
        collect_network_data_facts,
        collect_network_data_interfaces,
        collect_network_data_bgp_neighbors,
        collect_network_data_arp_table,
        # New getters
        collect_network_data_bgp_config,
        collect_network_data_bgp_neighbors_detail,
        collect_network_data_config,
        collect_network_data_environment,
        collect_network_data_firewall_policies,
        collect_network_data_interfaces_counters,
        collect_network_data_interfaces_ip,
        collect_network_data_ipv6_neighbors_table,
        collect_network_data_lldp_neighbors,
        collect_network_data_lldp_neighbors_detail,
        collect_network_data_mac_address_table,
        collect_network_data_network_instances,
        collect_network_data_ntp_peers,
        collect_network_data_ntp_servers,
        collect_network_data_ntp_stats,
        collect_network_data_optics,
        collect_network_data_probes_config,
        collect_network_data_probes_results,
        collect_network_data_route_to,
        collect_network_data_snmp_information,
        collect_network_data_users,
        collect_network_data_vlans,
    ],
    instructions="""
    You are a network engineer with access to detailed network data via specialized collection functions.

    Guidelines:
    1. Fully understand the user's request before invoking any function.
    2. Call only the functions necessary to retrieve data required for the answer.
    3. If the question can be addressed without fetching data, provide a direct response.
    4. Format all retrieved data as markdown tables, grouped by device.

    Notes:
    - Each function returns JSON data per device in the inventory.
    - Clearly label each table with the device name and the type of data presented.
    """,
    markdown=True
)
