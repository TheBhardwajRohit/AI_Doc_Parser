#!/bin/bash

echo "========================================"
echo "Linux Server Setup"
echo "========================================"
echo ""

echo "Installing Python dependencies..."
cd backend
pip3 install -r requirements.txt

echo ""
echo "========================================"
echo "Setup Complete!"
echo "========================================"
echo ""
echo "Next steps:"
echo "1. Run: ./start.sh"
echo "2. Or manually: cd backend && python3 main.py"
echo "3. Ensure port 8000 is open in firewall"
echo ""
