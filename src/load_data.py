import json

from src.types.champ_stats import ChampDataList


def load_champ_data() -> ChampDataList:
    with open("./data/10/25/champ-info.json") as f:
        data = json.load(f)
    return data


champ_data = load_champ_data()
