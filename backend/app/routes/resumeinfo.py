from fastapi import APIRouter
from app.controllers.resumeinfo import process_resume

router = APIRouter()

@router.get("/process_resume")
async def process_resume_endpoint():
    result = await process_resume()
    return result