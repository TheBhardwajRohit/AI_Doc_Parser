# AI Document Parser - Split Architecture

> **🎯 Quick Start:** Open [START_HERE.md](START_HERE.md) to begin!

## Overview

AI-powered document parser with OCR, skill extraction, and job matching capabilities.

**Architecture:** Split deployment with frontends on Windows and backend on Linux.

## 🚀 Quick Setup

### Windows PC (Frontends)
```cmd
cd windows-client
SETUP.bat
REM Create .env.local files with Linux server IP
START.bat
```

### Linux Server (Backend)
```bash
cd linux-server
./setup.sh
sudo ufw allow 8000/tcp
./start.sh
```

## 📁 Project Structure

```
AI_Doc_Parser/
│
├── 🪟 windows-client/          # Run on Windows PC
│   ├── user-frontend/          # User interface (Port 3000)
│   ├── server-frontend/        # Admin interface (Port 3001)
│   ├── SETUP.bat              # Setup script
│   └── START.bat              # Start script
│
├── 🐧 linux-server/            # Deploy to Linux
│   ├── backend/               # FastAPI backend (Port 8000)
│   ├── setup.sh               # Setup script
│   └── start.sh               # Start script
│
└── 📚 Documentation/
    ├── START_HERE.md          # 👈 Start here!
    ├── QUICK_START.md         # 5-minute setup
    ├── DEPLOYMENT_GUIDE.md    # Detailed guide
    ├── SETUP_CHECKLIST.md     # Step-by-step checklist
    └── More...
```

## 📖 Documentation

| Document | Purpose |
|----------|---------|
| **[START_HERE.md](START_HERE.md)** | 👈 **Begin here!** |
| [QUICK_START.md](QUICK_START.md) | Get running in 5 minutes |
| [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) | Complete setup instructions |
| [SETUP_CHECKLIST.md](SETUP_CHECKLIST.md) | Step-by-step checklist |
| [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) | Architecture overview |
| [MIGRATION_NOTES.md](MIGRATION_NOTES.md) | What changed |
| [WHAT_YOU_HAVE_NOW.md](WHAT_YOU_HAVE_NOW.md) | Summary of new setup |

## 🎨 Architecture

```
┌─────────────────────────────────┐
│      Windows PC (Client)        │
│                                 │
│  ┌─────────────────────────┐   │
│  │  User Frontend :3000    │   │
│  └─────────────────────────┘   │
│                                 │
│  ┌─────────────────────────┐   │
│  │  Server Frontend :3001  │   │
│  └─────────────────────────┘   │
│                                 │
│         │ HTTP API Calls        │
└─────────┼───────────────────────┘
          │
          ▼
┌─────────────────────────────────┐
│    Linux Server (Backend)       │
│                                 │
│  ┌─────────────────────────┐   │
│  │  FastAPI Backend :8000  │   │
│  │  - OCR Processing       │   │
│  │  - AI Analysis          │   │
│  │  - Job Matching         │   │
│  └─────────────────────────┘   │
│                                 │
│  ┌─────────────────────────┐   │
│  │  SQLite Database        │   │
│  │  Document Storage       │   │
│  └─────────────────────────┘   │
└─────────────────────────────────┘
```

## ✨ Features

- 📄 **Document Upload**: PDF, JPG, PNG support
- 🔍 **OCR Processing**: Extract text from images and PDFs
- 🤖 **AI Analysis**: Categorize documents and extract skills
- 💼 **Job Matching**: Find relevant jobs based on skills
- 📊 **Admin Dashboard**: Manage and view all documents
- 🔒 **CORS Enabled**: Secure cross-origin requests

## 🛠️ Tech Stack

### Frontend (Windows)
- Next.js 14
- React 18
- TypeScript
- Tailwind CSS
- Axios

### Backend (Linux)
- FastAPI
- Python 3.8+
- SQLite
- OCR Service
- AI/ML Integration

## 🎯 Access Points

After setup:

- **User Frontend**: http://localhost:3000
- **Server Frontend**: http://localhost:3001
- **Backend API**: http://YOUR_LINUX_IP:8000
- **API Docs**: http://YOUR_LINUX_IP:8000/docs

## 📋 Prerequisites

### Windows PC
- Node.js 18+
- npm

### Linux Server
- Python 3.8+
- pip
- Port 8000 accessible

## 🚦 Getting Started

**New to this project?** Follow these steps:

1. Read [START_HERE.md](START_HERE.md)
2. Follow [QUICK_START.md](QUICK_START.md)
3. Use [SETUP_CHECKLIST.md](SETUP_CHECKLIST.md) to verify
4. Reference [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for details

## 🆘 Troubleshooting

### Can't connect to backend?
- Verify backend is running on Linux
- Check firewall allows port 8000
- Confirm correct IP in `.env.local` files

### Frontend won't start?
- Run `SETUP.bat` first
- Check Node.js version (need 18+)
- Delete `node_modules` and reinstall

### CORS errors?
- Verify `.env.local` files exist
- Check Linux server IP is correct
- Restart frontends after config changes

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for more troubleshooting.

## 📝 Configuration

### Windows Client

Create `.env.local` in both frontend folders:

```env
NEXT_PUBLIC_API_URL=http://192.168.1.100:8000
```

Replace `192.168.1.100` with your Linux server IP.

### Linux Server

No configuration needed! Backend is pre-configured.

## 🔐 Security Notes

- CORS is set to `allow_origins=["*"]` for development
- For production, restrict to specific origins
- Consider adding authentication
- Use HTTPS in production

## 📦 What's Included

### Windows Client
- User-facing document upload interface
- Admin dashboard for document management
- Real-time processing status
- Job recommendations display

### Linux Server
- RESTful API with FastAPI
- OCR text extraction
- AI-powered document analysis
- Skill extraction and categorization
- Job matching algorithm
- SQLite database
- File storage management

## 🎉 Benefits of Split Architecture

- ✅ **Easy Development**: Edit code on Windows with your IDE
- ✅ **Better Performance**: No network latency for frontend
- ✅ **Easier Debugging**: Browser dev tools work normally
- ✅ **Better Security**: Only backend port needs exposure
- ✅ **Clean Separation**: True frontend/backend independence

## 📞 Support

1. Check [START_HERE.md](START_HERE.md)
2. Review [QUICK_START.md](QUICK_START.md)
3. Follow [SETUP_CHECKLIST.md](SETUP_CHECKLIST.md)
4. Read [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

## 📄 License

[Your License Here]

## 👥 Contributors

[Your Name/Team]

---

**Ready to start?** Open [START_HERE.md](START_HERE.md) now!
