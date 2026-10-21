from fastapi import FastAPI
from app.api import leads

app = FastAPI(
    title="LeadSense API",
    description="Personal developer opportunity discovery & skill progression engine",
    version="0.1.0",
)

app.include_router(leads.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the LeadSense API!", "status": "active"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "database": "not_connected"}