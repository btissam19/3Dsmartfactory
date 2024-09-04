from fastapi import APIRouter, UploadFile, File
from app.controllers.processfiles import upload_and_process ,get_chunks
from app.models.file import files_collection

router = APIRouter()

@router.post("/upload_and_process/")
async def upload_and_process_route(file: UploadFile = File(...)):
    return await upload_and_process(file)



@router.get("/get_chunks")
async def get_chunks_endpoint():
    result = await get_chunks(files_collection)  # Make sure to await this function
    return result