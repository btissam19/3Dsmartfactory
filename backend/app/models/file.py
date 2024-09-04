from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# MongoDB connection
client = AsyncIOMotorClient("mongodb+srv://btissamchaibi1912:csFmdD0B8nVO0tfg@cluster0.flf6j.mongodb.net/smartfactory?retryWrites=true&w=majority&appName=Cluster0")
db = client["smartfactory"]  # Make sure the database name matches the one you want to use
files_collection = db["files"]
extracted_info_collection = db["extracted_info"]
generated_question_collection=db["generated_questions"]

class TextChunk(BaseModel):
    file_id: str
    chunk_id: str
    content: str

