inp = [int(x) for x in open('7.txt').read().split(',')]
#inp = [int(x) for x in "16,1,2,0,4,2,7,1,2,14".split(',')]


dists = lambda cx, c: sum(abs(c-x) for x in cx)
d = lambda n: (n * (n+1))//2
dists2 = lambda cx, c: sum(d(abs(c-x)) for x in cx)

min_dists = 1e10
min_dists2 = 1e10
for i in range(min(inp), max(inp)+1):
    min_dists = min(min_dists, dists(inp, i))
    min_dists2 = min(min_dists2, dists2(inp, i))
    #print(i, dists2(inp, i))

print(inp)
print(min_dists, min_dists2)


# better:
from statistics import mean, median

print(dists(inp, int(median(inp))), dists2(inp, int(mean(inp))))

# best
mn = sum(inp)//len(inp)
md = sorted(inp)[len(inp)//2]
#print(mean(inp), mn, median(inp), md)
print(dists(inp, md), dists2(inp, mn))