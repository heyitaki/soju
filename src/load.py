import json
from types.champ_stats import ChampData


def get_champ_data() -> ChampData:
    with open("../data/10/25/champ-info.json") as f:
        data = json.load(f)
    return data
