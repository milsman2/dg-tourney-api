"""
Entry point for the scraper.
"""

from icecream import ic
from scraper.src.models import DiscGolfer, Base
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.future import select


async def run():
    ic()
    engine = create_async_engine(
        "sqlite+aiosqlite:///scraper/src/disc_golfers.db",
        echo=True,
    )

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async_session = async_sessionmaker(engine, expire_on_commit=False)

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
        stmt = select(DiscGolfer)
        # AsyncSession.execute() is used for 2.0 style ORM execution
        # (same as the synchronous API).
        result = await session.scalars(stmt)
        # result is a buffered Result object.
        for disc_golfer in result:
            ic(disc_golfer)
        # for streaming ORM results, AsyncSession.stream() may be used.
        result = await session.stream(stmt)
        # result is a streaming AsyncResult object.
        async for disc_golfer in result.scalars():
            ic(disc_golfer)
        result = await session.scalars(select(DiscGolfer).order_by(DiscGolfer.id))
        ic(result)
        ic(result.first())
        await session.commit()


if __name__ == "__main__":
    asyncio.run(run())
