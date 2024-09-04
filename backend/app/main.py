from fastapi import FastAPI
from app.routes.uploadfiles import router as resume_upload
from app.routes.resumeinfo import router as resume_info
from app.routes.generatequestions import router as questions
from app.routes.jobmatch import router as jobmatch

app = FastAPI()

app.include_router(resume_upload)
app.include_router(resume_info)
app.include_router(questions)
app.include_router(jobmatch)
