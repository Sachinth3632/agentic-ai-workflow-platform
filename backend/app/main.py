from fastapi import FastAPI
from pydantic import BaseModel

from backend.app.database.db import init_db
from backend.app.agents.workflow_agent import run_agent


app = FastAPI(
    title="Agentic AI Workflow Automation Platform",
    description="Agentic AI platform for HR and Finance workflow automation.",
    version="1.0.0"
)


class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    response: str


@app.on_event("startup")
def startup_event():
    init_db()


@app.get("/")
def root():
    return {
        "message": "Agentic AI Workflow Automation Platform",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post(
    "/api/v1/agent/query",
    response_model=QueryResponse
)
def agent_query(request: QueryRequest):

    response = run_agent(request.query)

    return QueryResponse(
        response=response
    )