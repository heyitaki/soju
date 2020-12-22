from copy import copy

a = [1, 2, 3]
b = copy(a)
b[0] = 5
print(a, b)
