import yfinance as yf
from duckduckgo_search import DDGS
import requests
import gradio as gr
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

# 1. Fetch stock information
def fetch_stock_info(ticker: str) -> dict:
    stock = yf.Ticker(ticker)
    info = stock.info
    return {
        "name": info.get("shortName", "N/A"),
        "currentPrice": info.get("currentPrice", "N/A"),
        "marketCap": info.get("marketCap", "N/A"),
        "trailingPE": info.get("trailingPE", "N/A"),
        "forwardPE": info.get("forwardPE", "N/A"),
        "summary": info.get("longBusinessSummary", "N/A"),
    }

# 2. Fetch recent news from DuckDuckGo
def fetch_company_news(query: str, max_results: int = 3) -> list:
    with DDGS() as ddgs:
        return [
            {"title": r["title"], "snippet": r["body"], "url": r["href"]}
            for r in ddgs.text(query + " stock news", max_results=max_results)
        ]

# 3. Analyze with Ollama
def analyze_with_langchain_ollama(stock_info: dict, news_articles: list) -> str:
    template = """
You are a financial analyst AI. Based on the following stock data and recent company news, evaluate the overall sentiment of the stock.

Stock Information:
{name}
Current Price: ${currentPrice}
Market Cap: {marketCap}
Trailing P/E: {trailingPE}
Forward P/E: {forwardPE}
Summary: {summary}

Recent News Articles:
{news}

Return the sentiment as **Positive**, **Neutral**, or **Negative**, and explain briefly.
"""

    prompt = PromptTemplate.from_template(template)
    llm = OllamaLLM(model="llama3.2:latest")

    chain = prompt | llm

    news_formatted = "\n".join(f"- {item['title']}: {item['snippet']}" for item in news_articles)

    inputs = {
        "name": stock_info["name"],
        "currentPrice": stock_info["currentPrice"],
        "marketCap": stock_info["marketCap"],
        "trailingPE": stock_info["trailingPE"],
        "forwardPE": stock_info["forwardPE"],
        "summary": stock_info["summary"][:500],
        "news": news_formatted,
    }

    result = chain.invoke(inputs)
    return result.strip()

# 4. Full pipeline to run in Gradio
def stock_sentiment_pipeline(ticker: str):
    try:
        stock_info = fetch_stock_info(ticker)
        news = fetch_company_news(stock_info['name'])
        sentiment = analyze_with_langchain_ollama(stock_info, news)

        info_str = f"""🧾 **{stock_info['name']}**

- Current Price: ${stock_info['currentPrice']}
- Market Cap: {stock_info['marketCap']}
- P/E (TTM): {stock_info['trailingPE']}
- P/E (Forward): {stock_info['forwardPE']}

📄 Summary:
{stock_info['summary'][:500]}...
        """

        return info_str, sentiment
    except Exception as e:
        return "Error fetching stock info. Please check the ticker.", str(e)

# 5. Gradio UI
with gr.Blocks(title="Stock Sentiment Analyzer") as demo:
    gr.Markdown("# 📊 Stock Sentiment Analyzer with Ollama")

    with gr.Row():
        ticker_input = gr.Textbox(label="Enter Stock Ticker", placeholder="e.g., AAPL")
        analyze_btn = gr.Button("Analyze")

    with gr.Row():
        stock_output = gr.Markdown()
        sentiment_output = gr.Textbox(label="Sentiment", interactive=False)

    analyze_btn.click(fn=stock_sentiment_pipeline, inputs=[ticker_input], outputs=[stock_output, sentiment_output])

demo.launch()
