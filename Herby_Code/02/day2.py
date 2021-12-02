from itertools import starmap

convert = lambda x, y: (x, int(y))

inp = [convert(*l.split(' ')) for l in open('2.txt')]
#inp = starmap(lambda x, y: (x, int(y)), inp)

forw = sum(x for l, x in inp if l == 'forward')
height = sum(x for l, x in inp if l == 'down') - sum(x for l, x in inp if l == 'up')

#print(forw * height)
h, d, a = 0, 0, 0
for l, x in inp:
    if l == 'down':
        #d += x
        a += x
    elif l == 'up':
        #d -= x
        a -= x
    elif l == 'forward':
        h += x
        d += a*x

print(f"Part 1: {forw*height}, Part 2: {h*d}")