import yfinance as yf
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

def fetch_stock_info(ticker: str) -> dict:
    stock = None
    info = {}
    info["ticker"] = ticker
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
    except Exception as e:
        print(f"Error fetching stock info for {ticker}: {e}")
        return {}

    news = ""
    for i, item in enumerate(stock.news[:5], start=1):
        content = item.get("content", {})
        title = content["title"] if "title" in content else "No Title"
        summary = content["summary"] if "summary" in content else "No Summary"
        url = content["canonicalUrl"]["url"] if "canonicalUrl" in content else "No URL"
        news += f"### {i}. {title}\n{summary}\n🔗 {url}\n\n"

    news = news.strip()
    if not news:
        news = "No recent news found."

    return {
        "name": info.get("shortName", "N/A"),
        "currentPrice": info.get("currentPrice", "N/A"),
        "marketCap": info.get("marketCap", "N/A"),
        "trailingPE": info.get("trailingPE", "N/A"),
        "forwardPE": info.get("forwardPE", "N/A"),
        "summary": info.get("longBusinessSummary", "N/A"),
        "recommendation": info.get("recommendationKey", "N/A"),
        "targetMeanPrice": info.get("targetMeanPrice", "N/A"),
        "targetHighPrice": info.get("targetHighPrice", "N/A"),
        "targetLowPrice": info.get("targetLowPrice", "N/A"),
        "fiftyTwoWeekLow": info.get("fiftyTwoWeekLow", "N/A"),
        "fiftyTwoWeekHigh": info.get("fiftyTwoWeekHigh", "N/A"),
        "fiftyTwoWeekRange": info.get("fiftyTwoWeekRange", "N/A"),
        "recommendations": stock.recommendations,
        "recommendationKey": info.get("recommendationKey", "N/A"),
        "totalDebt": info.get("totalDebt", "N/A"),
        "totalRevenue": info.get("totalRevenue", "N/A"),
        "debtToEquity": info.get("debtToEquity", "N/A"),
        "profitMargins": info.get("profitMargins", "N/A"),
        "news": news
    }


def analyze_sentiment(news_summary: str, stock_info: str, model="llama3.2:latest") -> str:
    llm = OllamaLLM(model=model)
    prompt = PromptTemplate.from_template("""
You are a financial analyst AI.

Given this stock information:

{stock_info}

And this summary of recent news:

{news_summary}

Evaluate the stock's sentiment as Positive, Neutral, or Negative, and explain briefly.
""")
    chain = prompt | llm
    return chain.invoke({
        "stock_info": stock_info,
        "news_summary": news_summary
    }).strip()