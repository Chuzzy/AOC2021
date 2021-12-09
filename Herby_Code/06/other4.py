data = [int(x) for x in open('6input').read().split(',')]

fishies = [0]*9
for i in data:
    fishies[i] += 1

day = 0
while 1:
    print(day, fishies, sum(fishies))
    spawn = fishies[0]
    fishies = fishies[1:7] + [fishies[7] + spawn, fishies[8]] + [spawn]
    day += 1
    
    if day > 256: break
    
