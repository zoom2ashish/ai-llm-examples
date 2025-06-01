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
- `agentic-ui-tester`: A UI testing framework that uses LangChain agents to interact with web pages. It includes tools for navigation, clicking, typing, and checking text on the page. Links to the [README](agentic_ui_tester/README.md) for more details.
- `stock-researcher`: A stock analysis tool that fetches stock data from Yahoo Finance, company news from DuckDuckGo, and performs sentiment analysis using the LLM. Links to the [README](stock-researcher/README.md) for more details.
- `sql-query-generator`: A tool that generates SQL queries based on user input. It uses the LLM to understand the user's requirements and generate the appropriate SQL code. Links to the [README](sql-query-generator/README.md) for more details.
- `stock-researcher-v2`: An updated version of the stock analysis tool with improved features and functionality. Uses multiple agents to fetch stock data and news, and provides a more comprehensive analysis of the stock market. Short-term memory is used to store the context of the conversation, allowing for more accurate and relevant responses from the LLM. Links to the [README](stock-researcher-v2/README.md) for more details.
- `vector-db-similarity-search`: A vector database for similarity search using ChromaDB. It processes documents (PDF or Markdown), generates embeddings for text chunks, and allows querying through a Gradio-based user interface. Links to the [README](vector-db-similarity-search/README.md) for more details.

## My Learning Tools
- [Prompt Engineering](https://www.promptingguide.ai/)
- [Langchain](https://python.langchain.com/docs/introduction/)
- [Langchain Tools Integrations](https://python.langchain.com/docs/integrations/tools/)
- [Vector Stores and Embeddings](https://python.langchain.com/docs/concepts/embedding_models/)
- [Ollama LLM](https://ollama.com/)
- [Gradio](https://www.gradio.app/docs)
- [Structured Output](https://python.langchain.com/docs/how_to/structured_output/)


## 🧠 Understanding Core AI Concepts Using a Fresh College Graduate Analogy

To make the world of large language models (LLMs) easier to grasp, let’s imagine everything through the lens of a **fresh college graduate**—someone intelligent, trained, but still learning how to apply their knowledge in the real world.

---

### 💬 **LLM (Language Model)**

An LLM is like a **fresh college graduate** who has read a massive number of books and articles, written tons of essays, and is now ready to communicate intelligently. They may not know everything about a specific topic, but they can carry thoughtful conversations, write clearly, and understand nuanced questions.

---

### ✍️ **Prompt**

A **prompt** is like the **question or task** you give the graduate. Just as you might ask, “Can you summarize this article?” or “What are your thoughts on climate change?”, a prompt guides the LLM’s response. The clearer the prompt, the better the response.

---

### 🧑‍💼 **Agent**

An **agent** is that same college grad after they’ve **landed a job**. Now they don’t just answer questions—they **take action**. They might book tickets, look up prices, write reports, or fetch files using tools. The agent uses their education (LLM) and resources (tools) to **get things done**.

---

### 🧰 **Tool**

A **tool** is like a **specialized skill** the agent has learned or a software they use—like Excel for data analysis, Google for web search, or Photoshop for design. These tools help the agent do tasks that go beyond just talking or writing.

---

### 🎯 **Prompt Engineering**

**Prompt engineering** is like **asking the right question** in the right way to get the best answer. If you’re vague with your college grad, you’ll get a vague response. But if you ask clearly—like Arjun asking Krishna in the Bhagavad Gita—you’ll get a meaningful, transformative answer. Prompt engineering is the art of being specific and strategic with your prompts.

---

### 📄 **Structured Output**

A **structured output** is like asking the graduate to write a **formal report**, resume, or presentation in a specific format. Instead of a free-form answer, they respond with neatly organized sections (e.g., title, summary, bullets, conclusion). This makes the information **clear, actionable, and easy to use**.

---

### 🧭 **Embeddings**

**Embeddings** are like the graduate’s **mental map** of concepts. They don’t just memorize facts—they understand connections. For instance, they know “Beach” is close in meaning to “Sun,” “Sand,” and “Ocean.” These connections are stored as **vectors** (numerical coordinates) in a high-dimensional space, letting the grad “navigate” knowledge by meaning, not just by exact words.

---

### 📦 **Vector Store**

A **vector store** is like a **digital filing cabinet** that stores all those embeddings. When the graduate wants to find all topics related to “Beach,” they don’t search by exact words—they search the vector space and pull in nearby ideas like “Tanning,” “Volleyball,” or “Seashells.” It’s smarter than keyword search; it’s **semantic search**.

---

## 🌴 Embeddings Explained with a Beach Analogy

**Embeddings** convert meaning into numbers and help machines understand relationships between concepts.

### 🏖️ Example: The Word "Beach"

Let’s say we turn the word **"Beach"** into a vector—a string of numbers that capture its meaning: sunshine, relaxation, ocean, fun.

Now imagine related words:

- ☀️ **Sun**
- 🏖️ **Sand**
- 🌊 **Ocean**
- 🐚 **Seashells**
- 🌦️ **Weather**
- 🏰 **Sandcastle**
- 🏐 **Volleyball**
- 🏓 **Beachball**
- 😎 **Tanning**

These are also converted into vectors that land **close to “Beach”** in a high-dimensional space, because they often appear together or mean similar things.

---

### 📚 Vector Store

A **vector store** holds all these vectors. When you search for "Beach," it retrieves not only the exact match but also everything semantically related, like "Sun" or "Sandcastle"—because they live close by in that conceptual space.

---

### 🔍 Summary

- **LLM** = Smart grad who understands language.
- **Prompt** = Your question or task.
- **Agent** = Grad who can act and use tools.
- **Tool** = A skill or app that helps the agent get work done.
- **Prompt Engineering** = Asking smart questions.
- **Structured Output** = Organized, easy-to-read responses.
- **Embeddings** = The grad’s mental map of concepts.
- **Vector Store** = A digital library organized by meaning.

---

This analogy helps simplify complex AI concepts into something anyone can understand. Let me know if you'd like illustrations or flow diagrams added!
