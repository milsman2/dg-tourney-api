"""
Entry point for the scraper.
"""

import asyncio

from icecream import ic
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from scraper.src.config import settings
from scraper.src.models import Base, DiscGolfer


async def insert_objects(async_session: async_sessionmaker[AsyncSession]) -> None:
    ic()
    async with async_session() as session:
        async with session.begin():
            session.add_all(
                [
                    DiscGolfer(
                        id=71050,
                        classification="Professional",
                        last_name="Barajas",
                        first_name="Matthew",
                        career_events=133,
                        career_wins=16,
                        rating=999,
                    ),
                    DiscGolfer(
                        id=12626,
                        classification="Professional",
                        last_name="Feldberg",
                        first_name="David",
                        career_events=586,
                        career_wins=124,
                        rating=1018,
                    ),
                ]
            )
        await session.commit()


async def run():
    ic()
    engine = create_async_engine(
        f"postgresql+asyncpg://{settings.PG_USER}:{settings.PG_PW}@{settings.PG_HOST}/{settings.PG_DB}"
    )
    async with engine.begin() as conn:
        ic()
        await conn.run_sync(Base.metadata.create_all)

    async_session = async_sessionmaker(engine, expire_on_commit=False)
    await insert_objects(async_session)
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(run())
