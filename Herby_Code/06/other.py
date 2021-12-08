with open('6.txt') as f:
    s = f.read().strip()
    fish = [int(x) for x in s.split(",")]

time_until = [0] * 9
for f in fish:
    time_until[f] += 1

offset = 0
for day in range(80):
    time_until[(offset+7)%9] += time_until[offset]
    offset = (offset+1)%9
silver = sum(time_until)

for day in range(256-80):
    time_until[(offset+7)%9] += time_until[offset]
    offset = (offset+1)%9
gold = sum(time_until)

print(silver, gold)