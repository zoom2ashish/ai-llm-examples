# main.py
import os
from dotenv import load_dotenv
from browser_agent import BrowserBot, create_agent

load_dotenv()

def main():
    browser_bot = BrowserBot()
    agent = create_agent(browser_bot)

    try:
        agent.invoke({"input": """
        1. Navigate to the URL "https://zoom2ashish.github.io/".
        2. Check if the text 'Ashish Patel' is present on the page.
        3. Click on the text 'Github' link button on the page.
        4. Navigate back to the previous page.
        """})
        print("✅ Test Passed!")
    except Exception as e:
        print(str(e))
        print("❌ Test Failed!")
    finally:
        browser_bot.close()

if __name__ == "__main__":
    main()
