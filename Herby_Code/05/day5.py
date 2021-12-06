from collections import defaultdict

inp = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".splitlines()
inp = open('5.txt').read().splitlines()

m = lambda xs: tuple(map(int, xs.split(',')))
convert_input = lambda s: tuple(map(m, s.split(' -> ')))

inp = [convert_input(l) for l in inp]

counts = defaultdict(int)
counts2 = defaultdict(int)

for xy0, xy1 in inp:
    x0, y0 = xy0
    x1, y1 = xy1
    if x0 == x1:
        for y in range(min(y0, y1), max(y0, y1)+1):
            counts[(x0, y)] += 1
            counts2[(x0, y)] += 1
    elif y0 == y1:
        for x in range(min(x0, x1), max(x0, x1)+1):
            counts[(x, y0)] += 1
            counts2[(x, y0)] += 1
    else:
        if x1 > x0:
            r1 = range(x0, x1+1)
        else:
            r1 = range(x0, x1-1, -1)
        if y1 > y0:
            r2 = range(y0, y1+1)
        else:
            r2 = range(y0, y1-1, -1)
        for x, y in zip(r1, r2):
            counts2[(x, y)] += 1

print(sum(1 for k, v in counts.items() if v >= 2))
print(sum(1 for k, v in counts2.items() if v >= 2))