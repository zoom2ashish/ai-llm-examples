from langchain.tools import tool
from langchain.agents import initialize_agent, AgentType, Tool
from langchain_community.llms import Ollama
from langchain.agents.agent_toolkits import create_sql_agent

# Mock schema
MOCK_SCHEMA = {
    "users": "Table: users\nColumns:\n- id: INTEGER\n- name: TEXT\n- email: TEXT",
    "orders": "Table: orders\nColumns:\n- id: INTEGER\n- user_id: INTEGER\n- total: FLOAT",
}

@tool
def get_schema(table_name: str) -> str:
    """Returns schema for a given table."""
    return MOCK_SCHEMA.get(table_name.replace("'", "").lower(), "Table not found.")
