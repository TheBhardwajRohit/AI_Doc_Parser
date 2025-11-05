# Configuration Example

## Step-by-Step: Creating .env.local Files

### Example Scenario

Your Linux server IP is: `192.168.1.50`

### File 1: user-frontend/.env.local

**Location:** `windows-client\user-frontend\.env.local`

**Content:**
```
NEXT_PUBLIC_API_URL=http://192.168.1.50:8000
```

**How to create:**

1. Open Notepad
2. Type the line above (replace with YOUR Linux IP)
3. Save as: `windows-client\user-frontend\.env.local`
4. Make sure it's `.env.local` not `.env.local.txt`

---

### File 2: server-frontend/.env.local

**Location:** `windows-client\server-frontend\.env.local`

**Content:**
```
NEXT_PUBLIC_API_URL=http://192.168.1.50:8000
```

**How to create:**

1. Open Notepad
2. Type the line above (replace with YOUR Linux IP)
3. Save as: `windows-client\server-frontend\.env.local`
4. Make sure it's `.env.local` not `.env.local.txt`

---

## Quick Copy Method

You can also copy the example files:

```cmd
cd windows-client\user-frontend
copy .env.local.example .env.local
notepad .env.local
REM Edit the IP address and save

cd ..\server-frontend
copy .env.local.example .env.local
notepad .env.local
REM Edit the IP address and save
```

---

## Verify Configuration

```cmd
REM Check if files exist
dir windows-client\user-frontend\.env.local
dir windows-client\server-frontend\.env.local

REM View contents
type windows-client\user-frontend\.env.local
type windows-client\server-frontend\.env.local
```

Both should show:
```
NEXT_PUBLIC_API_URL=http://YOUR_LINUX_IP:8000
```

---

## Common Mistakes

❌ **Wrong:** `NEXT_PUBLIC_API_URL=192.168.1.50:8000`  
✅ **Correct:** `NEXT_PUBLIC_API_URL=http://192.168.1.50:8000`

❌ **Wrong:** File named `.env.local.txt`  
✅ **Correct:** File named `.env.local`

❌ **Wrong:** `NEXT_PUBLIC_API_URL=http://localhost:8000`  
✅ **Correct:** `NEXT_PUBLIC_API_URL=http://192.168.1.50:8000`

---

## After Configuration

1. Save both files
2. Run `START.bat`
3. Open http://localhost:3000
4. Test document upload

If you see CORS errors or "Failed to fetch", double-check:
- Linux backend is running
- IP address is correct
- No typos in the URL
- You restarted the frontends after creating .env.local
