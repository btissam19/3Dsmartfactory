from fastapi import HTTPException
from app.config.llm import llm
from app.models.file import extracted_info_collection
from typing import Dict
from app.prompts.prompts import jobs_match_prompt_tamplete ,cover_letter_tamplete ,tips_template

async def compare_resume_to_job_description(job_description: str) -> Dict[str, str]:
    # Retrieve extracted information from MongoDB
    document = await extracted_info_collection.find_one()
    if not document or not document.get("content"):
        raise HTTPException(status_code=404, detail="No extracted information found.")
    
    extracted_info = document.get("content")
    
    # Format resume details for prompt
    resume_details = "\n".join([f"{key}: {value}" for key, value in extracted_info.items()])
    
    # Create the prompt for the LLM
    
    
    comparison_prompt = jobs_match_prompt_tamplete.format(
        job_description=job_description,
        resume_details=resume_details
    )
    
    try:
        # Invoke LLM to perform the comparison
        comparison_output = llm.invoke(comparison_prompt)
        return {"comparison_results": comparison_output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error comparing resume to job description: {str(e)}")

async def genrate_coverletter_resume_to_job_description(job_description: str) -> Dict[str, str]:
    # Retrieve extracted information from MongoDB
    document = await extracted_info_collection.find_one()
    if not document or not document.get("content"):
        raise HTTPException(status_code=404, detail="No extracted information found.")
    
    extracted_info = document.get("content")
    
    # Format resume details for prompt
    resume_details = "\n".join([f"{key}: {value}" for key, value in extracted_info.items()])
    
    # Create the prompt for the LLM
    
    
    cover_prompt = cover_letter_tamplete.format(
        job_description=job_description,
        resume_details=resume_details
    )
    
    try:
        # Invoke LLM to perform the comparison
        cover_letter = llm.invoke(cover_prompt )
        return {"cover letter": cover_letter }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error cover letter not genrated: {str(e)}")

async def genrate_tips_resume_to_job_description(job_description: str) -> Dict[str, str]:
    # Retrieve extracted information from MongoDB
    document = await extracted_info_collection.find_one()
    if not document or not document.get("content"):
        raise HTTPException(status_code=404, detail="No extracted information found.")
    
    extracted_info = document.get("content")
    
    # Format resume details for prompt
    resume_details = "\n".join([f"{key}: {value}" for key, value in extracted_info.items()])
    
    # Create the prompt for the LLM
    
    
    tips_prompt = tips_template.format(
        job_description=job_description,
        resume_details=resume_details
    )
    
    try:
        # Invoke LLM to perform the comparison
        tips= llm.invoke(tips_prompt)
        return {"tips": tips }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error tips not genrated: {str(e)}")
