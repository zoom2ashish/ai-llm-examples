# main.py
import os
from dotenv import load_dotenv
from browser_agent import BrowserBot, create_agent

load_dotenv()

# Define array of test cases
test_cases = [
    {
        "name": "Test My Home Page",
        "input": """
        1. Navigate to the URL "https://zoom2ashish.github.io/".
        2. Check if the text 'Ashish Patel' is present on the page.
        3. Click on the text 'Github' link button on the page.
        4. Scroll to the bottom of the page.
        """,
        "expected_result": "✅ Text 'Ashish Patel' found on the page and Github page opened successfully."
    },
    {
        "name": "Test Case 2",
        "input": """
        1. Navigate to the URL "https://zoom2ashish.github.io/".
        2. Check if the text 'Ashish Patel' is present on the page.
        3. Click on the text 'LinkedIn' link button on the page.
        4. Scroll to the bottom of the page.
        5. Navigate back to the previous page.
        """,
        "expected_result": "✅ Text 'Ashish Patel' found on the page and LinkedIn page opened successfully."
    },
    # Error Condition for not existing text
    {
        "name": "Test Case 3 - Error Condition",
        "input": """
        1. Navigate to the URL "https://zoom2ashish.github.io/".
        2. Check if the text "some_non_existent_text" is present on the page.
        """,
        "expected_result": "❌ Text 'some_non_existent_text' NOT found on the page."
    },

]

def main():
    browser_bot = BrowserBot()
    agent = create_agent(browser_bot)

    try:
        for test_case in test_cases:
            try:
                print(f"Running test case: {test_case['name']}")
                agent.invoke({"input": test_case["input"], "expected_result": test_case["expected_result"]})
                print(f"✅ Test {test_case['name']} Passed!")
            except Exception as e:
                print(str(e))
                print(f"❌ Test {test_case['name']} Failed")
            print("-" * 40)
    except Exception as e:
        print(str(e))
        print("An error occurred.")
    finally:
        browser_bot.close()
        print("Browser closed successfully.")

if __name__ == "__main__":
    main()
