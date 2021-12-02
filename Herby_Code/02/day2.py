from itertools import starmap

convert = lambda x, y: (x, int(y))

inp = [convert(*l.split(' ')) for l in open('2.txt')]
#inp = starmap(lambda x, y: (x, int(y)), inp)

#forw = sum(x for l, x in inp if l == 'forward')
#height = sum(x for l, x in inp if l == 'down') - sum(x for l, x in inp if l == 'up')

#print(forw * height)
h, d0 = 0, 0
d1, a = 0, 0
for l, x in inp:
    if l == 'down':
        d0 += x
        a += x
    elif l == 'up':
        d0 -= x
        a -= x
    elif l == 'forward':
        h += x
        d1 += a*x

print(f"Part 1: {d0*h}, Part 2: {d1*h}")