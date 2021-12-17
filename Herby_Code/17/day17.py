inp = open('17.txt').read()
#inp = 'target area: x=20..30, y=-10..-5'
*_, xarea, yarea = inp.split(' ')
xarea = xarea[2:-1]
yarea = yarea.strip()[2:]
xarea = [int(x) for x in xarea.split('..')]
yarea = [int(x) for x in yarea.split('..')]

print(xarea, yarea)

def sign(x):
    if x == 0: return 0
    return x//abs(x)

def update(x, y, xvel, yvel):
    return x + xvel, y + yvel, xvel - sign(xvel), yvel - 1

x, y, xvel, yvel = 0, 0, 7, 2

#for _ in range(8):
#    print(x, y, xvel, yvel)
#    x, y, xvel, yvel = update(x, y, xvel, yvel)
totals = set()

ymax = -1e10
for xvel_ in range(xarea[1]+1): #range(xarea[1]):
    #print('xvel', xvel)
    for yvel_ in range(yarea[0], 3*-yarea[0]):
        #print('xvel, yvel', xvel, yvel)
        x, y = 0, 0
        xvel = xvel_
        yvel = yvel_
        ymax_ = -1e10
        while x+xvel <= xarea[1] and y+yvel >= yarea[0]:
            x, y, xvel, yvel = update(x, y, xvel, yvel)
            ymax_ = max(y, ymax_)
            #print('xy', x, y)
            if xarea[0] <= x <= xarea[1] and yarea[0] <= y <= yarea[1]:
                totals.add((xvel_, yvel_))
                ymax = max(ymax, ymax_)
                #print('!', ymax)
                break

print(ymax)
print(totals)
print(len(totals))

"""
x, y, xvel, yvel = 0, 0, 6, 9
for _ in range(10):
    x, y, xvel, yvel = update(x, y, xvel, yvel)
    print(x, y)
    print(xvel, yvel)
    print()"""