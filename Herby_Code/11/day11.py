import numpy as np
from numpy.testing._private.utils import temppath

inp = [[int(x) for x in list(line.strip())] for line in open('11.txt')]
test = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""
test2 = """11111
19991
19191
19991
11111"""
#inp = [[int(x) for x in list(line.strip())] for line in test.splitlines()]

print(inp)

inp = np.array(inp)

def step(grid_):
    grid = grid_.copy()
    #print('start\n', grid)
    grid += 1
    #print('then\n', grid)
    flash = None
    #flashed = (grid == -1).copy()
    flashed = np.zeros_like(grid, dtype=bool)
    #print(flashed)
    #print(grid[flashed])
    #print(grid[~flashed])
    #print('\n\n')
    while np.any(grid[~flashed] > 9):
        flash = (grid > 9).copy()
        #flash = flash != flashed
        flash[flashed] = False
        #flashed = flashed | flash
        flashed[flash] = True

        #print('flash\n', flash)
        #print('flashed\n', flashed)

        #grid += flash[1:X+1]

        grid[1:] += flash[:-1] #r
        grid[:-1] += flash[1:] #l
        grid[:, 1:] += flash[:, :-1] #d
        grid[:, :-1] += flash[:, 1:] #u
        grid[1:, 1:] += flash[:-1, :-1] #rd
        grid[:-1, :-1] += flash[1:, 1:] #lu
        grid[1:, :-1] += flash[:-1, 1:] #ru
        grid[:-1, 1:] += flash[1:, :-1] #ld
        #print('post flash\n', grid)
    
    #grid[grid >= 9] = 0
    grid[flashed] = 0
    #print('Done\n\n\n')
    #print(np.sum(flashed))
    return grid, np.sum(flashed)

total = 0
t = 0
while True:
    t += 1
    inp, highlighted = step(inp)
    total += highlighted
    if highlighted == inp.size:
        print(t)
        print(inp)
        break
    if t == 100: print(total)

print(total)
#print(step(step(inp2)))