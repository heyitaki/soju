from copy import copy

# a = [1, 2, 3]
# b = copy(a)
# b[0] = 5
# print(a, b)


class t:
    def __init__(self):
        self.t = 1


a = [t(), t(), t()]
print(a.index(a[1]))
