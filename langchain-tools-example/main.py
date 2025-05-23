from langchain_ollama import OllamaLLM
from dotenv import load_dotenv
import os
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_react_agent, create_tool_calling_agent, AgentExecutor, initialize_agent, AgentType
from tools import search_tool, dummy_tool


# Load environment variables from .env file
load_dotenv()
tools = [search_tool]
llm = OllamaLLM(
    model="gemma2:2b",  # Make sure this model name matches the one you pulled with Ollama
    temperature=0.5
)

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    tools: list[str]
    sources: list[str]

parser = PydanticOutputParser(pydantic_object=ResearchResponse)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
         """
         You are a helpful research assistant which can help to generate a summary of a given research topic.
         Answer the user query using necessary sources and tools.
         Available tools are: {tool_names}
         Tool descriptions: {tools}.
         Wrap the output in this format and not include any other text\n{format_instructions}
         """),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(
    format_instructions=parser.get_format_instructions(),
    # tool_names=", ".join([tool.name for tool in tools]),
    # tools="\n".join([f"{tool.name}: {tool.description}" for tool in tools])  # Pass tool descriptions dynamically)
)
# this is not working with Ollama yet and giving error "This function requires a .bind_tools method be implemented on the LLM"
# agent = create_tool_calling_agent(
#     llm=llm,
#     tools=[],
#     prompt=prompt
# )

agent = initialize_agent(
    tools=tools,  # ✅ Now has DuckDuckGoSearchRun
    llm=llm,
    agent_type=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    max_iterations=3,
    return_intermediate_steps=True,
    agent_kwargs={
        "prompt": prompt,
        # "output_parser": parser,
    }
)

# agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)

# executor = AgentExecutor(
#     agent=agent,
#     verbose=True,
#     tools=tools
# )

raw_response = agent.invoke({
    "input": "tell me about the history of the internet"
})

# Print the raw response
print("Raw Response:", raw_response)