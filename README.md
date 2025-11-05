# AI Document Parser

An intelligent document processing system that uses OCR, AI analysis, and job matching to extract insights from academic documents.

## 📋 Overview

AI Document Parser is a full-stack application that processes academic documents (certificates, transcripts, etc.) to extract text, classify document types, identify skills, and recommend relevant job opportunities. The system uses a split architecture with frontends running on Windows and backend services on Linux.

## ✨ Key Features

- **� uMulti-Format Support** - Processes PDF, JPG, and PNG documents
- **🔍 Intelligent OCR** - Hybrid text extraction for both text-based and scanned documents
- **🤖 AI-Powered Analysis** - Google Gemini-inspired document classification and skill extraction
- **💼 Job Matching** - Intelligent recommendation engine matching skills to 20+ job postings
- **📊 Real-time Dashboard** - Live monitoring of system health and document processing
- **🔄 Automatic Fallback** - Rule-based analysis when AI is unavailable
- **⚡ High Performance** - Async processing pipeline for fast document handling

## 🏗️ Architecture

### System Design
```
┌─────────────────────────────────────────────────────────────┐
│                    SPLIT ARCHITECTURE                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────────────┐         ┌──────────────────────┐ │
│  │   Windows PC         │         │   Linux Server       │ │
│  │   (Client-Side)      │◄───────►│   (Server-Side)      │ │
│  │                      │   HTTP  │                      │ │
│  │  - User Frontend     │   API   │  - Backend API       │ │
│  │    Port: 3000        │  (JSON) │    Port: 8000        │ │
│  │                      │         │  - OCR Service       │ │
│  │  - Admin Frontend    │         │  - AI Service        │ │
│  │    Port: 3001        │         │  - Job Matcher       │ │
│  │                      │         │  - Database          │ │
│  │  Technology:         │         │  - File Storage      │ │
│  │  Next.js, React,     │         │                      │ │
│  │  TypeScript          │         │  Technology:         │ │
│  │                      │         │  FastAPI, Python,    │ │
│  └──────────────────────┘         │  EasyOCR, Gemini AI  │ │
│                                   └──────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

### Processing Pipeline
```
Upload → File Validation → OCR Extraction → AI Analysis → Job Matching → Database Storage → Response
```

## 🛠️ Technology Stack

### Backend (Linux Server)
- **Framework:** FastAPI (Python 3.8+)
- **OCR:** EasyOCR, OpenCV
- **PDF Processing:** PyMuPDF (fitz)
- **AI:** Google Gemini API
- **Database:** SQLite
- **Server:** Uvicorn (ASGI)

### Frontend (Windows PC)
- **Framework:** Next.js 14
- **UI Library:** React 18
- **Language:** TypeScript
- **Styling:** Tailwind CSS
- **HTTP Client:** Axios
- **Icons:** Lucide React

## 📁 Project Structure

```
AI_Doc_Parser/
├── windows-client/              # Frontend applications (Windows)
│   ├── user-frontend/           # User interface (Port 3000)
│   │   ├── app/                 # Next.js app directory
│   │   ├── components/          # React components
│   │   ├── .env.local.example   # Environment template
│   │   └── package.json
│   │
│   ├── server-frontend/         # Admin dashboard (Port 3001)
│   │   ├── app/
│   │   ├── components/
│   │   ├── .env.local.example
│   │   └── package.json
│   │
│   ├── SETUP.bat                # Windows setup script
│   └── START.bat                # Windows start script
│
├── linux-server/                # Backend services (Linux)
│   ├── backend/
│   │   ├── main.py              # FastAPI application
│   │   ├── ocr_service.py       # OCR processing
│   │   ├── ai_service.py        # AI analysis
│   │   ├── job_matcher.py       # Job matching
│   │   ├── database.py          # Database operations
│   │   └── requirements.txt     # Python dependencies
│   │
│   ├── setup.sh                 # Linux setup script
│   └── start.sh                 # Linux start script
│
├── PPT_CODE_SNIPPETS.md         # Code snippets for presentation
└── README.md                    # This file
```

## � *Quick Start

### Prerequisites

**Windows PC:**
- Node.js 18+ and npm
- Git (optional)

**Linux Server:**
- Python 3.8+
- pip3
- Port 8000 accessible

### Installation

#### 1. Linux Server Setup

```bash
# Navigate to linux-server directory
cd linux-server

# Make scripts executable
chmod +x setup.sh start.sh

# Install dependencies
./setup.sh

# Open firewall port
sudo ufw allow 8000/tcp

# Start the backend
./start.sh
```

Or manually:
```bash
cd linux-server/backend
pip3 install -r requirements.txt
python3 main.py
```

#### 2. Windows PC Setup

```cmd
# Navigate to windows-client directory
cd windows-client

# Run setup (installs npm dependencies)
SETUP.bat
```

#### 3. Configure API Connection

Create `.env.local` files in both frontend directories:

**windows-client/user-frontend/.env.local**
```env
NEXT_PUBLIC_API_URL=http://YOUR_LINUX_SERVER_IP:8000
```

**windows-client/server-frontend/.env.local**
```env
NEXT_PUBLIC_API_URL=http://YOUR_LINUX_SERVER_IP:8000
```

Replace `YOUR_LINUX_SERVER_IP` with your actual Linux server IP address.

#### 4. Start Frontends

```cmd
# Run start script (opens both frontends)
START.bat
```

Or manually:
```cmd
# Terminal 1 - User Frontend
cd windows-client/user-frontend
npm run dev

# Terminal 2 - Admin Frontend
cd windows-client/server-frontend
npm run dev
```

## 🌐 Access Points

After setup, access the application at:

- **User Frontend:** http://localhost:3000
- **Admin Dashboard:** http://localhost:3001
- **Backend API:** http://YOUR_LINUX_SERVER_IP:8000
- **API Documentation:** http://YOUR_LINUX_SERVER_IP:8000/docs

## 📖 Usage

### Uploading Documents

1. Open User Frontend (http://localhost:3000)
2. Enter your username
3. Drag and drop documents or click to browse
4. Supported formats: PDF, JPG, PNG
5. View results including:
   - Document type classification
   - Extracted skills
   - Job recommendations with match scores
   - Document metadata

### Admin Dashboard

1. Open Admin Dashboard (http://localhost:3001)
2. Monitor system health (Database, OCR, AI services)
3. View all processed documents
4. Check statistics and analytics
5. View/Delete documents
6. Auto-refreshes every 30 seconds

## 🔧 Configuration

### Backend Configuration

**Environment Variables (Optional):**
Create `linux-server/backend/.env`:
```env
GEMINI_API_KEY=your_google_gemini_api_key
```

If no API key is provided, the system uses rule-based fallback analysis.

### Frontend Configuration

Both frontends require `.env.local` files with the backend API URL:
```env
NEXT_PUBLIC_API_URL=http://192.168.1.100:8000
```

## 📊 API Endpoints

### Document Operations
- `POST /upload` - Upload and process documents
- `GET /documents` - List all documents
- `GET /documents/{id}` - Get document details
- `DELETE /documents/{id}` - Delete document

### System Operations
- `GET /` - API information
- `GET /health` - System health check
- `GET /stats` - System statistics

### API Documentation
Interactive API docs available at: `http://YOUR_LINUX_SERVER_IP:8000/docs`

## 🎯 Key Components

### 1. OCR Service
- **Image Processing:** Uses EasyOCR with OpenCV preprocessing
- **PDF Processing:** Hybrid approach - direct text extraction for text-based PDFs, OCR for scanned pages
- **Quality Enhancement:** Image preprocessing (grayscale, thresholding, denoising)

### 2. AI Service
- **Primary:** Google Gemini API for intelligent analysis
- **Fallback:** Rule-based keyword matching
- **Capabilities:**
  - Document type classification (10+ types)
  - Technical skill extraction (50+ skills)
  - Soft skill identification
  - Metadata extraction (institution, duration, grades)

### 3. Job Matcher
- **Database:** 20+ realistic job postings
- **Algorithm:** Fuzzy skill matching with percentage scoring
- **Output:** Top 5 most relevant jobs ranked by match score

### 4. Database
- **Type:** SQLite (serverless, file-based)
- **Schema:** Indexed for fast queries
- **Storage:** Document metadata, OCR text, analysis results, job recommendations

## 🔍 How It Works

### Document Processing Flow

1. **Upload & Validation**
   - User uploads document via frontend
   - Backend validates file type (PDF, JPG, PNG)
   - File saved with timestamp in user-specific directory

2. **OCR Text Extraction**
   - For images: Direct OCR using EasyOCR
   - For PDFs: Attempts text extraction first, falls back to OCR for scanned pages
   - Returns extracted text

3. **AI Analysis**
   - Sends extracted text to Google Gemini AI
   - AI classifies document type
   - Extracts technical and soft skills
   - Identifies metadata (institution, dates, grades)
   - Falls back to rule-based analysis if AI unavailable

4. **Job Matching**
   - Compares extracted skills with job database
   - Calculates match percentage for each job
   - Ranks jobs by relevance
   - Returns top 5 matches

5. **Storage & Response**
   - Saves all results to SQLite database
   - Returns comprehensive response to frontend
   - Frontend displays results with visualizations

## 🎨 Features in Detail

### Hybrid PDF Processing
Intelligently handles both text-based and scanned PDFs:
- Attempts direct text extraction first (fast)
- Falls back to OCR for image-based pages (accurate)
- Maintains high quality with 2x resolution rendering

### AI with Fallback
Ensures 100% uptime:
- Primary: Google Gemini AI for intelligent analysis
- Fallback: Rule-based keyword matching
- Seamless transition between modes

### Real-time Monitoring
Admin dashboard provides:
- Live system health status
- Service availability (Database, OCR, AI)
- Document processing statistics
- Auto-refresh every 30 seconds

### Intelligent Job Matching
Advanced matching algorithm:
- Fuzzy skill comparison (handles variations)
- Percentage-based scoring
- Multi-criteria ranking (score + skill count)
- Relevant job recommendations

## 🔒 Security Considerations

### Current Setup (Development)
- CORS enabled for all origins (`allow_origins=["*"]`)
- No authentication required
- SQLite database (single-user)

### Production Recommendations
1. **Restrict CORS** to specific frontend origins
2. **Add Authentication** (JWT tokens, OAuth)
3. **Use HTTPS** with SSL certificates
4. **Migrate to PostgreSQL** for multi-user support
5. **Implement Rate Limiting** to prevent abuse
6. **Add Input Validation** and sanitization
7. **Use Environment Variables** for sensitive data

## 🚧 Troubleshooting

### Backend Won't Start
```bash
# Check Python version
python3 --version  # Should be 3.8+

# Check if port is in use
sudo netstat -tuln | grep 8000

# Reinstall dependencies
pip3 install -r requirements.txt --force-reinstall
```

### Frontend Can't Connect
1. Verify backend is running: `curl http://LINUX_IP:8000/health`
2. Check `.env.local` files exist in both frontends
3. Verify correct IP address in `.env.local`
4. Restart frontends after changing `.env.local`
5. Check firewall allows port 8000

### CORS Errors
- Ensure backend is running
- Verify `.env.local` has correct URL format: `http://IP:8000`
- Check browser console for exact error
- Restart both frontend and backend

### OCR Not Working
- Ensure EasyOCR is properly installed
- Check if GPU is available (optional, uses CPU by default)
- Verify image/PDF file is not corrupted

## 📈 Performance

### Benchmarks (Approximate)
- **Image OCR:** 2-5 seconds per page
- **PDF Processing:** 3-8 seconds per document
- **AI Analysis:** 1-3 seconds per document
- **Job Matching:** <1 second
- **Total Processing:** 5-15 seconds per document

### Optimization Tips
- Use text-based PDFs when possible (faster)
- Process multiple documents in parallel
- Enable GPU for OCR (if available)
- Cache AI responses for similar documents

## 🔮 Future Enhancements

### Planned Features
- [ ] User authentication and authorization
- [ ] Batch document processing
- [ ] Export results to PDF/Excel
- [ ] Advanced search and filtering
- [ ] Document comparison
- [ ] Skills gap analysis
- [ ] Resume builder integration
- [ ] Email notifications
- [ ] Cloud storage integration (AWS S3, Google Drive)
- [ ] Multi-language support

### Scalability
- [ ] Migrate to PostgreSQL
- [ ] Implement Redis caching
- [ ] Add load balancing
- [ ] Containerize with Docker
- [ ] Deploy on Kubernetes
- [ ] Implement message queue (RabbitMQ/Celery)

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- Your Name - Initial work

## 🙏 Acknowledgments

- **EasyOCR** - OCR engine
- **Google Gemini** - AI analysis
- **FastAPI** - Backend framework
- **Next.js** - Frontend framework
- **PyMuPDF** - PDF processing
- **OpenCV** - Image processing

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact: your.email@example.com

## 📚 Documentation

- **PPT_CODE_SNIPPETS.md** - Code snippets for presentations
- **API Documentation** - Available at `/docs` endpoint
- **Inline Code Comments** - Detailed explanations in source code

---

**Built with ❤️ using FastAPI, Next.js, and AI**
