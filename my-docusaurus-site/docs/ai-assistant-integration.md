---
title: AI Assistant Integration
sidebar_position: 99
---

# AI Assistant Integration

This documentation explains how to set up and use the AI assistant integrated into this Docusaurus site.

## Overview

The AI assistant is seamlessly integrated into this documentation site. You can access it using the chat icon 💬 at the bottom right of any page.

## Getting Started

### 1. Backend Setup

To use the full functionality of the AI assistant, you need to run the backend service:

1. Navigate to your project root directory:
   ```bash
   cd C:\Users\LENOVO\my-qwen-project
   ```

2. Create a `.env` file in the project root with your API keys:
   ```env
   GOOGLE_API_KEY=your_actual_google_api_key_here
   COHERE_API_KEY=your_actual_cohere_api_key_here
   QDRANT_URL=your_actual_qdrant_url_here
   QDRANT_API_KEY=your_actual_qdrant_api_key_here
   ```

3. Start the FastAPI backend:
   ```bash
   uvicorn api:app --reload
   ```

### 2. Frontend Setup

The Docusaurus frontend is already configured to connect to the backend. The chatbot component is embedded site-wide.

If you need to build the frontend for production, run:
```bash
cd my-docusaurus-site
npm run build
```

## Architecture

- **Frontend**: Docusaurus site with React-based chatbot component
- **Backend**: FastAPI server that processes queries using Google Gemini and Qdrant vector database
- **Data**: Book content stored in Qdrant for retrieval-augmented generation (RAG)

## Troubleshooting

**Chatbot not responding**: Make sure the backend service is running on `http://localhost:8000`.

**API errors**: Verify that your `.env` file contains valid API keys.

**CORS issues**: The backend is configured to allow requests from any origin for development. In production, adjust the CORS settings appropriately.

## Customization

To customize the chatbot interface, edit the components in `src/components/Chatbot/`.

To modify backend behavior, edit the API endpoints in `api.py` in the project root.