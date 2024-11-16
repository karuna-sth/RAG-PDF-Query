from langchain.schema.document import Document
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from utils import CONFIG


def load_documents() -> list[Document]:
    raw_pdf_path = CONFIG["paths"]["raw_pdfs"]
    document_loader = PyPDFDirectoryLoader(raw_pdf_path)
    return document_loader.load()

def split_document(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False
    )
    return text_splitter.split_documents(documents=documents)


if __name__ == "__main__":
    documents = load_documents()
    chunks = split_document(documents=documents)
    print(chunks[0])