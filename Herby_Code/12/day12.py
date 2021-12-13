from collections import defaultdict, Counter
inp = [r.split('-') for r in """start-A
start-b
A-c
A-b
b-d
A-end
b-end""".splitlines()]
inp  = [r.strip().split('-') for r in open('12.txt')]


small = lambda s: s.islower() # and s != 'end' and s != 'start'

edges = defaultdict(set)
vertices = set()

for u, v in inp:
    edges[u].add(v)
    edges[v].add(u)
    vertices |= {u, v}

vertices -= {'start', 'end'}

def paths(edges, start='start', seen={'start'}, see_twice=None):
    total = 0

    for v in edges[start]:
        if v == 'end':
            total += 1
        elif small(v):
            if v in seen and v != see_twice:
                continue
            elif v in seen and v == see_twice:
                total += paths(edges, v, seen | {v})
            else:
                total += paths(edges, v, seen | {v}, see_twice)
        else:
            total += paths(edges, v, seen, see_twice)
    
    return total

print('Part 1:', paths(edges))
part2 = paths(edges) + \
    sum(paths(edges, see_twice=v)-paths(edges) for v in vertices if small(v))
print('Part 2:', part2)