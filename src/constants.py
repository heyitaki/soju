BOARD_WIDTH = 7
BOARD_HEIGHT = 4

# Champ cost -> total # in pool
CHAMP_POOL_SIZE = {
  1: 29,
  2: 22,
  3: 18,
  4: 12,
  5: 10
}

# Player level -> champ drop rate
CHAMP_DROP_RATE = {
  1: [1, 0, 0, 0, 0],
  2: [1, 0, 0, 0, 0],
  3: [.75, .25, 0, 0, 0],
  4: [.55, .30, .15, 0, 0],
  5: [.45, .33, .20, .2, 0],
  6: [.35, .35, .25, .05, 0],
  7: [.22, .35, .30, .12, .01],
  8: [.15, .25, .35, .20, .05],
  9: [.10, .15, .30, .30, .15]
}

# Champion level -> max health/atk damage modifier
CHAMP_LEVEL_SCALING = {
  0: 0.7,
  1: 1.0,
  2: 1.8,
  3: 3.24,
  4: 5.832
}
