to_int = lambda xs: [int(x) for x in list(xs)]
test = """2199943210
3987894921
9856789892
8767896789
9899965678"""
inp = [to_int(l) for l in open('9.txt').read().splitlines()]
#inp = [to_int(l) for l in test.splitlines()]

max_x, max_y = len(inp[0]), len(inp)

def get_nbs(x, y):
    nbs = list()
    if x != 0:
        nbs.append(inp[y][x-1])
    if x != max_x - 1:
        nbs.append(inp[y][x+1])
    if y != 0:
        nbs.append(inp[y-1][x])
    if y != max_y - 1:
        nbs.append(inp[y+1][x])
    
    return nbs

part1 = sum(1+inp[y][x] for y in range(max_y) for x in range(max_x) if inp[y][x] < min(get_nbs(x, y)))

print(part1)

places = set((x, y) for y in range(max_y) for x in range(max_x) if inp[y][x] < 9)
for y in range(max_y):
    for x in range(max_x):
        print('█' if (x, y) in places else ' ', end='')
    print()

nbs = lambda x, y: {(x, y), (x-1, y), (x, y-1), (x+1, y), (x, y+1)}

all_nbs = lambda xs: set().union(*[nbs(*p) for p in xs])

final_groups = list()

while places:
    gp = {places.pop()}
    
    #print(f"gp: {gp}, nbs: {all_nbs(gp)}")

    while all_nbs(gp) & places:
        temp = all_nbs(gp) & places
        gp |= temp
        places -= temp
        #print(f"temp: {temp}, gp: {gp}, places: ", '\n\n')
    
    final_groups.append(gp.copy())

#print(*final_groups, sep='\n')
#print(*map(len, final_groups), sep='\n')

sizes = list(map(len, final_groups))
from math import prod
print(prod(sorted(sizes)[-3:]))