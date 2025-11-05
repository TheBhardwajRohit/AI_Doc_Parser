# Quick Start Guide

Get up and running in 5 minutes!

## Step 1: Linux Server (Backend)

```bash
# 1. Copy linux-server folder to your Linux machine
# 2. Run setup
cd linux-server
chmod +x setup.sh start.sh
./setup.sh

# 3. Open firewall
sudo ufw allow 8000/tcp

# 4. Start backend
./start.sh

# 5. Get your server IP
hostname -I
# Note this IP address!
```

Backend should now be running on `http://0.0.0.0:8000`

---

## Step 2: Windows PC (Frontends)

```cmd
# 1. Navigate to windows-client folder
cd windows-client

# 2. Run setup (installs dependencies)
SETUP.bat

# 3. Configure API URL
# Create these files:

# windows-client/user-frontend/.env.local
NEXT_PUBLIC_API_URL=http://YOUR_LINUX_IP:8000

# windows-client/server-frontend/.env.local
NEXT_PUBLIC_API_URL=http://YOUR_LINUX_IP:8000

# Replace YOUR_LINUX_IP with the IP from Step 1

# 4. Start frontends
START.bat
```

---

## Step 3: Test It!

1. Open browser: `http://localhost:3000` (User Frontend)
2. Enter a username
3. Upload a test document
4. See results!

---

## Troubleshooting

**Can't connect to backend?**
- Check Linux IP is correct in `.env.local`
- Verify backend is running: `curl http://LINUX_IP:8000/health`
- Check firewall: `sudo ufw status`

**Frontend won't start?**
- Make sure you ran `SETUP.bat` first
- Check if `.env.local` files exist in both frontend folders

---

## What's Next?

- Read [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed setup
- Check [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) for architecture overview
- See individual README files in `windows-client/` and `linux-server/`
