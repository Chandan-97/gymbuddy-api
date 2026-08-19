# GymBuddy Sync API

An asynchronous, high-performance Python backend designed to help gym enthusiasts check into local fitness centers, coordinate workout schedules, match with training partners, and manage session invites in real-time.

This project is built using **Clean Architecture** principles and leverages modern Python asynchronous paradigms.

---

## 🏗️ System Architecture & Design Philosophy

As a senior-level portfolio piece, this application is structured to highlight clean, decoupled, and highly performant backend engineering patterns:

*   **Asynchronous I/O First:** Built entirely on Python's `asyncio` loop utilizing `FastAPI` and `SQLAlchemy 2.0` (with `aiosqlite`) to ensure non-blocking database queries and support high-concurrency requests.
*   **Fail-Safe Configuration Management:** Powered by `pydantic-settings` (V2) to enforce strict validation of environment configurations at system startup. If an environment variable is misconfigured or missing, the application crashes immediately instead of failing silently at runtime.
*   **Separation of Concerns:** The directory structure isolates database models, presentation layers (API endpoints), business logic schemas, and authentication providers to maintain a highly maintainable codebase.

---

## 📁 Directory Structure (todo)
    gymbuddy-sync/
    │ ├── app/
    │ ├── init.py
    │ ├── main.py
    │ ├── config.py # Environment config parsing & schema validation (Pydantic V2) 
    │ ├── database.py # Async SQLAlchemy engine & session generation (Epic 1.2) 
    │ ├── models.py # Core DB schemas (User, Gym, Session, Invite) (Epic 3) 
    │ ├── auth.py # Security dependencies, JWT & password hashing (Epic 2) 
    │ └── schemas.py # Strict request/response Pydantic validation schemas 
    │ ├── .env # Local environment variables (git-ignored) 
    ├── .gitignore # Standard Python gitignore rules 
    ├── Makefile # Task runner for quick setup, testing, and linting 
    ├── requirements.txt # Production & development dependencies 
    └── README.md # Project documentation

---

## 🚀 Getting Started

### 1. Prerequisites
*   Python 3.10, 3.11, or 3.12
*   `pip` (Python package manager)

### 2. Installation
Clone this repository to your local environment, 
navigate to the root directory, and set up your virtual environment:

```
bash

Create virtual environment
python3 -m venv .venv

Activate virtual environment (macOS/Linux)
source .venv/bin/bin/activate

Activate virtual environment (Windows)
.venv\Scripts\activate
```


### 3. Install Dependencies
Install the required packages. Note that we utilize pure-Python fallbacks for JWT and password operations to ensure zero-compilation issues across different operating systems:

`bash pip install --no-cache-dir -r requirements.txt`


### 4. Local Configuration
Create a `.env` file in the root directory. This contains local settings and secrets:

```
env

Application Settings
APP_NAME="GymBuddy Sync API" DEBUG=True API_V1_STR="/api/v1"

Security
JWT_SECRET_KEY="your-super-secret-random-key-change-this-in-production" ALGORITHM="HS256" ACCESS_TOKEN_EXPIRE_MINUTES=60

Database
DATABASE_URL="sqlite+aiosqlite:///./gymbuddy.db"
```

### 5. Running the Application
Launch the development server with hot-reloading enabled:

`bash uvicorn app.main:app --reload`


The server will spin up on **`http://127.0.0.1:8000`**. You can verify that the configuration loaded correctly by calling the health-check endpoint:

`bash curl http://127.0.0.1:8000/health`


---

## 🗺️ Roadmap & Agile Epics

To track development, the project is divided into focused milestones:
1.  **Epic 1: Project Setup & Core Configuration** *(InProgress)*
2.  **Epic 2: User Model & Secure JWT Authentication**
3.  **Epic 3: Gym Database Schemas & Registry API**
4.  **Epic 4: Active Workout Sessions Scheduling**
5.  **Epic 5: Overlapping Session Matchmaking Engine**
6.  **Epic 6: Social Collaboration & Invite State-Machine**
7.  **Epic 7: Real-Time WebSockets Event Dispatcher**
