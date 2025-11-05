# Linux Server - Backend API

This folder contains the backend API to run on your Linux server.

## Prerequisites
- Python 3.8+
- pip

## Quick Start

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Run the Backend

```bash
python main.py
```

The server will start on `http://0.0.0.0:8000`

### 3. Verify It's Running

```bash
# Test locally
curl http://localhost:8000/health

# Test from network
curl http://<your-server-ip>:8000/health
```

## Firewall Configuration

Ensure port 8000 is open:

```bash
# UFW
sudo ufw allow 8000/tcp
sudo ufw status

# Firewalld
sudo firewall-cmd --permanent --add-port=8000/tcp
sudo firewall-cmd --reload
```

## API Endpoints

- `GET /` - API info
- `GET /health` - Health check
- `POST /upload` - Upload documents
- `GET /documents` - List all documents
- `GET /documents/{id}` - Get document details
- `DELETE /documents/{id}` - Delete document
- `GET /stats` - Server statistics

## Access

- **API**: http://<your-linux-server-ip>:8000
- **API Docs**: http://<your-linux-server-ip>:8000/docs

## Directory Structure

```
linux-server/
├── backend/
│   ├── main.py           # FastAPI application
│   ├── database.py       # Database operations
│   ├── ocr_service.py    # OCR processing
│   ├── ai_service.py     # AI analysis
│   ├── job_matcher.py    # Job matching logic
│   └── requirements.txt  # Python dependencies
├── uploads/              # Uploaded documents (auto-created)
└── database/             # SQLite database (auto-created)
```
