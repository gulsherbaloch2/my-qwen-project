from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Add the parent directory to sys.path so we can import the existing chat functionality
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import and validate configuration on startup
from secure_config import validate_config
validate_config()

from chat_gemini import query_qdrant, format_response

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/chat', methods=['POST'])
def chat_endpoint():
    try:
        data = request.get_json()
        query = data.get('query', '')

        if not query:
            return jsonify({'error': 'Query is required'}), 400

        # Query the Qdrant database using the existing function
        search_results = query_qdrant(query)

        # Format the response using the existing function
        response = format_response(query, search_results)

        return jsonify({'response': response})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)