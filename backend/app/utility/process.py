
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from fastapi import  UploadFile, HTTPException
import os
def save_file(file: UploadFile, directory: str) -> str:
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, file.filename)
    try:
        with open(file_path, "wb") as f:
            f.write(file.file.read())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save file: {str(e)}")
    return file_path

# Function to process a PDF file and return chunks of text
def process_pdf(file_path: str):
    try:
        loader = PyPDFLoader(file_path)
        data = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=20)
        text_chunks = text_splitter.split_documents(data)
        chunk_texts = [chunk.page_content for chunk in text_chunks]
        return chunk_texts
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing failed: {str(e)}")

