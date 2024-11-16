from scripts.chroma_db import get_db
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama

from utils import CONFIG
from scripts.chroma_db import add_to_db
from scripts.pdf_extraction import (
    load_documents,
    split_document
)

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

def load_pdf_create_embedding():
    documents = load_documents()
    chunks = split_document(documents=documents)
    add_to_db(chunks=chunks)


def query_rag(query_text: str):
    db = get_db()
    result = db.similarity_search_with_score(query_text, k=5)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in result])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    
    model = Ollama(model=CONFIG["llm"]["model"])
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("id", None) for doc, _score in result]
    formatted_response = {
        "Response": response_text,
        "Sources": sources
    }
    return formatted_response

if __name__ == "__main__":
    query = "What format of files should the chatbot be able to read?"
    load_pdf_create_embedding()
    print(query_rag(query))
