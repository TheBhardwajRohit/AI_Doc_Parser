# AI Document Parser - Split Architecture Setup

## 🎯 Overview

Your project is now organized for **split deployment**:
- **Frontends** run on your Windows PC
- **Backend** runs on your Linux server

## 📁 Folder Structure

```
AI_Doc_Parser/
│
├── 🪟 windows-client/          ← Use this on Windows PC
│   ├── user-frontend/          (Port 3000)
│   ├── server-frontend/        (Port 3001)
│   ├── SETUP.bat              ← Run this first
│   ├── START.bat              ← Run this to start
│   └── README.md
│
├── 🐧 linux-server/            ← Deploy this to Linux
│   ├── backend/               (Port 8000)
│   ├── setup.sh               ← Run this first
│   ├── start.sh               ← Run this to start
│   └── README.md
│
└── 📚 Documentation
    ├── QUICK_START.md         ← Start here!
    ├── DEPLOYMENT_GUIDE.md    ← Detailed instructions
    ├── PROJECT_STRUCTURE.md   ← Architecture info
    └── MIGRATION_NOTES.md     ← What changed
```

## 🚀 Quick Start

### Linux Server (5 minutes)

```bash
cd linux-server
./setup.sh              # Install dependencies
sudo ufw allow 8000/tcp # Open firewall
./start.sh              # Start backend
hostname -I             # Get your IP
```

### Windows PC (5 minutes)

```cmd
cd windows-client
SETUP.bat               # Install dependencies

# Create .env.local in both frontend folders:
# NEXT_PUBLIC_API_URL=http://YOUR_LINUX_IP:8000

START.bat               # Start both frontends
```

### Test

- User Frontend: http://localhost:3000
- Server Frontend: http://localhost:3001
- Backend API: http://YOUR_LINUX_IP:8000

## 📖 Documentation

| Document | Purpose |
|----------|---------|
| [QUICK_START.md](QUICK_START.md) | Get running in 5 minutes |
| [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) | Complete setup instructions |
| [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) | Architecture overview |
| [MIGRATION_NOTES.md](MIGRATION_NOTES.md) | What changed from old setup |

## 🔧 Configuration

### Windows Client

Create `.env.local` files:

**windows-client/user-frontend/.env.local**
```env
NEXT_PUBLIC_API_URL=http://192.168.1.100:8000
```

**windows-client/server-frontend/.env.local**
```env
NEXT_PUBLIC_API_URL=http://192.168.1.100:8000
```

Replace `192.168.1.100` with your Linux server IP.

### Linux Server

No configuration needed! Backend is already set up correctly.

## 🎨 Architecture

```
┌─────────────────┐
│   Windows PC    │
│                 │
│  Frontend:3000  │──┐
│  Frontend:3001  │  │
└─────────────────┘  │
                     │ HTTP API Calls
                     │
                     ▼
              ┌─────────────────┐
              │  Linux Server   │
              │                 │
              │  Backend:8000   │
              │  Database       │
              │  File Storage   │
              └─────────────────┘
```

## ✅ Advantages

- ✨ **Easy Development**: Edit code on Windows with your IDE
- 🚀 **Better Performance**: No network latency for frontend
- 🐛 **Easier Debugging**: Browser dev tools work normally
- 🔒 **Better Security**: Only backend port needs to be exposed
- 📦 **Clean Separation**: Frontend and backend truly independent

## 🆘 Troubleshooting

### Can't connect to backend?

```bash
# On Linux server
curl http://localhost:8000/health  # Should return JSON
sudo ufw status                    # Port 8000 allowed?
netstat -tuln | grep 8000         # Server listening?
```

### Frontend errors?

```cmd
# Check .env.local exists and has correct IP
type windows-client\user-frontend\.env.local
type windows-client\server-frontend\.env.local

# Restart frontends after changing .env.local
```

### CORS errors?

- Backend already configured with `allow_origins=["*"]`
- Make sure backend is actually running
- Check browser console for exact error

## 📞 Support

1. Read [QUICK_START.md](QUICK_START.md)
2. Check [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
3. Review [MIGRATION_NOTES.md](MIGRATION_NOTES.md)

## 🎯 Next Steps

1. ✅ Follow [QUICK_START.md](QUICK_START.md)
2. ✅ Test document upload
3. ✅ Read [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for production setup
4. ✅ Configure authentication (optional)
5. ✅ Set up HTTPS (optional)

---

**Ready to start?** Open [QUICK_START.md](QUICK_START.md) and follow the steps!
