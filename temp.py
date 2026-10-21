import aiohttp
import asyncio
import time

HN_API = "https://hacker-news.firebaseio.com/v0"

async def fetch_story(session, story_id):
    async with session.get(f"{HN_API}/item/{story_id}.json") as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        # Get top story IDs
        async with session.get(f"{HN_API}/topstories.json") as response:
            story_ids = await response.json()
        
        print(f"Found {len(story_ids)} stories")
        print(f"First 5 IDs: {story_ids[:5]}")
        
        # Fetch first story details
        start = time.perf_counter()
        stories = await asyncio.gather(*(fetch_story(session, story_id) for story_id in story_ids[:10]))
        elapsed = time.perf_counter() - start

        print(f"\nStory structure:")
        for story in stories:
            for key, value in story.items():
                print(f"  {key}: {repr(value)[:50]}")
        print(f"\nElapsed time: {elapsed:.2f} seconds")

asyncio.run(main())