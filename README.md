# 🚀 FreelanceHub Pro

[![React](https://img.shields.io/badge/Frontend-React%2018%20%2B%20Vite-61DAFB?logo=react&logoColor=black)](https://react.dev/)
[![Flask](https://img.shields.io/badge/Backend-Flask%203-black?logo=flask)](https://flask.palletsprojects.com/)
[![MySQL](https://img.shields.io/badge/Database-MySQL%20%2F%20SQLite-4479A1?logo=mysql&logoColor=white)](https://www.mysql.com/)
[![JWT](https://img.shields.io/badge/Auth-JWT%20Tokens-000000?logo=jsonwebtokens)](https://jwt.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A modern, full-stack freelance marketplace web application connecting businesses and clients with top-tier freelancers. Built with high performance, role-based access control, responsive design, and intuitive project management tools.

---

## 📌 Table of Contents
- [✨ Key Features](#-key-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [📂 Project Architecture](#-project-architecture)
- [⚡ Quick Start & Setup](#-quick-start--setup)
  - [Prerequisites](#prerequisites)
  - [1. Clone Repository](#1-clone-repository)
  - [2. Backend Setup](#2-backend-setup)
  - [3. Frontend Setup](#3-frontend-setup)
- [🔑 Demo Login Accounts](#-demo-login-accounts)
- [🌐 REST API Reference](#-rest-api-reference)
- [🗄️ Database Schema & ORM](#️-database-schema--orm)
- [🚀 Deployment](#-deployment)
- [🤝 Team & Roles](#-team--roles)
- [📝 License](#-license)

---

## ✨ Key Features

### 👤 Role-Based Portals & Authentication
- **Secure JWT Authentication**: Role-based access control (RBAC) supporting **Freelancer**, **Client**, and **Admin**.
- **Password Security**: Safe password hashing via `werkzeug.security`.

### 💼 For Clients
- **Project Posting**: Create project listings with budgets, deadlines, skill tags, project types (Fixed / Hourly), and experience tiers.
- **Proposal Review**: Review freelancer bids, cover letters, proposed delivery days, and freelancer profiles.
- **Applicant Management**: Accept proposals, award contracts, manage milestones, and collaborate.

### 💻 For Freelancers
- **Smart Project Search & Filters**: Search projects by keyword, required skills, budget range, and experience level.
- **Bidding & Proposals**: Submit competitive proposals specifying bid amounts and estimated turnaround time.
- **Rich Freelancer Profiles & Portfolios**: Showcase bio, hourly rates, experience years, skills, rating, GitHub repositories, and live demo links.
- **Saved Projects**: Bookmark listings to review and bid on later.

### 🛡️ For Administrators
- **Platform Analytics**: Total users count, active project stats, completed contracts, and proposal activity.
- **Moderation**: Platform oversight on users, projects, and dispute resolutions.

### 🔔 Notifications & Milestones
- **Real-Time Style Notifications**: Alerts on new proposals, project acceptances, and status changes.
- **Milestone Tracking**: Project milestone creation, funding, and release workflow.

---

## 🛠️ Tech Stack

| Layer | Technology | Description |
|---|---|---|
| **Frontend** | **React 18** + **Vite** | Blazing-fast SPA with modern React hooks |
| **Routing** | **React Router v6** | Client-side routing with protected routes |
| **HTTP Client**| **Axios** | API requests with interceptors and token handling |
| **Styling** | **Custom CSS3** | Responsive glassmorphism-inspired modern UI |
| **Backend** | **Python 3.10+ / Flask 3.1** | Lightweight RESTful microframework |
| **ORM** | **Flask-SQLAlchemy** | Object-Relational Mapping for Python |
| **Database** | **MySQL / SQLite** | Primary MySQL support with automated SQLite fallback |
| **Auth** | **PyJWT** | Stateless JSON Web Token authentication |

---

## 📂 Project Architecture

```plaintext
FreelanceHub/
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   │   ├── admin.py            # Admin statistics and moderation
│   │   │   ├── applications.py     # Proposals & hiring workflow
│   │   │   ├── auth.py             # User registration & login
│   │   │   ├── notifications.py    # Notification center
│   │   │   ├── projects.py         # Project listings & filtering
│   │   │   ├── saved.py            # Saved/bookmarked projects
│   │   │   └── users.py            # Freelancer profiles & portfolios
│   │   ├── __init__.py             # Flask factory, CORS & DB setup
│   │   ├── models.py               # SQLAlchemy models (User, Project, etc.)
│   │   └── seed.py                 # Comprehensive initial platform data
│   ├── .env.example                # Backend environment template
│   ├── requirements.txt            # Python dependencies
│   └── run.py                      # Backend entry point (Port 5000)
│
├── frontend/
│   ├── public/                     # Public static assets
│   ├── src/
│   │   ├── api.js                  # Axios client & JWT headers
│   │   ├── App.jsx                 # Core UI views & routing
│   │   ├── main.jsx                # Application root mount
│   │   └── styles.css              # Custom styling & animations
│   ├── .env.example                # Frontend environment template
│   ├── index.html                  # HTML5 template
│   ├── package.json                # NPM dependencies & scripts
│   └── vite.config.js              # Vite bundler configuration
│
├── database/
│   └── schema.sql                  # Raw SQL relational schema
├── render.yaml                     # Render.com deployment configuration
└── README.md                       # Documentation
```

---

## ⚡ Quick Start & Setup

### Prerequisites
Make sure you have the following installed on your machine:
- **Git**: [git-scm.com](https://git-scm.com/)
- **Node.js**: [nodejs.org](https://nodejs.org/) (v18 or higher)
- **Python**: [python.org](https://www.python.org/) (v3.10 or higher)
- *(Optional)* **MySQL Server / XAMPP**: If MySQL is not detected, the app automatically runs on a local SQLite fallback database without configuration errors.

---

### 1. Clone Repository

```bash
git clone https://github.com/koushikvarma22/FreelanceHub.git
cd FreelanceHub
```

---

### 2. Backend Setup

Open a terminal in the root directory:

```bash
cd backend

# Create a virtual environment
python -m venv venv

# Activate virtual environment:
# On Windows (CMD / PowerShell):
venv\Scripts\activate
# On macOS / Linux:
# source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create your .env file
# Windows:
copy .env.example .env
# macOS / Linux:
# cp .env.example .env
```

#### *(Optional)* Configure MySQL in `backend/.env`:
If you want to use MySQL, ensure your MySQL service is running and create the database:
```sql
CREATE DATABASE freelancehub;
```
Update `backend/.env`:
```env
DATABASE_URL=mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/freelancehub
JWT_SECRET=your_super_secret_jwt_key
```
*(If left unchanged or if MySQL is unreachable, it automatically creates and runs `freelancehub.db` using SQLite).*

#### Run Backend Server:
```bash
python run.py
```
> **Backend runs at:** `http://localhost:5000`  
> *Tables and initial sample data are seeded automatically on first startup!*

---

### 3. Frontend Setup

Open a **separate terminal** in the root directory:

```bash
cd frontend

# Install npm dependencies
npm install

# Create frontend .env file
# Windows:
copy .env.example .env
# macOS / Linux:
# cp .env.example .env

# Start the Vite development server
npm run dev
```
> **Frontend runs at:** `http://localhost:5173`

---

## 🔑 Demo Login Accounts

The database is pre-seeded with sample accounts for testing all features right away:

| Role | Email | Password | Access Details |
|---|---|---|---|
| **Administrator** | `admin@freelancehub.com` | `admin123` | System stats, dispute oversight, platform logs |
| **Client** | `client1@freelancehub.com` | `password123` | Post projects, review proposals, hire freelancers |
| **Freelancer** | `freelancer1@freelancehub.com` | `password123` | Browse jobs, submit proposals, update portfolio |

*(You can also register new accounts anytime using the Register page).*

---

## 🌐 REST API Reference

### Auth (`/api/auth`)
- `POST /api/auth/register` - Create a new user account (freelancer / client).
- `POST /api/auth/login` - Authenticate user & return JWT token.
- `GET /api/auth/me` - Get profile details of the authenticated user.

### Projects (`/api/projects`)
- `GET /api/projects` - List all open projects (supports search query, skill, and budget filters).
- `GET /api/projects/<id>` - Retrieve details and proposals for a project.
- `POST /api/projects` - Post a new project (client only).
- `PUT /api/projects/<id>` - Edit project listing.
- `DELETE /api/projects/<id>` - Remove project listing.

### Proposals & Hiring (`/api/applications`)
- `POST /api/applications/apply` - Submit a proposal with bid amount and estimated days.
- `GET /api/applications/project/<id>` - Fetch all proposals for a specific project.
- `PUT /api/applications/<id>/status` - Accept or reject a proposal.

### Freelancer Profiles & Portfolios (`/api/users`)
- `GET /api/users/freelancers` - Browse top freelancers with filters.
- `GET /api/users/<id>` - Get detailed freelancer profile and portfolio items.
- `PUT /api/users/profile` - Update bio, skills, hourly rate, and experience.
- `POST /api/users/portfolio` - Add project showcase item with GitHub/demo links.

### Saved Projects & Notifications
- `GET /api/saved` - View saved projects for current user.
- `POST /api/saved/<project_id>` - Toggle bookmark on a project.
- `GET /api/notifications` - View user notifications.
- `PUT /api/notifications/<id>/read` - Mark notification as read.

### Admin (`/api/admin`)
- `GET /api/admin/stats` - Platform-wide statistics (users, projects, revenue metrics).

---

## 🗄️ Database Schema & ORM

The application models relational data using SQLAlchemy:
- **`users`**: User identities, roles, hashed passwords, bios, ratings, skills, and hourly rates.
- **`portfolios`**: Freelancer showcase projects with live demo and GitHub repository links.
- **`projects`**: Job listings, client associations, budgets, deadlines, and requirements.
- **`proposals`**: Freelancer bids, pricing, estimated completion duration, and statuses.
- **`saved_projects`**: User bookmarks for opportunities.
- **`notifications`**: Activity alerts for proposals, awards, and milestones.
- **`milestones`**: Project phase fundings and releases.

---

## 🚀 Deployment

### Backend (Render / Railway / Heroku)
1. Link your GitHub repository.
2. Select **Web Service** with the root directory set to `backend`.
3. Set **Build Command**: `pip install -r requirements.txt`.
4. Set **Start Command**: `gunicorn --bind 0.0.0.0:$PORT run:app`.
5. Add environment variables:
   - `JWT_SECRET`: Random secret string.
   - `DATABASE_URL`: Hosted MySQL / PostgreSQL connection string.

### Frontend (Vercel / Netlify)
1. Connect your repository.
2. Set root directory to `frontend`.
3. Set **Build Command**: `npm run build`.
4. Set **Output Directory**: `dist`.
5. Add environment variable:
   - `VITE_API_URL`: `https://YOUR-BACKEND-URL.onrender.com/api`.

---

## 🤝 Team & Roles

Developed as a collaborative 4-person full-stack engineering workflow:
- **Frontend Engineer**: React SPA UI components, dynamic search, responsive CSS, and state management.
- **Backend Engineer**: RESTful API design, JWT authentication, role-based authorization, and notification hooks.
- **Database Engineer**: Schema design, foreign key relations, constraints, queries, and seeding logic.
- **Full-Stack Integration & QA**: Proposal lifecycles, milestone management, error handling, and deployment setup.

---

## 📝 License

Distributed under the **MIT License**. See `LICENSE` for more details.
