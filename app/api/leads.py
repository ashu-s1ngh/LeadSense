from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.session import get_db
from app.db.models import Lead
from app.schemas.lead import LeadCreate, LeadResponse
from app.services.github import GitHubProvider

router = APIRouter(prefix="/leads", tags=["Leads"])

@router.post("/", response_model=LeadResponse)
async def create_lead(lead_in: LeadCreate, db: AsyncSession = Depends(get_db)):
    db_lead = Lead(**lead_in.model_dump(exclude = {"url"}), url= str(lead_in.url))

    db.add(db_lead)
    await db.commit()
    await db.refresh(db_lead)

    return db_lead

@router.get("/", response_model=list[LeadResponse])
async def get_leads(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Lead).order_by(Lead.created_at.desc()))
    leads = result.scalars().all()
    return leads

@router.post("/sync", response_model=list[LeadResponse])
async def sync_github_leads(keyword: str = "fastapi", db: AsyncSession = Depends(get_db)):
    github_provider = GitHubProvider()
    try:
        fetched_leads = await github_provider.fetch_leads(keyword)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    saved_leads = []
    for lead in fetched_leads:
        query = select(Lead).where(Lead.url == str(lead.url))
        result = await db.execute(query)
        existing_lead = result.scalars().first()

        if not existing_lead:
            db_lead = Lead(**lead.model_dump(exclude={"url"}), url=str(lead.url))
            db.add(db_lead)
            saved_leads.append(db_lead)

    if saved_leads:
        await db.commit()
        for lead in saved_leads:
            await db.refresh(lead)

    return saved_leads