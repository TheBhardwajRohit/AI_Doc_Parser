# Project Structure

This project is split into two deployment locations:

## 📁 windows-client/ (Run on Windows PC)
Contains the frontend applications that run on your Windows machine:
- `user-frontend/` - User-facing interface (Port 3000)
- `server-frontend/` - Admin/Server management interface (Port 3001)

Both frontends connect to the Linux server backend via API calls.

## 📁 linux-server/ (Run on Linux Server)
Contains the backend API that runs on your Linux server:
- `backend/` - FastAPI backend service (Port 8000)
- `uploads/` - Document storage
- `database/` - SQLite database

## Setup Instructions

### Windows PC Setup
```bash
cd windows-client/user-frontend
npm install
npm run dev

# In another terminal
cd windows-client/server-frontend
npm install
npm run dev
```

Access:
- User Frontend: http://localhost:3000
- Server Frontend: http://localhost:3001

### Linux Server Setup
```bash
cd linux-server/backend
pip install -r requirements.txt
python main.py
```

Access:
- Backend API: http://<linux-server-ip>:8000

## Configuration

Update the API URL in both frontends to point to your Linux server:

**Windows PC - Set environment variable:**
```bash
# PowerShell
$env:NEXT_PUBLIC_API_URL="http://<your-linux-server-ip>:8000"

# Or create .env.local file in each frontend:
NEXT_PUBLIC_API_URL=http://<your-linux-server-ip>:8000
```

**Linux Server - Ensure backend allows CORS:**
Already configured in `main.py` with `allow_origins=["*"]`
