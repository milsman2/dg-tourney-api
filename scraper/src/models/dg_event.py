"""
Disc Golf Course model
"""

from __future__ import annotations

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class DgEvent(Base):
    __tablename__ = "dg_events"

    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    name: Mapped[str]
