import yfinance as yf
from duckduckgo_search import DDGS
import requests
import gradio as gr
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from agents.search_news import search_news, summarize_news
from agents.stock_info_analyzer import fetch_stock_info, analyze_sentiment
from dotenv import load_dotenv
import os
from utils import format_stock_info
from agents.query_stock import query_stock

# Load environment variables from .env file
load_dotenv()

# Global variables
stock_memory = {}


NEWS_SUMMARIZER_MODEL = os.environ.get("NEWS_SUMMARIZER_MODEL", "llama3.2:latest")
STOCK_ANALYZER_MODEL = os.environ.get("STOCK_ANALYZER_MODEL", "llama3.2:latest")
def multi_agent_pipeline(ticker: str) -> tuple[str, str, str]:
    # Initialize placeholders
    news_summary = ""
    stock_info = ""
    sentiment = ""

    try:
        try:
            stock_info = fetch_stock_info(ticker)
        except Exception as e:
            stock_info = f"Failed to retrieve stock info: {e}"

        # Get company name
        company_name = stock_info.get("name")
        company_news = stock_info.get("news")
        formatted_stock_info = format_stock_info(stock_info)

        # Agent A: Search news
        try:
            raw_news = search_news(company_name)
            if not raw_news.strip():
                news_summary = "No recent news found."
            else:
                # Summarize news
                try:
                    # combine raw_news with stock_info.get("news") dictionary
                    raw_news = f"{raw_news}\n\n{company_news}"

                    news_summary = summarize_news(raw_news, model=NEWS_SUMMARIZER_MODEL)
                except Exception as e:
                    news_summary = f"Failed to summarize news: {e}"
        except Exception as e:
            news_summary = f"Failed to search news: {e}"

        # Agent B: Sentiment analysis
        if "Failed" not in news_summary and "Failed" not in formatted_stock_info:
            try:
                sentiment = analyze_sentiment(news_summary, formatted_stock_info, model=STOCK_ANALYZER_MODEL)
            except Exception as e:
                sentiment = f"Sentiment analysis failed: {e}"
        else:
            sentiment = "Sentiment not available due to missing input data."

        stock_memory[ticker.upper()] = {
            "news": news_summary,
            "stock_info": formatted_stock_info,
            "sentiment": sentiment,
        }

        return news_summary, formatted_stock_info, sentiment


    except Exception as e:
        return "❌ General error occurred.", "", str(e)



# Analysis function
def ui_analyze(ticker):
    if not ticker:
        return "", "", "", "", gr.update(interactive=True), gr.update(value="Please enter a ticker.")

    status_msg = f"Analyzing {ticker.upper()}..."
    news, info, sentiment = multi_agent_pipeline(ticker)
    status_msg = f"✅ Analysis complete for {ticker.upper()}."

    return (
        ticker.upper(),
        news,
        info,
        sentiment,
        gr.update(interactive=True),  # Enable Ask button
        gr.update(value=status_msg),  # Update status text
    )

# Query function (reuses last analyzed ticker)
def ui_query(ticker, question):
    if not ticker:
        return "Please analyze a stock first."

    # find the last analyzed ticker
    last_stock_analysis = {}
    ticker = ticker.upper()
    if ticker not in stock_memory:
        return "No stock information available. Please analyze a stock first."

    last_stock_analysis = stock_memory[ticker]

    return query_stock(ticker, question, last_stock_analysis, model=STOCK_ANALYZER_MODEL)


# 5. Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("# 📊 Stock Sentiment Analyzer with Memory")

    ticker_state = gr.State()

    # --- Stock Input Section ---
    ticker_input = gr.Text(label="Enter Stock Ticker", placeholder="e.g. AAPL")
    analyze_btn = gr.Button("Analyze")
    status_output = gr.Textbox(label="Status", interactive=False)
    news_output = gr.Markdown()
    info_output = gr.Markdown()
    sentiment_output = gr.Markdown()

    # --- User Question Section ---
    gr.Markdown("## 🤔 Ask a question about this stock")
    user_question = gr.Text(label="Your Question", placeholder="e.g. What is the market cap?")
    ask_btn = gr.Button("Ask", interactive=False)
    answer_output = gr.Markdown()

    # --- Analysis Trigger and UI Update ---
    analyze_btn.click(
        fn=ui_analyze,
        inputs=ticker_input,
        outputs=[
            ticker_state,
            news_output,
            info_output,
            sentiment_output,
            ask_btn,
            status_output,
        ],
        preprocess=False,  # Don’t validate inputs automatically
        postprocess=False,  # Manual update of state/output
    ).then(
        lambda: gr.update(interactive=True), None, [analyze_btn]  # Re-enable Analyze button
    )

    # Disable Analyze button while it's running
    analyze_btn.click(
        lambda: gr.update(interactive=False), None, [analyze_btn]
    )

    ask_btn.click(
        fn=ui_query,
        inputs=[ticker_state, user_question],
        outputs=answer_output
    )

demo.launch()
