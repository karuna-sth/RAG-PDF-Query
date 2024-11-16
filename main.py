import os
from fastapi import FastAPI, File, UploadFile, BackgroundTasks

from utils import CONFIG
from scripts.main_query_chat import load_pdf_create_embedding, query_rag

app = FastAPI()

@app.post("/upload-file")
async def uplaod_new_file(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    file_path = os.path.join(CONFIG["paths"]["raw_pdfs"], f'{file.filename}.pdf')
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    background_tasks.add_task(load_pdf_create_embedding)
    return {"message": "File Recieved and embedding started"}


@app.post("/query")
async def query_document(query: str):
    response = query_rag(query)
    return response