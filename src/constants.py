from typing import Dict, List, Union

BOARD_WIDTH = 7
BOARD_HEIGHT = 4

# Champ cost -> total # in pool
CHAMP_POOL_SIZE: Dict[int, int] = {1: 29, 2: 22, 3: 18, 4: 12, 5: 10}

# Player level -> champ drop rate
CHAMP_DROP_RATE: Dict[int, List[Union[int, float]]] = {
    1: [1, 0, 0, 0, 0],
    2: [1, 0, 0, 0, 0],
    3: [0.75, 0.25, 0, 0, 0],
    4: [0.55, 0.30, 0.15, 0, 0],
    5: [0.45, 0.33, 0.20, 0.2, 0],
    6: [0.35, 0.35, 0.25, 0.05, 0],
    7: [0.22, 0.35, 0.30, 0.12, 0.01],
    8: [0.15, 0.25, 0.35, 0.20, 0.05],
    9: [0.10, 0.15, 0.30, 0.30, 0.15],
}

# Champion level -> max health/atk damage modifier
CHAMP_LEVEL_SCALING: Dict[int, float] = {0: 0.7, 1: 1.0, 2: 1.8, 3: 3.24, 4: 5.832}
