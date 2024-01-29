"""
Entry point for the scraper.
"""

from icecream import ic

from scraper.src.schemas import TournamentSchema


def run():
    ic()
    tourney = TournamentSchema(
        id=1,
        name="test",
        slug=1234,
        city="test",
        state="test",
        phone=1234,
        email="test",
    )
    ic(tourney)


if __name__ == "__main__":
    run()
