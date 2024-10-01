# Problem: Asyncio Example
# Question: Implement a simple asyncio task that fetches data from multiple URLs concurrently.








import asyncio
import requests

async def fetch_url(url):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, requests.get, url)

async def fetch_all(urls):
    tasks = [fetch_url(url) for url in urls]
    return await asyncio.gather(*tasks)

# Example usage
# asyncio.run(fetch_all(["https://api.github.com", "https://www.example.com"]))
