from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate


def query_stock(ticker: str, question: str, stock_analysis: dict, model="llama3.2:latest") -> str:
    llm = OllamaLLM(model=model)  # Adjust to your setup

    news_summary = stock_analysis.get("news")
    stock_info = stock_analysis.get("stock_info")
    sentiment = stock_analysis.get("sentiment")

    context = f"""
### Stock Ticker:
{ticker}

### Stock Summary:
{stock_info}

### News Summary:
{news_summary}

### Sentiment:
{sentiment}
"""

    prompt = PromptTemplate.from_template("""
You are a financial assistant AI. Given the following data about a stock, answer the user's question.

{context}

User question: {question}
Answer:
""")

    chain = prompt | llm
    return chain.invoke({"context": context, "question": question})
