"""
Create a Redis client to interact with the Redis server.
"""

import redis
from scraper.src.config import settings

redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    password=settings.REDIS_PW,
    db=settings.REDIS_DB,
)
