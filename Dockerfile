# Use a slim Python image for efficiency
FROM python:3.11-slim

# Install system dependencies for audio and document processing
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libmagic1 \
    libreoffice \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --no-cache-dir \
    flask \
    pandas \
    watchdog \
    litellm \
    "markitdown[all]" \
    requests \
    pydantic \
    openai \
    easyocr \
    transformers \
    huggingface_hub

RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

# Copy application files
COPY . .

# Expose the Flask port
EXPOSE 1688

# Start the Flask server, which will spawn the background agent
CMD ["python", "app.py"]
