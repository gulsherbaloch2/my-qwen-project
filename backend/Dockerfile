FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend files
COPY . .

# Copy docs from the docusaurus site
COPY ../my-docusaurus-site/docs ./docs

# Copy startup script
COPY startup.sh .
RUN chmod +x startup.sh

EXPOSE 8000

# Use startup script to handle ingestion and API server startup
CMD ["./startup.sh"]