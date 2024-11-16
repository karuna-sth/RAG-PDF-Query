from langchain_community.vectorstores import Chroma

from scripts.embedding_generator import get_embedding_function
from utils import CONFIG, calculate_chunk_id


def get_db():
    return Chroma(
        persist_directory=CONFIG["paths"]["chroma_db"], embedding_function=get_embedding_function()
        )

def add_to_db(chunks):
    db = get_db()
    chunks_with_id = calculate_chunk_id(chunks)

    existing_chunks = db.get(include=[])
    existing_chunks_id = set(existing_chunks["ids"])

    new_chunks = [chunk for chunk in chunks_with_id if chunk.metadata["ids"] not in existing_chunks_id]

    if len(new_chunks):
        print("Adding new documents to db")
        new_chunks_id = [chunk.metadata.get("ids") for chunk in new_chunks]
        db.add_documents(new_chunks, id=new_chunks_id)
    else:
        print("No new documnets to add.")
    print("completed.")
