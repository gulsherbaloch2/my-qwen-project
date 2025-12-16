"""
Vercel-compatible entry point for the AI Assistant Backend.
This file wraps the FastAPI application to work with Vercel's serverless functions.
"""

import os
import sys
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

# Add the current directory to sys.path so we can import other modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Validate configuration on startup
from secure_config import validate_config
validate_config()

# Import the core functionality
from chat_gemini import query_qdrant, format_response


# Create Flask app
app = Flask(__name__)

# Add CORS support
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "AI Assistant Backend is running!"})

@app.route('/api/chat', methods=['POST'])
def chat_endpoint():
    try:
        json_data = request.get_json()
        
        if not json_data or 'query' not in json_data:
            return jsonify({"error": "Query is required"}), 400

        query = json_data['query']

        if not query.strip():
            return jsonify({"error": "Query cannot be empty"}), 400

        # Query the Qdrant database using the existing function
        search_results = query_qdrant(query)

        # Format the response using the existing function
        response = format_response(query, search_results)

        return jsonify({"response": response})

    except HTTPException as e:
        return jsonify({"error": str(e.description)}), e.code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# For Vercel
if __name__ == "__main__":
    app.run(debug=True)