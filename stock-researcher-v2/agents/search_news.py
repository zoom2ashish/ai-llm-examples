from duckduckgo_search import DDGS
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

def search_news(query: str, max_results=5) -> str:
    with DDGS() as ddgs:
        results = ddgs.text(query + " stock news", max_results=max_results)
        news_str = ""
        for i, r in enumerate(results, start=1):
            title = r.get("title", "No Title")
            snippet = r.get("body", "No Snippet")
            url = r.get("href", "No URL")
            news_str += f"### {i}. {title}\n{snippet}\n🔗 {url}\n\n"
        return news_str.strip()

def summarize_news(news_text: str, model="llama3.2:latest") -> str:
    llm = OllamaLLM(model=model)
    prompt = PromptTemplate.from_template("""
You are a financial analyst AI that specializes in stock trading and analyze news that impact stock prices.
Summarize the following company news that is relevant to stock trading.
The summary should be concise and highlight the most important points.
Also, provide a brief sentiment analysis (Positive, Neutral, Negative) based on the news content.
### News:

{news}
""")
    chain = prompt | llm

    return chain.invoke({"news": news_text}).strip()