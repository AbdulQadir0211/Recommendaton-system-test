import httpx
import os
from dotenv import load_dotenv

load_dotenv()

FLIC_TOKEN = os.getenv("FLIC_TOKEN")
API_BASE_URL = os.getenv("API_BASE_URL")

HEADERS = {
    "Flic-Token": FLIC_TOKEN
}

RESONANCE_PARAM = "resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if"


async def fetch_data_from_endpoint(endpoint: str, page: int = 1, page_size: int = 1000, include_resonance: bool = True):
    params = {
        "page": page,
        "page_size": page_size
    }
    if include_resonance:
        params["resonance_algorithm"] = RESONANCE_PARAM

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/{endpoint}", headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json()
