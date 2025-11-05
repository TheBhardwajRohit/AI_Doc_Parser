# Quick Setup Guide

## Step-by-Step Installation

### 1. Install Python Dependencies

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Gemini API

1. Get your API key from: https://makersuite.google.com/app/apikey
2. Copy `.env.example` to `.env`
3. Edit `.env` and add your key:
   ```
   GEMINI_API_KEY=your_actual_key_here
   ```

### 3. Install Frontend Dependencies

```bash
# User Frontend
cd user-frontend
npm install

# Server Frontend
cd ../server-frontend
npm install
```

## Running the Application

Open **3 separate terminals**:

### Terminal 1 - Backend
```bash
cd backend
venv\Scripts\activate
python main.py
```
✅ Backend running on http://localhost:8000

### Terminal 2 - User Frontend
```bash
cd user-frontend
npm run dev
```
✅ User interface on http://localhost:3000

### Terminal 3 - Server Dashboard
```bash
cd server-frontend
npm run dev
```
✅ Admin dashboard on http://localhost:3001

## Access from Other PCs

1. Find your server IP:
   ```bash
   ipconfig
   ```
   Look for IPv4 Address (e.g., 192.168.1.100)

2. On other PCs (same WiFi), access:
   - User Frontend: `http://192.168.1.100:3000`
   - Server Dashboard: `http://192.168.1.100:3001`

3. Configure frontends to use server IP:
   
   Create `user-frontend/.env.local`:
   ```
   NEXT_PUBLIC_API_URL=http://192.168.1.100:8000
   ```
   
   Create `server-frontend/.env.local`:
   ```
   NEXT_PUBLIC_API_URL=http://192.168.1.100:8000
   ```

4. Allow firewall access for ports 3000, 3001, 8000

## Verification

1. Open http://localhost:8000/health - Should show server status
2. Open http://localhost:3000 - User upload interface
3. Open http://localhost:3001 - Server dashboard

## Common Issues

**EasyOCR Installation Error:**
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
pip install easyocr
```

**Port Already in Use:**
- Change port in package.json: `"dev": "next dev -p 3002"`

**Cannot Connect to Backend:**
- Ensure backend is running
- Check firewall settings
- Verify API URL in .env.local files

## First Time Usage

1. Start all three services
2. Open user frontend (http://localhost:3000)
3. Enter a username
4. Upload a test document (PDF/JPG/PNG)
5. View results with extracted skills and job recommendations
6. Check server dashboard (http://localhost:3001) to see processed documents

---

**Need Help?** Check the main README.md for detailed documentation.
