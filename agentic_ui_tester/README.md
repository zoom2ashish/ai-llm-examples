# Agentic UI Tester

## Overview
Agentic UI Tester is a project that automates UI testing using a browser automation bot integrated with LangChain agents. It leverages Playwright for browser interactions and Ollama LLM for intelligent decision-making based on test instructions.

## Features
- Automate browser navigation, clicks, typing, and text verification.
- Use LangChain agents to execute structured test instructions.
- Integrate tools for specific browser actions (e.g., Navigate, Click, Type, Check Text).
- Perform intelligent UI testing with a strict adherence to provided instructions.

## How It Works
1. **BrowserBot**: A Playwright-based bot that handles browser interactions such as navigation, clicking, typing, and text verification.
2. **LangChain Agent**: An agent created using the `create_tool_calling_agent` function, which uses tools to interact with the browser based on test instructions.
3. **Tools**: A set of tools (NavigateTool, ClickTool, TypeTool, CheckTextTool, BackTool, CloseTool) that define specific browser actions.
4. **Agent Execution**: The agent executes test instructions step-by-step using the tools provided.

## File Structure
- `.env`: Environment variables for configuring the browser agent model.
- `browser_agent.py`: Contains the implementation of the BrowserBot and LangChain agent creation.
- `main.py`: Main script to execute the agent and perform UI testing.
- `requirements.txt`: Lists the dependencies required for the project.

## Requirements
Install the required dependencies using the following command:
```bash
pip install -r requirements.txt
```

## Usage
1. Set the browser agent model in the .env file:
 ```
 BROWSER_AGENT_MODEL=llama3.2:latest
```
2. Run the main.py script to execute the UI test:
```
python main.py
```
3. The agent will perform the following actions based on the test instructions:
- Navigate to a URL.
- Check if specific text is present on the page.
- Click on a button or link.
- Navigate back to the previous page.

## Example Test Instructions
The following instructions are executed by the agent:
```
1. Navigate to the URL "https://zoom2ashish.github.io/".
2. Check if the text 'Ashish Patel' is present on the page.
3. Click on the text 'Github' link button on the page.
4. Navigate back to the previous page.
```

## Technologies Used
- Playwright: Browser automation framework for handling UI interactions.
- LangChain: Framework for building agents and integrating tools.
- Ollama LLM: Language model for intelligent decision-making.
- Python: Programming language for implementing the project.

## Future Improvements
- Add support for more complex test scenarios.
- Enhance error handling and reporting mechanisms.
- Integrate additional tools for advanced browser - interactions.
- Support headless browser mode for faster execution.

## My Learnings
- Understanding how to create and use LangChain agents for browser automation.
- Prompt engineering for effective test instructions.
- Integrating Playwright with LangChain for UI testing.

## License
This project is licensed under the MIT License. See the LICENSE file for details.