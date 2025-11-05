#!/bin/bash

echo "========================================"
echo "Starting Backend API Server"
echo "========================================"
echo ""
echo "Server will start on: http://0.0.0.0:8000"
echo "API Docs available at: http://0.0.0.0:8000/docs"
echo ""
echo "Press Ctrl+C to stop"
echo ""

cd backend
python3 main.py
