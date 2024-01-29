"""
Tournament schema
"""

from typing import Optional

from pydantic import BaseModel, Field


class TournamentSchema(BaseModel):
    """
    Schema for a tournament.
    """

    tournament_id: int = Field(..., alias="id")
    name: str
    slug: int
    city: str
    state: str
    phone: int
    email: Optional[str] = None


class TourneyRoundSchema(BaseModel):
    """
    Schema for a tournament round.
    """

    player_id: int
    score: int
    tournament: TournamentSchema
    rating: int
    round: int
