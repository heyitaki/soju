from timeit import repeat

a = repeat(
    "x = randint(0, 10000000) ** 0.5", setup="from random import randint", repeat=1
)
b = repeat(
    "x = sqrt(randint(0, 10000000))",
    setup="from random import randint; from math import sqrt",
    repeat=1,
)
print(a, b)
