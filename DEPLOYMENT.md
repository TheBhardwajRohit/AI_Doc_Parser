# Deployment Guide for Linux Server

This guide explains how to deploy the AI Document Parser on a Linux server.

## Prerequisites

- Linux server (Ubuntu 20.04+ recommended)
- Python 3.8+
- Node.js 18+
- Nginx (optional, for production)
- Domain name or static IP (optional)

## 1. Server Preparation

### Update System
```bash
sudo apt update
sudo apt upgrade -y
```

### Install Python and Dependencies
```bash
sudo apt install python3 python3-pip python3-venv -y
```

### Install Node.js
```bash
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install nodejs -y
```

## 2. Upload Project to Server

### Option A: Using Git
```bash
cd /home/your-user/
git clone <your-repository-url>
cd AI_Doc_Parser
```

### Option B: Using SCP/SFTP
```bash
# From your local machine
scp -r AI_Doc_Parser user@server-ip:/home/user/
```

## 3. Backend Setup

```bash
cd /home/your-user/AI_Doc_Parser/backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
nano .env  # Add your Gemini API key
```

## 4. Frontend Setup

### User Frontend
```bash
cd /home/your-user/AI_Doc_Parser/user-frontend
npm install
npm run build
```

### Server Frontend
```bash
cd /home/your-user/AI_Doc_Parser/server-frontend
npm install
npm run build
```

## 5. Running with systemd (Production)

### Backend Service

Create `/etc/systemd/system/ai-doc-parser-backend.service`:

```ini
[Unit]
Description=AI Document Parser Backend
After=network.target

[Service]
Type=simple
User=your-user
WorkingDirectory=/home/your-user/AI_Doc_Parser/backend
Environment="PATH=/home/your-user/AI_Doc_Parser/backend/venv/bin"
ExecStart=/home/your-user/AI_Doc_Parser/backend/venv/bin/python main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

### User Frontend Service

Create `/etc/systemd/system/ai-doc-parser-user-frontend.service`:

```ini
[Unit]
Description=AI Document Parser User Frontend
After=network.target

[Service]
Type=simple
User=your-user
WorkingDirectory=/home/your-user/AI_Doc_Parser/user-frontend
Environment="NODE_ENV=production"
Environment="NEXT_PUBLIC_API_URL=http://localhost:8000"
ExecStart=/usr/bin/npm start
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

### Server Frontend Service

Create `/etc/systemd/system/ai-doc-parser-server-frontend.service`:

```ini
[Unit]
Description=AI Document Parser Server Frontend
After=network.target

[Service]
Type=simple
User=your-user
WorkingDirectory=/home/your-user/AI_Doc_Parser/server-frontend
Environment="NODE_ENV=production"
Environment="NEXT_PUBLIC_API_URL=http://localhost:8000"
ExecStart=/usr/bin/npm start
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

### Enable and Start Services

```bash
sudo systemctl daemon-reload
sudo systemctl enable ai-doc-parser-backend
sudo systemctl enable ai-doc-parser-user-frontend
sudo systemctl enable ai-doc-parser-server-frontend

sudo systemctl start ai-doc-parser-backend
sudo systemctl start ai-doc-parser-user-frontend
sudo systemctl start ai-doc-parser-server-frontend

# Check status
sudo systemctl status ai-doc-parser-backend
sudo systemctl status ai-doc-parser-user-frontend
sudo systemctl status ai-doc-parser-server-frontend
```

## 6. Firewall Configuration

```bash
# Allow necessary ports
sudo ufw allow 8000/tcp   # Backend
sudo ufw allow 3000/tcp   # User Frontend
sudo ufw allow 3001/tcp   # Server Frontend
sudo ufw enable
```

## 7. Nginx Reverse Proxy (Optional)

Install Nginx:
```bash
sudo apt install nginx -y
```

Create `/etc/nginx/sites-available/ai-doc-parser`:

```nginx
server {
    listen 80;
    server_name your-domain.com;

    # User Frontend
    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }

    # Server Frontend
    location /admin {
        proxy_pass http://localhost:3001;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }

    # Backend API
    location /api {
        proxy_pass http://localhost:8000;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Enable the site:
```bash
sudo ln -s /etc/nginx/sites-available/ai-doc-parser /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## 8. Access from Other Devices

### Find Server IP
```bash
ip addr show
# or
hostname -I
```

### Access URLs

From devices on the same network:
- User Frontend: `http://server-ip:3000`
- Server Dashboard: `http://server-ip:3001`
- Backend API: `http://server-ip:8000`

If using Nginx:
- User Frontend: `http://your-domain.com`
- Server Dashboard: `http://your-domain.com/admin`
- Backend API: `http://your-domain.com/api`

## 9. Monitoring and Logs

### View Logs
```bash
# Backend logs
sudo journalctl -u ai-doc-parser-backend -f

# User frontend logs
sudo journalctl -u ai-doc-parser-user-frontend -f

# Server frontend logs
sudo journalctl -u ai-doc-parser-server-frontend -f
```

### Restart Services
```bash
sudo systemctl restart ai-doc-parser-backend
sudo systemctl restart ai-doc-parser-user-frontend
sudo systemctl restart ai-doc-parser-server-frontend
```

## 10. Backup

### Database Backup
```bash
# Backup database
cp /home/your-user/AI_Doc_Parser/backend/documents.db /backup/documents_$(date +%Y%m%d).db

# Backup uploads
tar -czf /backup/uploads_$(date +%Y%m%d).tar.gz /home/your-user/AI_Doc_Parser/backend/uploads/
```

### Automated Backup (Cron)
```bash
crontab -e
```

Add:
```
0 2 * * * cp /home/your-user/AI_Doc_Parser/backend/documents.db /backup/documents_$(date +\%Y\%m\%d).db
0 2 * * * tar -czf /backup/uploads_$(date +\%Y\%m\%d).tar.gz /home/your-user/AI_Doc_Parser/backend/uploads/
```

## 11. Security Recommendations

1. **Use HTTPS**: Set up SSL/TLS with Let's Encrypt
   ```bash
   sudo apt install certbot python3-certbot-nginx
   sudo certbot --nginx -d your-domain.com
   ```

2. **Secure .env file**:
   ```bash
   chmod 600 /home/your-user/AI_Doc_Parser/backend/.env
   ```

3. **Regular Updates**:
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

4. **Limit Upload Size**: Already configured in backend (10MB)

5. **Use Strong Passwords**: For server access

## Troubleshooting

### Service Won't Start
```bash
# Check logs
sudo journalctl -u service-name -n 50

# Check if port is in use
sudo netstat -tulpn | grep :8000
```

### Permission Issues
```bash
# Fix ownership
sudo chown -R your-user:your-user /home/your-user/AI_Doc_Parser
```

### Database Locked
```bash
# Stop all services
sudo systemctl stop ai-doc-parser-*
# Start them one by one
```

---

**Your application is now deployed and accessible from any device on your network!**
