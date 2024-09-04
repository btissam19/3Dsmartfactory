from fastapi import UploadFile, File, HTTPException
from app.utility.process import save_file, process_pdf
from app.models.file import files_collection
from pymongo.collection import Collection
from uuid import uuid4
import os

async def upload_and_process(file: UploadFile = File(...)):
    upload_dir = "uploads"
    file_path = save_file(file, upload_dir)
    file_id = str(uuid4())
    
    try:
        # Process the PDF and extract chunks
        chunks = process_pdf(file_path)
        # Create a document with the file_id and chunks
        document = {
            "file_id": file_id,
            "content": chunks
        }
        # Upsert operation to ensure there is only one document in the collection
        result = await files_collection.replace_one(
            {},  # Empty filter means match all documents
            document,
            upsert=True
        )
        
        if result.upserted_id is None and result.modified_count == 0:
            raise HTTPException(status_code=500, detail="Failed to replace the document")
        
        return {"message": "Upload successful", "file_id": file_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

async def get_chunks():
    try:
        # Retrieve the single document from the collection
        document = await files_collection.find_one()  # Ensure this is awaited
        if not document:
            raise HTTPException(status_code=404, detail="No document found")
        chunks = document.get("content", [])
        return {"chunks": chunks}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
