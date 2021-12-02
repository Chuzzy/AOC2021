#from itertools import starmap
#count = lambda c, xs: sum(starmap(c, xs))

inp = [int(x) for x in open('1.txt')]
#inp = *map(int, open('1.txt'))

count = lambda c, xs: sum(c(*x) for x in xs)
gt = lambda x, y: x > y

part1 = count(gt, zip(inp[1:], inp))
part2 = count(gt, zip(inp[3:], inp))
print('Part 1', part1, '\nPart 2', part2)