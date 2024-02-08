"""
Entry point for the scraper.
"""

from icecream import ic

from scraper.src.models import DiscGolfer


def run():
    ic()
    disc_golfer = DiscGolfer(
        id=2,
        classification="Amateur",
        last_name="Kane",
        first_name="Miles",
        career_events=25,
        career_wins=4,
    )
    ic(disc_golfer)


if __name__ == "__main__":
    run()
