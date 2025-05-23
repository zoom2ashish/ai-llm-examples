from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_community.llms import Ollama
from tools import tools  # Your DuckDuckGoSearch tool
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel


# 1. LLM
llm = Ollama(model="gemma:2b")


class ResearchResponse(BaseModel):
    topic: str
    summary: str
    tools: list[str]
    sources: list[str]

# Define the output parser
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

# 2. Prompt with required variables
prompt = ChatPromptTemplate.from_messages([
    [
        ("system",
         """
         You are a helpful research assistant which can help to generate a summary of a given research topic.
         Answer the user query using necessary sources and tools.
         Available tools: {tool_names}.
         Tool descriptions: {tools}.
         Wrap the output in this format and do not include any other text:\n{format_instructions}
         """),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
    ] # ✅ Required by ReAct agent
]).partial(
    format_instructions=parser.get_format_instructions(),
    tool_names=", ".join([tool.name for tool in tools]),
    tools="\n".join([f"{tool.name}: {tool.description}" for tool in tools]),  # Pass tool descriptions dynamically
    agent_scratchpad=[HumanMessage(content="This is the initial prompt")]  # ✅ Required by ReAct agent
)

# 3. Create the ReAct agent
agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)

# 4. Wrap in an executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 5. Invoke it
response = agent_executor.invoke({"input": "What is the capital of Germany?"})
print(response)
