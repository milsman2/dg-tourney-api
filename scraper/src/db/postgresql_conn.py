"""
Create a connection to the PostgreSQL database using SQLAlchemy's asyncpg driver.
"""

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from scraper.src.config import settings

engine = create_async_engine(
    f"postgresql+asyncpg://{settings.PG_USER}:{settings.PG_PW}@{settings.PG_HOST}/{settings.PG_DB}"
)
async_session = async_sessionmaker(engine, expire_on_commit=False)
