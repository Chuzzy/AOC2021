from functools import lru_cache

#inp = [int(x) for x in "3,4,3,1,2".split(',')]
inp = [int(x) for x in open('6.txt').read().split(',')]

def pos(n: int) -> int:
    return n if n > 0 else 0

def fish_count(T: int) -> int:
    return pos((T+6)//7)

@lru_cache
def babies(T: int) -> int:
    total = 0
    for f in range(9, T+1, 7):
        total += babies(T-f)

    return total + fish_count(T)


def total_fish(xs, T):
    return sum((1 + babies(T-x)) for x in xs)

print('Part 1:', total_fish(inp, 80), 'Part 2:', total_fish(inp, 256))