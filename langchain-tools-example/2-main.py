from langchain_ollama import OllamaLLM
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain.agents import initialize_agent, AgentType
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import Tool
from tools import search_tool

# Load environment variables from .env file
load_dotenv()

# Initialize the LLM
llm = OllamaLLM(
    model="gemma2:2b",  # Ensure this model is available in Ollama
    temperature=0.5
)

# Define the output schema
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    tools: list[str]
    sources: list[str]

# Define the output parser
parser = PydanticOutputParser(pydantic_object=ResearchResponse)


# Add the tool to the tools list
tools = [search_tool]

# Define the prompt template
prompt_template = """
You are a helpful research assistant which can help to generate a summary of a given research topic.
Answer the user query using necessary sources and tools.
Available tools are: {tool_names}.
Tool descriptions: {tools}.
Always wrap the output in this format:
{format_instructions}

User Query: {input}
"""

# format_instructions =  parser.get_format_instructions()
format_instructions = """
{
    "topic": "<topic>",
    "summary": "<summary>",
    "tools": ["<tool1>", "<tool2>"],
    "sources": ["<source1>", "<source2>"]
}
"""
# Create the prompt
prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["input"],
    partial_variables={
        "tool_names": ", ".join([tool.name for tool in tools]),
        "tools": "\n".join([f"{tool.name}: {tool.description}" for tool in tools]),
        "format_instructions": format_instructions,
    }
)

formatted_prompt = prompt.format(input="Tell me about the history of the internet.")

# Initialize the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    max_iterations=3,
    return_intermediate_steps=False,
    agent_kwargs={
        "prompt": formatted_prompt,
    }
)

# Invoke the agent with a query
raw_response = agent.invoke({
    "input": "Tell me about the history of the internet."
})


try:
    raw_output = raw_response.get("output", "")

    if raw_output:
        # Use the LLM to process the raw output and extract the topic
        topic_extraction_prompt = f"""
        Extract the topic name from the following response:
        {raw_output}

        Only return the topic name.
        """
        topic_name = llm(topic_extraction_prompt)
        print("Extracted Topic Name:", topic_name)
    else:
        print("No output found in the response.")

    print("Output:", raw_output)
    print("Topic Name:", topic_name)
except Exception as e:
    print("Error parsing response:", e)
