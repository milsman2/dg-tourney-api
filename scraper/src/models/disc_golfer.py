"""
DiscGolfer model
"""

from __future__ import annotations

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class DiscGolfer(Base):
    __tablename__ = "disc_golfer"

    id: Mapped[int] = mapped_column(primary_key=True)
    classification: Mapped[str]
    last_name: Mapped[str]
    first_name: Mapped[str]
    career_events: Mapped[int]
    career_wins: Mapped[int]
