from collections import deque, Counter

inp = open('6.txt').read().split(',')
#inp = [int(x) for x in inp]

number_of_fish = deque([0] * 9)

for f in inp:
    number_of_fish[int(f)] += 1

for _ in range(80):
    number_of_fish[7] += number_of_fish[0]
    number_of_fish.rotate(-1)

print(sum(number_of_fish))

for _ in range(256-80):
    number_of_fish[7] += number_of_fish[0]
    number_of_fish.rotate(-1)

print(sum(number_of_fish))
