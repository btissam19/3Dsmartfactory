from fastapi import HTTPException
from app.config.llm import llm
from app.prompts.prompts import extract_resume_info_prompt
from app.models.file import files_collection, extracted_info_collection
from app.utility.formatoutput import format_extracted_information

async def process_resume():
    document = await files_collection.find_one()
    if not document or not document.get("content"):
        raise HTTPException(status_code=404, detail="No content found in the collection.")
    
    content_array = document["content"]
    resume_text = "\n".join(content_array)
    prompt1 = extract_resume_info_prompt.format(resume_text=resume_text)
    
    try:
        output = llm.invoke(prompt1)  # Ensure this is awaited if it's an async call
        extracted_info = format_extracted_information(output)
        
        # Prepare the document to be inserted or updated
        document = {
            "content": extracted_info
        }
        
        # Upsert operation: Update if exists, otherwise insert
        result = await extracted_info_collection.update_one(
            {},  # Empty filter to match any document (or none if collection is empty)
            {"$set": document},
            upsert=True
        )
        
        if result.upserted_id:  # Check if a new document was inserted
            return {"message": "Extracted information successfully inserted.", "extracted_info": extracted_info}
        else:
            return {"message": "Extracted information successfully updated.", "extracted_info": extracted_info}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing resume: {str(e)}")
