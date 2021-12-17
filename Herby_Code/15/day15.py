from collections import defaultdict
import heapq

inp = open('15.txt').read().splitlines()

test = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581""".splitlines()

maze = [[int(x) for x in line] for line in inp]
maze = [[int(x) for x in line] for line in test]
#print(maze)

X, Y = len(maze[0]), len(maze)

nbs = lambda x, y: [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
"""
not_visited = {(x, y) for x in range(X) for y in range(Y)}

distances = defaultdict(lambda: X*Y)
prev = dict()

#current = (0, 0)
distances[(0, 0)] = 0

while (X-1, Y-1) in not_visited: # (X-1, Y-1) in 
    current = min(not_visited, key=lambda x: distances[x])
    not_visited.remove(current)

    for coord in nbs(*current):
        if coord[0] < 0 or coord[0] >= X or coord[1] < 0 or coord[1] >= Y or coord not in not_visited: continue

        current_dist = distances[current]
        current_weight = maze[current[1]][current[0]]
        if distances[coord] > current_dist + current_weight:
            distances[coord] = current_dist + current_weight
            prev[coord] = current
    

print(X, Y)

current = (X-1, Y-1)
path = []

#print(not_visited)
#print(sorted(distances))
#print(sorted(prev))
#prev[(8, 9)]
while current != (0, 0):
    path.append(current)
    current = prev[current]

#print(prev[(X-1, Y-1)])
#print(path[::-1])

print(sum(maze[y][x] for x, y in path))
"""


newmaze = [[0 for _ in range(5*X)] for _ in range(5*Y)]

for i in range(5):
    for j in range(5):
        for y in range(Y):
            for x in range(X):
                newmaze[i*Y+y][j*X+x] = (i + j + maze[y][x]-1)%9 + 1

#print(*newmaze, sep = '\n')


not_visited = {(x, y) for x in range(5*X) for y in range(5*Y)}

distances = defaultdict(lambda: 25*X*Y)
prev = dict()

#current = (0, 0)
distances[(0, 0)] = 0

#nbs = lambda x, y: [(x+1, y), (x, y+1)]

largest_X, largest_Y = 0, 0
#to_do = [(maze[y][x], (x, y)) for x, y in nbs(0, 0)]
to_do = [(0, (0, 0))]
#heapq.heapify(to_do)

while (5*X-1, 5*Y-1) in not_visited: # or (5*X-2, 5*Y-1) in not_visited or (5*X-1, 5*Y-2) in not_visited
    #if len(not_visited) % 1000 == 0: print(len(not_visited))
    #current = min(filter(lambda coord: coord[0]-1<=largest_X and coord[1]-1<=largest_Y, not_visited), key=lambda x: distances[x])
    #print(to_do)
    _, current = heapq.heappop(to_do)
    while current not in not_visited:
        _, current = heapq.heappop(to_do)
    #print('\n\ncurrent', current)
    #print(current in not_visited)
    #print(*filter(lambda x: x[1] not in not_visited, to_do))
    #assert(all(t in not_visited for _, t in to_do))
    #largest_X = max(largest_X, current[0])
    #largest_Y = max(largest_Y, current[1])
    #print(not_visited)
    not_visited.remove(current)

    for coord in nbs(*current):
        if coord[0] >= 5*X or coord[1] >= 5*Y or coord not in not_visited: continue
        #print(coord, coord in not_visited)
        #if coord[0] < current[0] or coord[1] < current[1]: continue

        current_dist = distances[current]
        current_weight = newmaze[current[1]][current[0]]
        if distances[coord] > current_dist + current_weight:
            distances[coord] = current_dist + current_weight
            prev[coord] = current
            #print('adding', coord, distances[coord])
            #print('adding to', to_do)
            heapq.heappush(to_do, (distances[coord], coord[:]))
    


current = (5*X-1, 5*Y-1)
path = []

#print(not_visited)
#print(sorted(distances))
#print(sorted(prev))
#prev[(8, 9)]
while current != (0, 0):
    path.append(current)
    current = prev[current]

#print(prev[(X-1, Y-1)])
#print(path[::-1])

print(sum(newmaze[y][x] for x, y in path))

