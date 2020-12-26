from champion import Champion


def get_sell_cost(champ: Champion) -> int:
    if champ.level == 1:
        return champ.cost
    else:
        return champ.cost - 1
