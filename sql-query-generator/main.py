import gradio as gr
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain.agents import Tool, initialize_agent, AgentType
from langchain.chains import LLMChain
from sqlalchemy import create_engine, text
from langchain.tools import Tool
from langchain.chains.sql_database.query import create_sql_query_chain
from tools import get_schema

# 1. Define schema & example queries
schema_description = """
You are a SQL expert. The database has the following tables:

Table: users
- id (INTEGER, Primary Key)
- name (TEXT)
- email (TEXT)
- created_at (DATETIME)

Table: orders
- id (INTEGER, Primary Key)
- user_id (INTEGER, Foreign Key -> users.id)
- amount (FLOAT)
- status (TEXT)
- created_at (DATETIME)

Database Type: PostgreSQL
Database Name: my_database

Example Queries:
-- Get all users who registered in the last 30 days
SELECT * FROM users WHERE created_at >= DATE('now', '-30 day');

-- Get total sales grouped by user
SELECT user_id, SUM(amount) as total_sales FROM orders GROUP BY user_id;

-- Get all orders for a specific user
SELECT * FROM orders WHERE user_id = 1;
"""

# 2. Prompt template
prompt = PromptTemplate(
    input_variables=["question"],
    template=schema_description + """
    \n\nConvert the following natural language question into a valid SQL query:
    \nUse only columns from these tables. Do not explain anything. Output ONLY the SQL query.\n
    \nUse get_schema to get the schema of a table and only call it once.\n
    \nQuestion: {question}\nSQL:"""
)

# 3. Ollama LLM
llm = OllamaLLM(model="llama3.2:latest", temperature=0.0)
sql_chain = LLMChain(prompt=prompt, llm=llm)

# create_sql_query_chain(llm, sql_chain, verbose=True)

# 4. Register as a LangChain Tool
tools = [
    Tool(
        name="get_schema",
        func=get_schema,
        description="Returns the schema of a SQL table. Input should be the table name."
    )
]

agent_executor = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    max_iterations=3,
)

def ask_agent(question):
    return agent_executor.run(question).strip()

# 4. Generate SQL
def generate_sql(question):
    sql = sql_chain.run(question).strip()
    return sql

# 5. Run SQL
def run_sql(sql, db_url="sqlite:///example.db"):
    try:
        engine = create_engine(db_url)
        with engine.connect() as conn:
            result = conn.execute(text(sql))
            rows = result.fetchall()
            if not rows:
                return "No results."
            return "\n".join(str(row) for row in rows)
    except Exception as e:
        return f"Error executing SQL: {e}"

# 6. Gradio interface function
def handle_question(question, execute_tools, execute):
    sql = ""
    if execute_tools:
        sql = ask_agent(question)
    else:
        sql = generate_sql(question)

    if execute:
        result = run_sql(sql)
        return sql, result
    else:
        return sql, "SQL execution skipped."

# 7. Launch Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("# 🧠 Natural Language to SQL (Powered by Ollama)")
    with gr.Row():
        question_input = gr.Textbox(label="Ask a Question", placeholder="e.g., Show me all completed orders", lines=2)
    execute_checkbox = gr.Checkbox(label="Execute SQL on database", value=False)
    execute_tools = gr.Checkbox(label="Execute SQL on Tools", value=False)
    submit_btn = gr.Button("Generate SQL")

    sql_output = gr.Textbox(label="Generated SQL")
    result_output = gr.Textbox(label="Query Result")

    # submit_btn.click(fn=ask_agent, inputs=[question_input], outputs=[sql_output])
    submit_btn.click(fn=handle_question, inputs=[question_input, execute_tools, execute_checkbox], outputs=[sql_output, result_output])

demo.launch()

# response = handle_question("Show me all completed orders", True)
# print("Generated SQL:", response[0])
# print("Query Result:", response[1])