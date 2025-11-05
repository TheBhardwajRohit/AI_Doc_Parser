# 👋 START HERE

## What Just Happened?

Your project has been reorganized for **split deployment**:

✅ **Frontends** → Run on Windows PC (this machine)  
✅ **Backend** → Deploy to Linux server

This solves your connectivity issues!

---

## 🎯 What You Need to Do

### Step 1: Setup Linux Server (Backend)

1. **Transfer the `linux-server/` folder to your Linux machine**
   - Use WinSCP, FileZilla, or SCP
   - Or use Git to clone the repo

2. **On Linux, run:**
   ```bash
   cd linux-server
   chmod +x setup.sh start.sh
   ./setup.sh
   sudo ufw allow 8000/tcp
   ./start.sh
   ```

3. **Get your Linux server IP:**
   ```bash
   hostname -I
   ```
   Write it down! You'll need it next.

---

### Step 2: Setup Windows PC (Frontends)

1. **Open Command Prompt in this folder**

2. **Navigate to windows-client:**
   ```cmd
   cd windows-client
   ```

3. **Run setup:**
   ```cmd
   SETUP.bat
   ```

4. **Create configuration files:**
   
   Create `windows-client\user-frontend\.env.local`:
   ```
   NEXT_PUBLIC_API_URL=http://YOUR_LINUX_IP:8000
   ```
   
   Create `windows-client\server-frontend\.env.local`:
   ```
   NEXT_PUBLIC_API_URL=http://YOUR_LINUX_IP:8000
   ```
   
   Replace `YOUR_LINUX_IP` with the IP from Step 1.

5. **Start the frontends:**
   ```cmd
   START.bat
   ```

---

### Step 3: Test Everything

1. **Open browser:**
   - User Frontend: http://localhost:3000
   - Server Frontend: http://localhost:3001

2. **Upload a test document** and verify it works!

---

## 📚 Need More Help?

| Read This | When You Need |
|-----------|---------------|
| [QUICK_START.md](QUICK_START.md) | Step-by-step setup guide |
| [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) | Detailed instructions & troubleshooting |
| [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) | Understanding the architecture |
| [MIGRATION_NOTES.md](MIGRATION_NOTES.md) | What changed from old setup |

---

## 🗂️ Folder Guide

```
📁 windows-client/     ← Use this on Windows (this PC)
   ├── SETUP.bat       ← Run first
   └── START.bat       ← Run to start frontends

📁 linux-server/       ← Copy to Linux server
   ├── setup.sh        ← Run first
   └── start.sh        ← Run to start backend

📁 backend/            ← Old folder (can delete after testing)
📁 user-frontend/      ← Old folder (can delete after testing)
📁 server-frontend/    ← Old folder (can delete after testing)
```

---

## ⚡ Quick Commands

### On Linux Server
```bash
cd linux-server
./start.sh              # Start backend
curl http://localhost:8000/health  # Test it
```

### On Windows PC
```cmd
cd windows-client
START.bat               # Start frontends
```

---

## 🎉 That's It!

Your setup is now:
- ✅ Simpler to manage
- ✅ Easier to develop
- ✅ More reliable
- ✅ Better performance

**Ready?** Follow the steps above or open [QUICK_START.md](QUICK_START.md)!
