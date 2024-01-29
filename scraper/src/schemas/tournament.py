"""
Tournament schema
"""
from pydantic import BaseModel, Field
from typing import Optional


class TournamentSchema(BaseModel):
    tournament_id: int = Field(..., alias="id")
    name: str
    slug: int
    city: str
    state: str
    phone: int
    email: Optional[str] = None


class TourneyRoundSchema(BaseModel):
    player_id: int
    score: int
    tournament: TournamentSchema
    rating: int
    round: int
