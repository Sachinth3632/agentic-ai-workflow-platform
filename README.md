# Agentic AI Workflow Automation Platform

An Agentic AI platform designed to automate HR and Finance workflows using LLMs, tool calling, RAG, and REST APIs.

## Architecture

User
↓
Streamlit Frontend
↓
FastAPI Backend
↓
LangGraph Agent
↓
Azure OpenAI
↓
Tool Selection
├── Database Tool
├── RAG Document Search
└── Report Generation
↓
Final Response

## Features

- Agentic AI workflow orchestration
- LLM-based intent understanding
- Tool calling
- HR and Finance database queries
- RAG-based document retrieval
- Structured report generation
- FastAPI REST API
- Streamlit user interface
- FAISS vector search
- SQLAlchemy database layer
- Docker-ready architecture

## Technology Stack

- Python
- LangChain
- LangGraph
- Azure OpenAI
- FastAPI
- Streamlit
- FAISS
- SQLAlchemy
- SQLite
- Pydantic
- Docker
- Git/GitHub

## Project Structure

```text
agentic-ai-workflow-platform/
│
├── backend/
│   └── app/
│       ├── agents/
│       ├── database/
│       ├── models/
│       ├── rag/
│       ├── services/
│       └── tools/
│
├── frontend/
│   └── app.py
│
├── data/
│   └── documents/
│
├── tests/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md