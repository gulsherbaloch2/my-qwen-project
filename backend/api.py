from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys
import os

# Add the parent directory to sys.path so we can import the chat functionality
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import and validate configuration on startup
from secure_config import validate_config
validate_config()

from chat_gemini import query_qdrant, format_response

# Create FastAPI app
app = FastAPI(title="AI Assistant Backend", description="Backend API for Docusaurus AI Assistant")

# Add CORS middleware to allow requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request/response models
class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    response: str

@app.get("/")
def read_root():
    return {"message": "AI Assistant Backend is running!"}

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        query = request.query

        if not query:
            raise HTTPException(status_code=400, detail="Query is required")

        # Query the Qdrant database using the existing function
        search_results = query_qdrant(query)

        # Format the response using the existing function
        response = format_response(query, search_results)

        return ChatResponse(response=response)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)