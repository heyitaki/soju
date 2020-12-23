import json
from types.champ_stats import ChampDataList


def load_champ_data() -> ChampDataList:
    with open("../data/10/25/champ-info.json") as f:
        data = json.load(f)
    return data
