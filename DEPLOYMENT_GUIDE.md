# Deployment Guide - Split Architecture

This guide explains how to deploy the AI Document Parser with frontends on Windows and backend on Linux.

## Architecture Overview

```
┌─────────────────────────────────┐
│      Windows PC (Client)        │
│                                 │
│  ┌─────────────────────────┐   │
│  │  User Frontend          │   │
│  │  http://localhost:3000  │   │
│  └─────────────────────────┘   │
│                                 │
│  ┌─────────────────────────┐   │
│  │  Server Frontend        │   │
│  │  http://localhost:3001  │   │
│  └─────────────────────────┘   │
│                                 │
│         │                       │
│         │ API Calls             │
│         ▼                       │
└─────────────────────────────────┘
          │
          │ HTTP
          │
┌─────────▼───────────────────────┐
│    Linux Server (Backend)       │
│                                 │
│  ┌─────────────────────────┐   │
│  │  FastAPI Backend        │   │
│  │  http://0.0.0.0:8000    │   │
│  └─────────────────────────┘   │
│                                 │
│  ┌─────────────────────────┐   │
│  │  Database & Uploads     │   │
│  └─────────────────────────┘   │
└─────────────────────────────────┘
```

## Part 1: Linux Server Setup

### 1. Transfer Backend Files

Transfer the `linux-server/` folder to your Linux machine:

```bash
# Option 1: Using SCP from Windows
scp -r linux-server/ user@linux-server-ip:/home/user/ai-doc-parser/

# Option 2: Using Git
# On Linux server:
git clone <your-repo>
cd <repo>/linux-server
```

### 2. Install Dependencies

```bash
cd linux-server
chmod +x setup.sh start.sh
./setup.sh
```

Or manually:
```bash
cd backend
pip install -r requirements.txt
```

### 3. Configure Firewall

```bash
# UFW (Ubuntu/Debian)
sudo ufw allow 8000/tcp
sudo ufw status

# Firewalld (CentOS/RHEL)
sudo firewall-cmd --permanent --add-port=8000/tcp
sudo firewall-cmd --reload

# Check if port is open
sudo netstat -tuln | grep 8000
```

### 4. Start the Backend

```bash
./start.sh
```

Or manually:
```bash
cd backend
python main.py
```

### 5. Verify Backend is Running

```bash
# From Linux server
curl http://localhost:8000/health

# From Windows PC (replace with your Linux IP)
curl http://192.168.1.100:8000/health
```

You should see a JSON response with status "healthy".

### 6. Get Your Linux Server IP

```bash
# Get IP address
ip addr show
# or
hostname -I
```

Note this IP address - you'll need it for Windows setup.

---

## Part 2: Windows PC Setup

### 1. Navigate to Windows Client Folder

```powershell
cd windows-client
```

### 2. Run Setup

Double-click `SETUP.bat` or run:

```cmd
SETUP.bat
```

This will install npm dependencies for both frontends.

### 3. Configure API Connection

Create `.env.local` files in both frontend folders:

**windows-client/user-frontend/.env.local**
```
NEXT_PUBLIC_API_URL=http://192.168.1.100:8000
```

**windows-client/server-frontend/.env.local**
```
NEXT_PUBLIC_API_URL=http://192.168.1.100:8000
```

Replace `192.168.1.100` with your actual Linux server IP.

### 4. Start the Frontends

Double-click `START.bat` or run:

```cmd
START.bat
```

This will open two command windows:
- User Frontend on http://localhost:3000
- Server Frontend on http://localhost:3001

---

## Testing the Setup

### 1. Check Backend Health

Open browser: `http://<linux-server-ip>:8000/health`

Should show:
```json
{
  "status": "healthy",
  "services": {
    "database": "online",
    "ocr": "online",
    "ai": "online"
  }
}
```

### 2. Access User Frontend

Open browser: `http://localhost:3000`

You should see the document upload interface.

### 3. Access Server Frontend

Open browser: `http://localhost:3001`

You should see the admin/server management interface.

### 4. Test Document Upload

1. Go to User Frontend (localhost:3000)
2. Enter a username
3. Upload a test document (PDF, JPG, or PNG)
4. Check if it processes successfully
5. View results in Server Frontend (localhost:3001)

---

## Troubleshooting

### Backend Issues

**Problem: Can't connect to backend from Windows**

Check:
```bash
# On Linux server
sudo ufw status                    # Firewall open?
netstat -tuln | grep 8000         # Server listening?
curl http://localhost:8000/health # Works locally?
```

**Problem: Backend crashes**

Check logs:
```bash
cd linux-server/backend
python main.py
# Look for error messages
```

### Frontend Issues

**Problem: CORS errors in browser console**

- Ensure backend `main.py` has `allow_origins=["*"]` in CORS middleware
- Check that `.env.local` has correct Linux server IP
- Restart frontends after changing `.env.local`

**Problem: "Failed to fetch" errors**

- Verify backend is running: `curl http://<linux-ip>:8000/health`
- Check `.env.local` has correct IP address
- Ensure no typos in the URL (http://, not https://)

**Problem: Frontend won't start**

```cmd
# Clear cache and reinstall
cd user-frontend
rmdir /s /q node_modules .next
npm install
npm run dev
```

---

## Production Deployment

### Linux Server (Backend)

Use a process manager like systemd or PM2:

**systemd service example:**

```bash
sudo nano /etc/systemd/system/ai-doc-parser.service
```

```ini
[Unit]
Description=AI Document Parser Backend
After=network.target

[Service]
Type=simple
User=your-user
WorkingDirectory=/home/your-user/ai-doc-parser/linux-server/backend
ExecStart=/usr/bin/python3 main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable ai-doc-parser
sudo systemctl start ai-doc-parser
sudo systemctl status ai-doc-parser
```

### Windows Client (Frontends)

For production builds:

```cmd
cd user-frontend
npm run build
npm start

cd ../server-frontend
npm run build
npm start
```

Or use a Windows service wrapper like NSSM to run as background services.

---

## Network Configuration

### Same Network (LAN)

- Use local IP: `http://192.168.1.100:8000`
- Both machines must be on same network
- Firewall must allow connections

### Different Networks (Internet)

- Configure port forwarding on Linux server router
- Use public IP or domain name
- Consider using HTTPS with SSL certificate
- Update CORS settings to specific origins (not "*")

---

## Security Recommendations

1. **Change CORS settings** in production:
   ```python
   allow_origins=["http://your-windows-pc-ip:3000", "http://your-windows-pc-ip:3001"]
   ```

2. **Use HTTPS** for production with SSL certificates

3. **Add authentication** to protect API endpoints

4. **Restrict firewall** to specific IP addresses if possible

5. **Use environment variables** for sensitive configuration

---

## Quick Reference

### Linux Server Commands

```bash
# Start backend
cd linux-server && ./start.sh

# Check status
curl http://localhost:8000/health

# View logs
cd backend && python main.py

# Stop (Ctrl+C in terminal)
```

### Windows Client Commands

```cmd
# Setup (first time only)
SETUP.bat

# Start both frontends
START.bat

# Or start individually
cd user-frontend && npm run dev
cd server-frontend && npm run dev
```

### Ports

- **3000**: User Frontend (Windows)
- **3001**: Server Frontend (Windows)
- **8000**: Backend API (Linux)
