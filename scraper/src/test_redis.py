"""
Entry point for the scraper.
"""

import asyncio

import redis
from icecream import ic
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from scraper.src.db import redis_client, async_session, engine
from scraper.src.models import DiscGolfer


async def db_fetch(a_session: async_sessionmaker[AsyncSession]):
    ic()
    async with a_session() as session:
        stmt = select(DiscGolfer).order_by(DiscGolfer.id)
        result = await session.execute(stmt)
        disc_golfer = result.scalars().first()
        if disc_golfer:
            disc_golfer_obj = {
                "id": disc_golfer.id,
                "classification": disc_golfer.classification,
                "last_name": disc_golfer.last_name,
                "first_name": disc_golfer.first_name,
                "career_events": disc_golfer.career_events,
                "career_wins": disc_golfer.career_wins,
                "rating": disc_golfer.rating,
            }
            return disc_golfer_obj


async def cache_fetch(cache_client: redis.Redis, disc_golfer_id: str):
    ic()
    if cache_client.exists(disc_golfer_id):
        return cache_client.hgetall(str(disc_golfer_id))
    else:
        disc_golfer = await db_fetch(async_session)
        if disc_golfer:
            cache_client.hset(disc_golfer_id, mapping=disc_golfer)
            await engine.dispose()
            return disc_golfer


async def run():
    ic()
    disc_golfer_id = str(12626)
    disc_golfer = await cache_fetch(redis_client, disc_golfer_id)
    ic(disc_golfer)
    redis_client.close()


if __name__ == "__main__":
    asyncio.run(run())
