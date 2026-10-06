from langchain_openai import AzureChatOpenAI
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

from backend.app.config import settings
from backend.app.tools.database_tool import query_employee_data
from backend.app.tools.document_tool import retrieve_documents
from backend.app.tools.report_tool import generate_report


llm = AzureChatOpenAI(
    azure_deployment=settings.AZURE_OPENAI_CHAT_DEPLOYMENT,
    api_key=settings.AZURE_OPENAI_API_KEY,
    azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
    api_version=settings.AZURE_OPENAI_API_VERSION,
    temperature=0
)


@tool
def database_tool(query: str) -> str:
    """
    Query internal HR and Finance database information.
    """
    return query_employee_data(query)


@tool
def document_search_tool(query: str) -> str:
    """
    Search internal company documents using RAG.
    """
    return retrieve_documents(query)


@tool
def report_generation_tool(
    title: str,
    summary: str,
    data: str
) -> str:
    """
    Generate a structured business report.
    """
    return generate_report(
        title,
        summary,
        data
    )


tools = [
    database_tool,
    document_search_tool,
    report_generation_tool
]


SYSTEM_PROMPT = """
You are an enterprise Agentic AI Workflow Automation Assistant.

Your job is to understand the user's request and select the
appropriate tool to complete the task.

Available tools:

1. database_tool

Use this for:
- HR employee information
- Finance employee information
- salaries
- employee counts
- department information
- employee performance

2. document_search_tool

Use this for:
- company policies
- internal documents
- procedures
- internal knowledge
- document-based questions

3. report_generation_tool

Use this for:
- business reports
- structured summaries
- formatted reports

Rules:

- Understand the user's intent before selecting a tool.
- Use tools when the requested information is available through them.
- Never invent database or document information.
- Provide a clear and professional final response.
"""


agent = create_react_agent(
    llm,
    tools,
    prompt=SYSTEM_PROMPT
)


def run_agent(user_query: str) -> str:

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user_query
                }
            ]
        }
    )

    return result["messages"][-1].content