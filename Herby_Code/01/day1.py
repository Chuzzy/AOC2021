#from itertools import starmap
#count = lambda c, xs: sum(starmap(c, xs))

inp = [int(x) for x in open('1.txt')]
#inp = *map(int, open('1.txt'))

count = lambda c, xs: sum(c(*x) for x in xs)
gt = lambda x, y: x > y

comp_window = lambda xs, w: sum(x > y for x, y in zip(inp[w:], inp))

part1 = count(gt, zip(inp[1:], inp))
part2 = count(gt, zip(inp[3:], inp))
print('Part 1', part1, '\nPart 2', part2)
print(comp_window(inp, 1), comp_window(inp, 3))

def c_w(w, xs=[*map(int, open('1.txt'))]): return sum(x > y for x, y in zip(inp[w:], inp))
print(c_w(1), c_w(3))