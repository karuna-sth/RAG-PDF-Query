# RAG PDF Query and Chat System

This project implements a **Retrieval-Augmented Generation (RAG)** system using **LangChain**, **Ollama**, **ChromaDB**, and **FastAPI**. It allows users to upload PDF documents, generate embeddings, and query those documents through an API.

## Features

- **Upload and process PDFs**: Upload PDF files for text extraction and embedding generation.
- **Embeddings with ChromaDB**: Use ChromaDB to store and retrieve document embeddings efficiently.
- **Query**: Query uploaded documents and get responses generated with contextual information.
- **Customizable models**: Easily change the embedding model and LLM through the configuration file.

## Installation

1. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the FastAPI server**:

   ```bash
   uvicorn main_query_chat:app --reload
   ```

3. **Upload PDFs**: Use the `/upload-file` endpoint to upload PDFs and initiate embedding generation.

4. **Query the documents**: Interact with the `/query` endpoint to get responses based on the uploaded PDFs.

## API Endpoints
### Summary Endpoints
- **Upload PDF file**: `POST /upload-file/` - Upload File and create embeddings.

- **Query Document**: `POST /query/` - Query the documents.