from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


VECTOR_STORE_PATH = Path("data/vector_store")
DOCUMENT_PATH = Path("data/documents")

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )


def create_vector_store():

    documents = []

    for pdf_file in DOCUMENT_PATH.glob("*.pdf"):

        loader = PyPDFLoader(
            str(pdf_file)
        )

        documents.extend(
            loader.load()
        )

    if not documents:
        raise ValueError(
            "No PDF documents found in data/documents"
        )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(
        documents
    )

    embeddings = get_embeddings()

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    VECTOR_STORE_PATH.mkdir(
        parents=True,
        exist_ok=True
    )

    vector_store.save_local(
        str(VECTOR_STORE_PATH)
    )

    return vector_store


def load_vector_store():

    embeddings = get_embeddings()

    return FAISS.load_local(
        str(VECTOR_STORE_PATH),
        embeddings,
        allow_dangerous_deserialization=True
    )


def search_documents(query: str) -> str:

    vector_store = load_vector_store()

    documents = vector_store.similarity_search(
        query,
        k=4
    )

    if not documents:
        return "No relevant documents found."

    results = []

    for document in documents:

        source = document.metadata.get(
            "source",
            "unknown"
        )

        results.append(
            f"Source: {source}\n"
            f"{document.page_content}"
        )

    return "\n\n".join(results)