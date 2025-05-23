from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import Tool

search_tool = Tool(
    name="search_web",
    func=DuckDuckGoSearchRun().run,
    description="Search the web to answer questions about current events. You should ask targeted questions."
)

def dummy_tool(input: str) -> str:
    return "No tools available."


tools = [
    search_tool,
    # Tool.from_function(
    #     func=dummy_tool,
    #     name="DummyTool",
    #     description="A placeholder tool that returns a dummy response."
    # )
]