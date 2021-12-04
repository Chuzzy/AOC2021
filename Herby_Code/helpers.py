from itertools import starmap

def bin(s):
    return sum(2**i*(b=='1') for i, b in enumerate(s[::-1]))

count_ = lambda c, xs: sum(c(x) for x in xs)
count = lambda c, xs: sum(map(c, xs))

transpose_ = lambda xs: zip(*xs)
transpose = lambda xs: [list(x) for x in zip(*xs)]

print(*transpose_([[1, 2, 3], [2, 3, 4], [10, 11, 12]]))