from app.services.github import GitHubProvider
from app.services.scorer import ProgressionEngine
from app.db.models import Lead
from app.db.session import get_db as session
from sqlalchemy import select

async def auto_sync_github_gigs():
    print("Background Task: Waking up to fetch gigs...")
    provider = GitHubProvider()
    engine = ProgressionEngine()
    
    try:
        fetched_leads = await provider.fetch_leads("fastapi")
    except Exception as e:
        print(f"Background Task Failed: {e}")
        return

    # Manually opening the async database session
    async with session() as db:
        saved_leads = []
        for lead_in in fetched_leads:
            query = select(Lead).where(Lead.url == str(lead_in.url))
            result = await db.execute(query)
            
            if not result.scalars().first():
                score = engine.calculate_score(lead_in.tech_stack)
                db_lead = Lead(
                    **lead_in.model_dump(exclude={"url"}), 
                    url=str(lead_in.url), 
                    comfort_score=score
                )
                db.add(db_lead)
                saved_leads.append(db_lead)
                
        if saved_leads:
            await db.commit()
            print(f"Background Task: Successfully auto-synced {len(saved_leads)} new gigs!")
        else:
            print("Background Task: No new gigs found.")