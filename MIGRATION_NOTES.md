# Migration Notes

## What Changed?

Your project has been reorganized into a split architecture:

### Old Structure
```
AI_Doc_Parser/
├── backend/           # Backend API
├── user-frontend/     # User interface
└── server-frontend/   # Admin interface
```

### New Structure
```
AI_Doc_Parser/
├── windows-client/              # 👈 Run on Windows PC
│   ├── user-frontend/
│   ├── server-frontend/
│   ├── SETUP.bat
│   └── START.bat
│
├── linux-server/                # 👈 Deploy to Linux server
│   ├── backend/
│   ├── setup.sh
│   └── start.sh
│
└── [old folders still exist]
```

## What to Do Now?

### On Your Windows PC (Current Machine)

1. **Use the new `windows-client/` folder**
   ```cmd
   cd windows-client
   SETUP.bat
   # Configure .env.local files
   START.bat
   ```

2. **Old folders can be kept as backup** or deleted after confirming everything works:
   - `user-frontend/` (old)
   - `server-frontend/` (old)
   - `backend/` (old - but keep until Linux setup is done)

### On Your Linux Server

1. **Transfer only the `linux-server/` folder**
   ```bash
   # From Windows, use SCP or WinSCP
   scp -r linux-server/ user@linux-ip:/path/to/destination/
   ```

2. **Or use Git** to clone the repo and use only `linux-server/`

## Key Differences

### Frontend Configuration

**Old way:**
- Frontends tried to bind to `0.0.0.0` (for network access)
- Ran on Linux server
- Had issues with accessibility

**New way:**
- Frontends run on Windows (localhost only)
- Connect to Linux backend via API
- Much simpler and more reliable

### Backend Configuration

**No changes needed!**
- Backend still runs on Linux
- Still binds to `0.0.0.0:8000`
- CORS already configured correctly

## Benefits of New Architecture

1. **Easier Development**: Edit frontend code on Windows with your IDE
2. **Better Performance**: Frontend runs locally, no network latency
3. **Simpler Debugging**: Browser dev tools work normally
4. **Clearer Separation**: Frontend and backend are truly independent
5. **No Port Forwarding Needed**: Only backend port (8000) needs to be accessible

## Cleanup (Optional)

After confirming everything works, you can clean up:

```cmd
# On Windows (be careful!)
rmdir /s /q user-frontend
rmdir /s /q server-frontend
rmdir /s /q backend
```

**But keep them as backup until you're 100% sure the new setup works!**

## Rollback

If you need to go back to the old setup:

1. The old folders are still there
2. Just use them as before
3. The new `windows-client/` and `linux-server/` folders don't interfere

## Questions?

- Check [QUICK_START.md](QUICK_START.md) for setup steps
- Read [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed instructions
- See [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) for architecture overview
