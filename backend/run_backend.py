#!/usr/bin/env python3
"""
Script to run the FastAPI backend with proper error handling
"""

import os
import subprocess
import sys
from secure_config import validate_config

def main():
    """
    Main function to run the backend API
    """
    print("Starting AI Assistant Backend...")

    # Validate configuration before starting the server
    try:
        validate_config()
        print("Configuration validated successfully")
    except ValueError as e:
        print(f"Configuration error: {e}")
        print("Please make sure all required environment variables are set in your .env file")
        print("Required variables: GOOGLE_API_KEY, COHERE_API_KEY, QDRANT_URL, QDRANT_API_KEY")
        sys.exit(1)

    # Display API endpoints info
    print("\nAPI Endpoints:")
    print("   GET  /           - Health check")
    print("   POST /chat       - Chat endpoint")
    print("\nExample request to /chat endpoint:")
    print('   curl -X POST "http://localhost:8000/chat" -H "Content-Type: application/json" -d \'{"query": "Your question here"}\'')
    print()

    # Run the FastAPI application
    try:
        # Using uvicorn to run the app
        subprocess.run([sys.executable, "-m", "uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"])
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    except Exception as e:
        print(f"Error running server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()