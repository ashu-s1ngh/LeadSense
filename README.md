# LeadSense

An automated, full-stack gig-tracking platform designed to seamlessly aggregate, score, and manage freelance developer opportunities.

LeadSense autonomously monitors platforms like GitHub for open issues matching a predefined technical skill matrix, evaluates them via a custom progression engine, and surfaces high-value leads on a clean, edge-to-edge SaaS dashboard.

## 🚀 Features

- **Automated Background Sync:** Utilizes APScheduler to run asynchronous fetching tasks at defined intervals without blocking the main API thread.
- **Intelligent Scoring Engine:** Automatically assigns a "Comfort Score" (out of 5) to incoming leads based on tech stack alignment.
- **Duplicate Prevention:** Checks incoming URLs against the database in real-time, executing commits only for novel leads.
- **Edge-to-Edge Dashboard:** A brutalist, dark-themed responsive UI built with Tailwind CSS, featuring client-side pagination and real-time mapping of SQLite data.
- **Schema Versioning:** Database architecture and iterative changes (like tracking issue authors) are managed entirely through Alembic migrations.

## 🛠️ Tech Stack

**Backend**

- **Framework:** FastAPI (Python)
- **Database:** SQLite via SQLAlchemy (Async)
- **Migrations:** Alembic
- **Automation:** APScheduler
- **Network:** aiohttp, Pydantic (Data Validation)

**Frontend**

- **UI/UX:** HTML5, Tailwind CSS
- **Logic:** Vanilla JavaScript (ES6+), Fetch API
- **Design Language:** High-contrast, minimalist SaaS aesthetic

## ⚙️ Getting Started

### 1. Backend Setup

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/ashu-s1ngh/LeadSense.git
cd LeadSense
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Database Initialization

LeadSense uses Alembic to manage the SQLite database schema. Construct the tables by running the latest migration:

```bash
alembic upgrade head
```

### 3. Run the API Engine

Start the FastAPI server. The APScheduler background task will automatically begin its fetching cycle.

```bash
uvicorn app.main:app --reload
```

### 4. Launch the Dashboard

The frontend operates independently via API calls.

1. Navigate to the `/frontend` directory.
2. Open `index.html` directly in your browser or serve it using an extension like VS Code Live Server.
3. The dashboard will automatically fetch data from `http://127.0.0.1:8000` and populate the gig pipeline.

## 🏗️ Project Architecture

```text
LeadSense/
├── alembic/                # Database migration scripts
├── app/
│   ├── main.py             # FastAPI app and Lifespan manager (APScheduler)
│   ├── core/               # App configuration and scorers
│   ├── db/
│   │   ├── models.py       # SQLAlchemy ORM models (Lead)
│   │   └── session.py      # Async engine and session factories
│   ├── schemas/
│   │   └── lead.py         # Pydantic validation models
│   └── services/
│       └── github.py       # Async web scraper/provider
├── frontend/
│   └── index.html          # Edge-to-edge Tailwind dashboard
├── alembic.ini             # Alembic configuration
└── requirements.txt
```

## 📖 Development Philosophy

This project is built on a 70/30 practical learning split—prioritizing 70% hands-on engineering and 30% architectural theory. It serves as a continuous project journal for mastering backend systems, asynchronous task scheduling, and seamless API-to-frontend integrations.

## 🗺️ Roadmap

- [ ] Wire the "Force Sync Now" UI button to trigger immediate backend fetches.
- [ ] Expand scraping modules to include Upwork and Reddit pipelines.
- [ ] Implement Discord webhooks for instant notifications on score 4+ gigs.
- [ ] Transition from local web view to a native desktop application wrapper (Tauri/Electron).
