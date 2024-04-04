"""
Testing settings.
"""

import json

from icecream import ic


def test_json():
    ic()
    with open("../data/matt_barajas.json", encoding="utf-8") as f:
        data = json.load(f)
        ic(data)
