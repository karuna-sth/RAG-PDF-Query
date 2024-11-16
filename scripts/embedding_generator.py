from langchain_community.embeddings.ollama import OllamaEmbeddings

from utils import CONFIG

def get_embedding_function():
    embeddings = OllamaEmbeddings(model=CONFIG["embedding"])
    return embeddings


