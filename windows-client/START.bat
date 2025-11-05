@echo off
echo ========================================
echo Starting Frontend Applications
echo ========================================
echo.
echo User Frontend will start on: http://localhost:3000
echo Server Frontend will start on: http://localhost:3001
echo.
echo Press Ctrl+C in each window to stop
echo.

start "User Frontend" cmd /k "cd user-frontend && npm run dev"
start "Server Frontend" cmd /k "cd server-frontend && npm run dev"

echo.
echo Both frontends are starting in separate windows...
echo.
pause
