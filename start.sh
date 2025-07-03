#!/bin/bash

# Quick start script for the Mergington High School Activities API

echo "🏫 Starting Mergington High School Activities API..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Run ./setup.sh first."
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Check if dependencies are installed
if ! python -c "import fastapi" 2>/dev/null; then
    echo "❌ Dependencies not installed. Run ./setup.sh first."
    exit 1
fi

# Start the server
echo "🚀 Starting development server..."
echo "📍 Server will be available at: http://127.0.0.1:8000"
echo "📚 API documentation: http://127.0.0.1:8000/docs"
echo "📚 Alternative docs: http://127.0.0.1:8000/redoc"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

uvicorn src.app:app --reload --host 0.0.0.0 --port 8000
