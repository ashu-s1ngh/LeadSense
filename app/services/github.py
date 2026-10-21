import aiohttp
from app.schemas.lead import LeadCreate

class GitHubProvider:
    BASE_URL = "https://api.github.com/search/issues"

    async def fetch_leads(self, keyword: str) -> list[LeadCreate]:

        query = f'"{keyword}" state:open type:issue'
        params = {
            "q": query,
            "sort": "created",
            "order": "desc",
            "per_page": 10,
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(self.BASE_URL, params=params) as response:
                if response.status != 200:
                    raise Exception(f"Failed to fetch leads from GitHub: {response.status}")
                
                data = await response.json()
                leads = [
                    LeadCreate(
                        title=item["title"],
                        url=item["html_url"],
                        source="GitHub",
                        tech_stack=[keyword],
                    )
                    for item in data.get("items", [])
                ]
                return leads