# Windows Client - Frontend Applications

This folder contains the frontend applications to run on your Windows PC.

## Prerequisites
- Node.js 18+ installed
- npm or yarn

## Quick Start

### 1. Install Dependencies

```bash
# User Frontend
cd user-frontend
npm install

# Server Frontend
cd ../server-frontend
npm install
```

### 2. Configure API URL

Create `.env.local` file in each frontend directory:

**user-frontend/.env.local**
```
NEXT_PUBLIC_API_URL=http://<your-linux-server-ip>:8000
```

**server-frontend/.env.local**
```
NEXT_PUBLIC_API_URL=http://<your-linux-server-ip>:8000
```

Replace `<your-linux-server-ip>` with your actual Linux server IP address.

### 3. Run the Applications

```bash
# Terminal 1 - User Frontend
cd user-frontend
npm run dev

# Terminal 2 - Server Frontend
cd server-frontend
npm run dev
```

## Access

- **User Frontend**: http://localhost:3000
- **Server Frontend**: http://localhost:3001

## Troubleshooting

If you get CORS errors, ensure:
1. The Linux backend is running
2. The API URL in `.env.local` is correct
3. The backend CORS settings allow your requests
