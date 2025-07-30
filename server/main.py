from fastapi import FastAPI, UploadFile, File, HTTPException
from supabase import create_client, Client
from dotenv import load_dotenv
from pydantic import BaseModel
import os
from ai_parser import extract_skills

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Initialize Supabase client
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

# Pydantic model for parse_resume input
class ParseResumeRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "FastAPI is running"}

@app.get("/auth/test")
def test_auth():
    try:
        response = supabase.auth.get_user()
        return {"message": "Supabase connected successfully"}
    except Exception as e:
        return {"error": str(e)}

@app.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...)):
    try:
        # Validate file type
        allowed_extensions = ['.pdf', '.doc', '.docx', '.png', '.jpg', '.jpeg']
        file_extension = os.path.splitext(file.filename)[1].lower()
        if file_extension not in allowed_extensions:
            raise HTTPException(status_code=400, detail="Invalid file type")

        # Upload to Supabase Storage
        file_content = await file.read()
        file_path = f"resumes/{file.filename}"
        supabase.storage.from_("resumes").upload(file_path, file_content)

        # Parse resume with AI
        skills = extract_skills(file_content.decode('utf-8', errors='ignore'))
        return {"filename": file.filename, "skills": skills}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/parse_resume")
async def parse_resume(request: ParseResumeRequest):
    try:
        skills = extract_skills(request.text)
        return {"skills": skills}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))