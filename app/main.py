from fastapi import FastAPI
from app.api import leads
from contextlib import asynccontextmanager
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.api import leads
from app.services.automation import auto_sync_github_gigs

@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler = AsyncIOScheduler()
    scheduler.add_job(auto_sync_github_gigs, 'interval', minutes=0.5) # change the interval to 60 after testing
    scheduler.start()
    yield
    scheduler.shutdown()

app = FastAPI(
    title="LeadSense API",
    description="Personal developer opportunity discovery & skill progression engine",
    version="0.1.0",
    lifespan=lifespan
)

app.include_router(leads.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the LeadSense API!", "status": "active"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "database": "not_connected"}