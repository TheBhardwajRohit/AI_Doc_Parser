@echo off
echo ========================================
echo Windows Client Setup
echo ========================================
echo.

echo Installing User Frontend dependencies...
cd user-frontend
call npm install
cd ..

echo.
echo Installing Server Frontend dependencies...
cd server-frontend
call npm install
cd ..

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Copy .env.local.example to .env.local in each frontend folder
echo 2. Update the NEXT_PUBLIC_API_URL with your Linux server IP
echo 3. Run START.bat to launch both frontends
echo.
pause
