test = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""
test = open('13.txt').read()
points, folds = test.split('\n\n')
points = [tuple(int(x) for x in  l.split(',')) for l in points.splitlines()]
folds = [l.split(' ')[2] for l in folds.splitlines()]
folds = [tuple(f.split('=')) for f in folds]

print(points, folds)

def fold(grid, axis, pos):
    axis = 1 if axis=='y' else 0
    pos = int(pos)

    new_grid = set()

    for pt in grid:
        newpt = [0, 0]
        if pt[axis] > pos:
            newpt[axis] = 2 * pos - pt[axis]
            newpt[1-axis] = pt[1-axis]
        else:
            newpt = pt
        new_grid.add(tuple(newpt))
    return new_grid

def disp(grid):
    X = max(p[0] for p in grid)
    Y = max(p[1] for p in grid)

    for y in range(Y+1):
        for x in range(X+1):
            print('#' if (x, y) in grid else ' ', end='')
        print()

grid = set(points)

#disp(grid)
print('---------------\n\n\n')
#disp(fold(grid, *folds[0]))
print(len(fold(grid, *folds[0])))

result = grid

for f in folds:
    result = fold(result, *f)

disp(result)