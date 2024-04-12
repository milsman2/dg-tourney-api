"""
Entry point for the scraper.
"""

import asyncio

import redis.asyncio as redis
from icecream import ic
from src.config import settings


async def run():
    ic()
    r = redis.Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        password=settings.REDIS_PW,
        db=settings.REDIS_DB,
    )
    ic(await r.ping())
    await r.aclose()


if __name__ == "__main__":
    asyncio.run(run())
