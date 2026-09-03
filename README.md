# FreelanceHub Pro

Full-stack freelance marketplace built with React.js, Flask/Python and MySQL.

## Added 7 recommended features
1. Freelancer profiles: bio, skills, hourly rate, experience, availability, location, ratings.
2. Freelancer portfolios: projects, technologies, GitHub and live-demo links.
3. Advanced project search: keyword, skill, budget range, experience and project type.
4. Messaging: REST conversation API with project context and attachment URL support; ready for WebSocket upgrade.
5. Notifications: proposal, hiring and milestone notifications.
6. Payments: milestone fund/release demo workflow with a production Razorpay/Stripe integration point.
7. Admin dashboard/reporting: platform statistics and user/project report management.

## Existing workflow
JWT authentication, client/freelancer/admin roles, project posting, proposals, bidding, hiring, contracts, milestones, reviews, saved projects and responsive UI.

## Four-person team
- Person 1 — Frontend Developer: React UI, routing, dashboards, profiles, search and API integration.
- Person 2 — Backend Developer: Flask REST APIs, JWT authentication, authorization, notifications and business logic.
- Person 3 — Database Developer: MySQL schema, relationships, constraints, indexes, queries and data integrity.
- Person 4 — Full-Stack Integration & QA: contracts, milestones, messaging, payment integration, reviews, admin, testing and deployment.

## Run locally

### MySQL
CREATE DATABASE freelancehub;

### Backend
cd backend
python -m venv venv
# Windows
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python run.py

Backend: http://localhost:5000

### Frontend
cd frontend
npm install
copy .env.example .env
npm run dev

Frontend: http://localhost:5173

## Deployment
Render backend:
- Root: backend
- Build: pip install -r requirements.txt
- Start: gunicorn --bind 0.0.0.0:$PORT run:app

Vercel frontend:
- Root: frontend
- Build: npm run build
- Output: dist
- VITE_API_URL=https://YOUR-RENDER-URL.onrender.com/api

Payment endpoints are demo endpoints; connect and verify Razorpay/Stripe webhooks before processing real money. Messaging is REST-based and can be upgraded to Flask-SocketIO/WebSockets.
