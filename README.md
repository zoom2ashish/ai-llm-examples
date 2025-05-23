# ai-llm-examples
This is a collection of examples demonstrating how to use the Ollama LLM (Language Model) for various tasks. The examples cover a range of topics, including stock analysis, data processing, and more.
The goal is to provide practical use cases for leveraging the capabilities of the LLM in different scenarios, and learning how to integrate it into your projects.
## Getting Started
To get started, you'll need to have Ollama installed and running on your system. You can find instructions on how to install Ollama on various platforms in the official documentation.
Once you have Ollama set up, you can run the examples by following the instructions below.
## Running the Examples
To run the examples, you'll need to have Python installed on your system. You can install the required dependencies by running the following command:
```
pip install -r requirements.txt
```
After installing the dependencies, you can run the examples by executing the following command:
```
python <example_name>/main.py
```
Replace `<example_name>` with the directory name of the example you want to run.


## Example List
- `stock-researcher`: A stock analysis tool that fetches stock data from Yahoo Finance, company news from DuckDuckGo, and performs sentiment analysis using the LLM. Links to the [README](stock-researcher/README.md) for more details.
- `sql-query-generator`: A tool that generates SQL queries based on user input. It uses the LLM to understand the user's requirements and generate the appropriate SQL code. Links to the [README](sql-query-generator/README.md) for more details.
- `stock-researcher-v2`: An updated version of the stock analysis tool with improved features and functionality. Uses multiple agents to fetch stock data and news, and provides a more comprehensive analysis of the stock market. Short-term memory is used to store the context of the conversation, allowing for more accurate and relevant responses from the LLM. Links to the [README](stock-researcher-v2/README.md) for more details.

## My Learning Tools
- [Prompt Engineering](https://www.promptingguide.ai/)
- [Langchain](https://python.langchain.com/docs/introduction/)
- [Langchain Tools Integrations](https://python.langchain.com/docs/integrations/tools/)
- [Vector Stores and Embeddings](https://python.langchain.com/docs/concepts/embedding_models/)
- [Ollama LLM](https://ollama.com/)
- [Gradio](https://www.gradio.app/docs)
- [Structured Output](https://python.langchain.com/docs/how_to/structured_output/)

## My Definitions
- **LLM**: Language Model, a type of artificial intelligence model that is trained to understand and generate human language. It is like a fresh college graduate who has just learned a new language and is eager to apply their knowledge in real-world scenarios.
- **Prompt**: A prompt is a piece of text or instruction given to the LLM (my Fresh Graduate Grad here) to guide its response. It is like a question or request that helps the model understand what information or action is being sought.
- **Agent**: An agent is a fresh college grad turned into a professional who can take action based on the information provided. In the context of LLMs, an agent is a system that can perform tasks or make decisions based on the input it receives. Agent has tools that can help it perform specific actions or tasks, and has general knowledge about the world from LLM.
- **Tool**: A tool is a specific capability or function that an agent can use to perform tasks. It is like a set of specialized skills or resources that the agent can leverage to achieve its goals. For example, an agent may have tools for data analysis, web scraping, or natural language processing.
- **Prompt Engineering**: The process of designing and optimizing prompts to elicit the desired responses from LLMs. For LLM, bad question asked, then bad response received. Like Arjun asking a question to Krishna, and Krishna giving the right answer that leads to Bhagwad Gita. Prompt engineering is like asking the right question to get the right answer.
- **Structured Output**: A structured output is a specific format or structure in which the LLM generates its response. It is like a well-organized report or document that presents information in a clear and concise manner. It is like telling my college grad to write a report in a specific format, such as a research paper or a business proposal. Structured output helps ensure that the information is presented in a way that is easy to understand and use.
- **Vector Store**: A vector store is a database or storage system that is designed to store and retrieve high-dimensional vectors. It is like a library that organizes and categorizes books based on their content, making it easy to find and access specific information.
- **Embeddings**: Embeddings are numerical representations of data, such as words or images, that capture their meaning and relationships in a high-dimensional space. It is like a map that shows the location of different concepts in relation to each other, allowing for easy navigation and understanding of their connections.
## Understanding Embeddings Through a Beach Analogy

**Embeddings** are numerical representations of data—such as words, phrases, or images—converted into multi-dimensional vectors. Think of them as coordinates that place a concept in a "semantic space" where similar concepts are positioned close together.

### 🌴 Example: The Word "Beach"

Imagine we assign the word **"Beach"** a vector—a long list of numbers—that captures its meaning: sunshine, sand, water, fun, and relaxation. This vector doesn’t just store the word; it stores its **context** and **semantic meaning**.

Now consider related words like:

- ☀️ **Sun**
- 🏖️ **Sand**
- 🌊 **Ocean**
- 🐚 **Seashells**
- 🌦️ **Weather**
- 🏰 **Sandcastle**
- 🏐 **Volleyball**
- 🏓 **Beachball**
- 😎 **Tanning**

Each of these would also be represented by their own vectors, located **close to "Beach"** in this semantic space, because they often appear in similar contexts.

### 📚 Vector Store

A **vector store** is like a digital library that holds these vectors. When you search for "Beach", it doesn’t just look for that exact word. Instead, it retrieves **all nearby vectors**, such as “Sun”, “Ocean”, or “Tanning”, based on **semantic similarity**.

### 🔍 Summary

- **Embeddings** convert meaning into numbers.
- These vectors help machines **understand relationships** between concepts.
- A **vector store** makes it easy to **organize and retrieve** this information efficiently based on meaning.

This is how systems like ChatGPT, recommendation engines, or semantic search tools return highly relevant results—even for things you didn’t explicitly type.

