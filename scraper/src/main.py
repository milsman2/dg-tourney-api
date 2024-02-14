"""
Entry point for the scraper.
"""

from icecream import ic
from scraper.src.models import DiscGolfer, Base
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


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
        "sqlite+aiosqlite:///scraper/src/disc_golfers.db",
        echo=True,
    )

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async_session = async_sessionmaker(engine, expire_on_commit=False)
    await insert_objects(async_session)
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(run())
