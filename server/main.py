from fastapi import FastAPI
from supabase import create_client, Client
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Initialize Supabase client
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

@app.get("/")
def read_root():
    return {"message": "FastAPI is running"}

@app.get("/auth/test")
def test_auth():
    try:
        # Test Supabase connection by fetching users
        response = supabase.auth.get_user()
        return {"message": "Supabase connected successfully"}
    except Exception as e:
        return {"error": str(e)}