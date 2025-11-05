# AI Document Parser

A comprehensive AI-powered document processing system that extracts text from academic documents using OCR, categorizes them using Gemini AI, extracts skills, and provides relevant job recommendations.

## 🚀 Features

- **Drag & Drop Upload**: Easy-to-use interface for uploading multiple documents
- **OCR Processing**: Extracts text from PDF, JPG, and PNG files using EasyOCR
- **AI Categorization**: Automatically categorizes documents using Google Gemini API
- **Skill Extraction**: Identifies technical and soft skills from certificates
- **Job Matching**: Provides relevant job recommendations based on extracted skills
- **Server Dashboard**: Monitor server health and manage processed documents
- **Multi-user Support**: Organizes documents by username

## 📁 Project Structure

```
AI_Doc_Parser/
├── backend/                    # FastAPI backend server
│   ├── main.py                # Main API endpoints
│   ├── database.py            # SQLite database operations
│   ├── ocr_service.py         # EasyOCR integration
│   ├── ai_service.py          # Gemini AI integration
│   ├── job_matcher.py         # Job recommendation engine
│   ├── requirements.txt       # Python dependencies
│   └── .env.example           # Environment variables template
├── user-frontend/             # Next.js user interface (Port 3000)
│   ├── app/                   # Next.js app directory
│   ├── components/            # React components
│   └── package.json           # Node dependencies
├── server-frontend/           # Next.js admin dashboard (Port 3001)
│   ├── app/                   # Next.js app directory
│   ├── components/            # React components
│   └── package.json           # Node dependencies
└── README.md                  # This file
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8 or higher
- Node.js 18 or higher
- npm or yarn

### 1. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file from example
copy .env.example .env

# Edit .env and add your Gemini API key
# Get your API key from: https://makersuite.google.com/app/apikey
```

**Important**: Edit the `.env` file and add your Gemini API key:
```
GEMINI_API_KEY=your_actual_api_key_here
```

### 2. User Frontend Setup

```bash
# Navigate to user frontend directory
cd user-frontend

# Install dependencies
npm install

# The frontend will connect to backend at http://localhost:8000
```

### 3. Server Frontend Setup

```bash
# Navigate to server frontend directory
cd server-frontend

# Install dependencies
npm install

# The frontend will connect to backend at http://localhost:8000
```

## 🚀 Running the Application

You need to run all three services simultaneously. Open **three separate terminal windows**:

### Terminal 1: Backend Server

```bash
cd backend
# Activate virtual environment if not already active
python main.py
```

The backend will start on `http://localhost:8000`

### Terminal 2: User Frontend

```bash
cd user-frontend
npm run dev
```

The user interface will start on `http://localhost:3000`

### Terminal 3: Server Frontend

```bash
cd server-frontend
npm run dev
```

The admin dashboard will start on `http://localhost:3001`

## 🌐 Accessing from Other PCs on Same WiFi

### Find Your Server IP Address

**On Windows:**
```bash
ipconfig
```
Look for "IPv4 Address" under your active network adapter (e.g., `192.168.1.100`)

**On Linux/Mac:**
```bash
ifconfig
# or
ip addr show
```

### Access the Applications

Once you have your server's IP address (e.g., `192.168.1.100`):

- **User Frontend**: `http://192.168.1.100:3000`
- **Server Dashboard**: `http://192.168.1.100:3001`
- **Backend API**: `http://192.168.1.100:8000`

### Important Notes

1. **Firewall**: Ensure Windows Firewall or your system firewall allows incoming connections on ports 3000, 3001, and 8000
2. **Same Network**: All devices must be connected to the same WiFi network
3. **Backend URL**: You may need to update the API URL in the frontend `.env` files:

Create `user-frontend/.env.local`:
```
NEXT_PUBLIC_API_URL=http://192.168.1.100:8000
```

Create `server-frontend/.env.local`:
```
NEXT_PUBLIC_API_URL=http://192.168.1.100:8000
```

## 📖 Usage Guide

### User Frontend (Port 3000)

1. **Enter Username**: Type your username in the input field
2. **Upload Documents**: Drag and drop or click to select academic documents (PDF, JPG, PNG)
3. **Process**: Click "Upload" to process the documents
4. **View Results**: See extracted information, skills, and job recommendations

### Server Dashboard (Port 3001)

1. **Server Health**: View real-time server status and service health
2. **Statistics**: Monitor total documents, users, and recent activity
3. **Document List**: Browse all processed documents with timestamps
4. **View Details**: Click "View" to see full document analysis
5. **Delete**: Remove documents and their data from the server

## 🔧 Configuration

### Backend Configuration (`.env`)

```env
GEMINI_API_KEY=your_gemini_api_key_here
HOST=0.0.0.0
PORT=8000
DATABASE_PATH=documents.db
MAX_UPLOAD_SIZE=10485760  # 10MB
ALLOWED_EXTENSIONS=pdf,jpg,jpeg,png
```

### Document Categories

The AI can classify documents into:
- Internship Certificate
- Skill Certificate
- Course Completion Certificate
- Academic Transcript
- Degree Certificate
- Participation Certificate
- Achievement Certificate
- Workshop Certificate
- Training Certificate
- Project Certificate

## 🎯 API Endpoints

- `GET /` - API root
- `GET /health` - Server health check
- `POST /upload` - Upload and process documents
- `GET /documents` - List all documents
- `GET /documents/{id}` - Get document details
- `DELETE /documents/{id}` - Delete document
- `GET /stats` - Get server statistics

## 🐛 Troubleshooting

### Backend Issues

**EasyOCR Installation Error:**
```bash
# Install PyTorch first
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
# Then install EasyOCR
pip install easyocr
```

**Gemini API Error:**
- Verify your API key is correct in `.env`
- Check your internet connection
- Ensure you have API quota available

### Frontend Issues

**Port Already in Use:**
```bash
# Change port in package.json
"dev": "next dev -p 3002"  # Use different port
```

**Cannot Connect to Backend:**
- Ensure backend is running on port 8000
- Check firewall settings
- Verify API URL in environment variables

## 📦 Dependencies

### Backend
- FastAPI - Web framework
- EasyOCR - OCR engine
- Google Generative AI - Gemini API
- PyMuPDF - PDF processing
- OpenCV - Image processing
- SQLite - Database

### Frontend
- Next.js 14 - React framework
- TailwindCSS - Styling
- Axios - HTTP client
- Lucide React - Icons
- React Dropzone - File upload

## 🔒 Security Notes

- Never commit `.env` files with real API keys
- Use environment variables for sensitive data
- Implement authentication for production use
- Validate and sanitize all file uploads
- Set appropriate CORS policies for production

## 📝 License

This project is for educational purposes.

## 🤝 Contributing

Feel free to fork, modify, and use this project for your needs.

## 📧 Support

For issues or questions, please check the troubleshooting section or create an issue in the repository.

---

**Built with ❤️ using FastAPI, Next.js, EasyOCR, and Gemini AI**
