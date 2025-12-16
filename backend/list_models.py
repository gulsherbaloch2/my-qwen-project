import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google Generative AI with your API key
api_key = os.getenv("GOOGLE_API_KEY", "AIzaSyCkNg--UypDPPX3foc6tPfGSc5Qj46Rf6c")
genai.configure(api_key=api_key)

# List available models
try:
    print("Available models:")
    for model in genai.list_models():
        if 'generateContent' in model.supported_generation_methods:
            print(f"- {model.name}")
except Exception as e:
    print(f"Error listing models: {e}")
    print("The most common model name is usually 'gemini-1.5-pro' or 'gemini-1.0-pro'")