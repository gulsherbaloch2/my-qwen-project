# Physical AI & Humanoid Robotics Curriculum Assistant

This project combines a Docusaurus documentation site with an AI-powered chatbot that can answer questions about the Physical AI & Humanoid Robotics curriculum.

## Project Architecture

The project consists of three main components:

1. **Docusaurus Documentation Site** (`my-docusaurus-site/`)
   - Static documentation site built with Docusaurus
   - Hosts the curriculum content
   - Features an integrated AI chatbot component

2. **Python AI Backend** (Root directory)
   - RAG (Retrieval Augmented Generation) system using Cohere and Qdrant
   - FastAPI/Flask server providing chat endpoints
   - Processes natural language queries against curriculum content
   - Uses embeddings to find relevant information

3. **Knowledge Base** (`docs/`)
   - Contains markdown files with curriculum content
   - Serves as the source of truth for the AI system

## How It Works

1. **Content Ingestion**: The curriculum content from the `docs/` directory is first processed by the ingestion pipeline (`main.py`) which chunks the text, creates embeddings using Cohere, and stores them in Qdrant vector database.

2. **Query Processing**: When a user asks a question via the chatbot, the query is:
   - Sent to the Python backend
   - Converted to an embedding using Cohere
   - Used to search similar content in the Qdrant database
   - The retrieved content is passed to a language model (either Gemini or Cohere) to generate a response

3. **Frontend Display**: The Docusaurus site provides a user interface where users can access both the static curriculum content and the AI chatbot.

## Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js 18+
- Qdrant Cloud account or local instance
- Cohere API key
- Google API key (for Gemini integration)

### Configuration
1. Copy `.env.example` to `.env` and add your API keys:
   ```
   GOOGLE_API_KEY=your_google_api_key
   COHERE_API_KEY=your_cohere_api_key
   QDRANT_URL=your_qdrant_url
   QDRANT_API_KEY=your_qdrant_api_key
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install Node.js dependencies:
   ```bash
   cd my-docusaurus-site
   npm install
   ```

### Running the System

1. **Ingest the content** (one-time setup):
   ```bash
   python main.py ingest
   ```

2. **Start the Python backend**:
   ```bash
   # Option 1: Using FastAPI
   python run_backend.py
   ```
   Or manually:
   ```bash
   cd ..
   uvicorn api:app --reload
   ```

3. **Start the Docusaurus frontend**:
   ```bash
   cd my-docusaurus-site
   npm run start
   ```

## Available Scripts

- `python main.py ingest` - Ingest curriculum content into the vector database
- `python main.py chat` - Run the command-line chat interface
- `python run_backend.py` - Start the backend API server
- `python test_client.py` - Run the test client to interact with the API
- `npm run start` - Run Docusaurus in development mode (from `my-docusaurus-site` directory)

## File Structure

```
├── api.py              # FastAPI backend
├── backend_api.py      # Flask backend alternative
├── chat.py             # Cohere-based chat interface
├── chat_gemini.py      # Google Gemini-based chat interface
├── main.py             # Main entry point for ingestion and chat
├── config.py           # Configuration file
├── secure_config.py    # Secure configuration with validation
├── check_collection.py # Script to inspect collection info
├── test_client.py      # Simple client to test the API
├── run_backend.py      # Script to run backend with error handling
├── docs/               # Curriculum markdown files
├── my-docusaurus-site/ # Docusaurus documentation site
└── README.md           # This file
```

## Troubleshooting

### Common Issues

1. **"'process' is not defined" error in browser**: This has been fixed by updating the WebChatbot component to properly handle environment variables in browser environments.

2. **Cannot connect to API**: Ensure both the backend server (`http://localhost:8000`) and frontend are running.

3. **Missing environment variables**: Verify all required API keys are set in your `.env` file and that `.env` is in the root directory.

4. **Qdrant connection issues**: Check that your QDRANT_URL and QDRANT_API_KEY are correct in your `.env` file.