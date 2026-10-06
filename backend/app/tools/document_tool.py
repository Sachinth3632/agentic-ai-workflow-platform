from backend.app.rag.vector_store import search_documents


def retrieve_documents(query: str) -> str:
    """
    Retrieve relevant information from internal company documents.
    """

    return search_documents(query)