# browser_agent.py
from langchain.agents import Tool
from langchain.tools import StructuredTool
from langchain_ollama.chat_models import ChatOllama
from langchain.agents import initialize_agent, AgentType
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor

class BrowserBot:
    def __init__(self):
        self.pw = sync_playwright().start()
        self.browser = self.pw.chromium.launch(headless=False)
        self.page = self.browser.new_page()

    def navigate(self, url):
        self.page.goto(url)
        return f"Navigated to {url}"

    def click_text(self, text):
        self.page.get_by_text(text).click()
        return f"Clicked on text '{text}'"

    def type_in_field(self, selector, value):
        self.page.fill(selector, value)
        return f"Typed '{value}' into '{selector}'"

    def back(self):
        self.page.go_back()
        return "Navigated back to the previous page."

    def check_text(self, text):
        try:
            self.page.wait_for_selector(f"text={text}", timeout=3000)
            return f"✅ Text '{text}' found on the page."
        except PlaywrightTimeoutError:
            raise ValueError(f"❌ Text '{text}' NOT found on the page.")

    def close(self):
        try:
            self.browser.close()
            self.pw.stop()
            print(" ✅ Browser closed successfully.")
        except Exception as e:
            print(f"❌ Error closing browser: {str(e)}")


def create_agent(browser_bot, model="llama3.2:latest"):
    tools = [
        Tool(
            name="NavigateTool",
            func=browser_bot.navigate,
            description="Use this to go to navigate to a URL."
        ),
        Tool(
            name="ClickTool",
            func=browser_bot.click_text,
            description="Use this to click elements by visible text."
        ),
        Tool(
            name="TypeTool",
            func=browser_bot.type_in_field,
            description="Use this to type into an input field using a CSS selector."
        ),
        Tool(
            name="CheckTextTool",
            func=browser_bot.check_text,
            description="Use this to check if a specific text is present on the page."
        ),
        StructuredTool.from_function(
            name="BackTool",
            func=browser_bot.back,
            description="Use this to navigate back to the previous page.",
            args_schema=None  # Explicitly define no inputs
        ),
        # Add more tools as needed
        # Tool(
        #     name="CloseTool",
        #     func=browser_bot.close,
        #     description="Use this to close the browser."
        # ),
        StructuredTool.from_function(
            name="CloseTool",
            func=browser_bot.close,
            description="Use this to close the browser. ONLY use when explicitly instructed to close the browser.",
            args_schema=None  # Explicitly define no inputs
        )
    ]


    # Define a structured prompt template with examples
    prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(
            "You are a strict UI test automation assistant. "
            "Your only task is to interact with a web page using the tools provided. "
            "Available tools:\n"
            "- NavigateTool(url)\n"
            "- ClickTool(text)\n"
            "- TypeTool(selector, text)\n"
            "- CheckTextTool(text)\n"
            "- CloseTool() — ONLY use when explicitly instructed to close the browser.\n\n"
            "NEVER perform any action outside the test instructions.\n"
            "NEVER use CloseTool unless told to.\n"
            "DO NOT Close the browser unless explicitly instructed by the test script.\n"
        ),
        HumanMessagePromptTemplate.from_template(
            "Instructions:\n"
            "{input}"
        ),
        HumanMessagePromptTemplate.from_template(
            "Use tools strictly as needed to fulfill the instructions. Do not assume or add steps."
        ),
        MessagesPlaceholder("agent_scratchpad")
    ])

    llm = ChatOllama(temperature=0, model=model, tools=tools)


    agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    return agent_executor
