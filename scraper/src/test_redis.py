"""
Entry point for the scraper.
"""

import asyncio

import redis.asyncio as redis
from icecream import ic
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from scraper.src.config import settings
from scraper.src.models import DiscGolfer


async def db_fetch(async_session: async_sessionmaker[AsyncSession]):
    ic()
    async with async_session() as session:
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


async def run():
    ic()
    redis_client = redis.Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        password=settings.REDIS_PW,
        db=settings.REDIS_DB,
    )
    engine = create_async_engine(
        f"postgresql+asyncpg://{settings.PG_USER}:{settings.PG_PW}@{settings.PG_HOST}/{settings.PG_DB}"
    )
    async_session = async_sessionmaker(engine, expire_on_commit=False)
    disc_golfer_id = str(12626)
    if await redis_client.exists(disc_golfer_id):
        disc_golfer = await redis_client.hgetall(str(disc_golfer_id))
        await engine.dispose()
        return disc_golfer
    else:
        disc_golfer = await db_fetch(async_session)
        if disc_golfer:
            await redis_client.hset(disc_golfer_id, mapping=disc_golfer)
            await engine.dispose()
            return disc_golfer
    await redis_client.aclose()


if __name__ == "__main__":
    asyncio.run(run())
