from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.controllers.generatequetions import generate_interview_questions ,generate_answers ,generate_advices

router = APIRouter()

class QuestionsRequest(BaseModel):
    questions: List[str]

@router.get("/generate_interview_questions")
async def process_resume_endpoint():
    return await generate_interview_questions()

@router.post("/generate_answers")
async def generate_answers_endpoint(request: QuestionsRequest):
    questions = request.questions
    if not questions:
        raise HTTPException(status_code=400, detail="No questions provided.")
    return await generate_answers(questions)


@router.get("/generate_advices")
async def process_resume_endpoint():
    return await generate_advices()
