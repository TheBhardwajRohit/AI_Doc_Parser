# Setup Checklist

Use this checklist to ensure everything is configured correctly.

## 📋 Linux Server Checklist

### Prerequisites
- [ ] Python 3.8+ installed
- [ ] pip installed
- [ ] SSH access to server

### Setup Steps
- [ ] Transferred `linux-server/` folder to Linux machine
- [ ] Navigated to `linux-server/` directory
- [ ] Made scripts executable: `chmod +x setup.sh start.sh`
- [ ] Ran `./setup.sh` successfully
- [ ] No errors during pip install

### Firewall Configuration
- [ ] Opened port 8000: `sudo ufw allow 8000/tcp`
- [ ] Verified firewall status: `sudo ufw status`
- [ ] Port 8000 shows as ALLOW

### Start Backend
- [ ] Ran `./start.sh` or `cd backend && python main.py`
- [ ] Server started without errors
- [ ] Saw message: "✅ Server started successfully"

### Verification
- [ ] Local test works: `curl http://localhost:8000/health`
- [ ] Returns JSON with `"status": "healthy"`
- [ ] Got server IP: `hostname -I`
- [ ] Wrote down IP: ________________

### Network Test
- [ ] From Windows, can ping Linux server: `ping YOUR_LINUX_IP`
- [ ] From Windows, can access API: `curl http://YOUR_LINUX_IP:8000/health`
- [ ] Or in browser: `http://YOUR_LINUX_IP:8000/health`

---

## 🪟 Windows PC Checklist

### Prerequisites
- [ ] Node.js 18+ installed
- [ ] npm installed
- [ ] Have Linux server IP address

### Setup Steps
- [ ] Navigated to `windows-client/` directory
- [ ] Ran `SETUP.bat`
- [ ] Both frontends installed dependencies successfully
- [ ] No errors during npm install

### Configuration
- [ ] Created `windows-client\user-frontend\.env.local`
- [ ] File contains: `NEXT_PUBLIC_API_URL=http://YOUR_LINUX_IP:8000`
- [ ] Created `windows-client\server-frontend\.env.local`
- [ ] File contains: `NEXT_PUBLIC_API_URL=http://YOUR_LINUX_IP:8000`
- [ ] Replaced YOUR_LINUX_IP with actual IP
- [ ] Files are `.env.local` not `.env.local.txt`

### Verify Configuration
- [ ] Checked file exists: `dir windows-client\user-frontend\.env.local`
- [ ] Checked file exists: `dir windows-client\server-frontend\.env.local`
- [ ] Viewed contents: `type windows-client\user-frontend\.env.local`
- [ ] URL starts with `http://` not `https://`
- [ ] URL ends with `:8000`

### Start Frontends
- [ ] Ran `START.bat`
- [ ] Two command windows opened
- [ ] User Frontend window shows "Ready" on port 3000
- [ ] Server Frontend window shows "Ready" on port 3001
- [ ] No errors in either window

### Browser Access
- [ ] Opened http://localhost:3000 in browser
- [ ] User Frontend loads successfully
- [ ] Opened http://localhost:3001 in browser
- [ ] Server Frontend loads successfully
- [ ] No CORS errors in browser console (F12)

---

## 🧪 Testing Checklist

### Backend Health Check
- [ ] Opened: `http://YOUR_LINUX_IP:8000/health`
- [ ] Shows status: "healthy"
- [ ] All services show: "online"

### API Documentation
- [ ] Opened: `http://YOUR_LINUX_IP:8000/docs`
- [ ] FastAPI Swagger UI loads
- [ ] Can see all endpoints

### User Frontend Test
- [ ] Opened: http://localhost:3000
- [ ] Entered a test username
- [ ] Selected a test file (PDF, JPG, or PNG)
- [ ] Clicked upload
- [ ] File uploaded successfully
- [ ] Saw processing status
- [ ] Received results with skills/jobs

### Server Frontend Test
- [ ] Opened: http://localhost:3001
- [ ] Can see list of documents
- [ ] Can see the test document uploaded
- [ ] Can view document details
- [ ] Can see statistics

### End-to-End Test
- [ ] Upload document from User Frontend
- [ ] Document appears in Server Frontend
- [ ] Document shows correct information
- [ ] Can delete document from Server Frontend
- [ ] Document removed successfully

---

## ❌ Troubleshooting Checklist

### If Backend Won't Start
- [ ] Check Python version: `python --version` (need 3.8+)
- [ ] Check if port 8000 is already in use: `netstat -tuln | grep 8000`
- [ ] Check for error messages in terminal
- [ ] Try installing dependencies again: `pip install -r requirements.txt`

### If Can't Connect from Windows
- [ ] Verify backend is running on Linux
- [ ] Verify firewall allows port 8000: `sudo ufw status`
- [ ] Verify correct IP address: `hostname -I`
- [ ] Try ping from Windows: `ping YOUR_LINUX_IP`
- [ ] Try curl from Windows: `curl http://YOUR_LINUX_IP:8000/health`

### If Frontend Won't Start
- [ ] Check Node.js version: `node --version` (need 18+)
- [ ] Check if port is in use: `netstat -ano | findstr :3000`
- [ ] Delete node_modules and reinstall: `rmdir /s /q node_modules && npm install`
- [ ] Clear Next.js cache: `rmdir /s /q .next`

### If CORS Errors
- [ ] Verify `.env.local` files exist
- [ ] Verify `.env.local` has correct IP
- [ ] Verify URL starts with `http://`
- [ ] Restart frontends after changing `.env.local`
- [ ] Check backend CORS settings in `main.py`

### If Upload Fails
- [ ] Check backend logs for errors
- [ ] Verify file type is PDF, JPG, or PNG
- [ ] Check file size (not too large)
- [ ] Verify backend has write permissions for uploads folder
- [ ] Check disk space on Linux server

---

## ✅ Success Criteria

You're all set when:

- ✅ Backend running on Linux without errors
- ✅ Both frontends running on Windows without errors
- ✅ Can access User Frontend at localhost:3000
- ✅ Can access Server Frontend at localhost:3001
- ✅ Can upload a document successfully
- ✅ Document appears in Server Frontend
- ✅ No errors in browser console
- ✅ No errors in terminal windows

---

## 📞 Still Having Issues?

1. Review [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) troubleshooting section
2. Check all items in this checklist again
3. Verify network connectivity between Windows and Linux
4. Check firewall settings on both machines
5. Review error messages carefully

---

## 🎉 All Done?

Congratulations! Your AI Document Parser is now running in split architecture mode.

Next steps:
- [ ] Test with real documents
- [ ] Configure for production (see DEPLOYMENT_GUIDE.md)
- [ ] Set up HTTPS (optional)
- [ ] Add authentication (optional)
- [ ] Configure backups
