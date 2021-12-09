from collections import defaultdict
input=list(map(int,open("6.txt").read().strip().split(',')))

fish=defaultdict(int)
for i in input:
    fish[i]+=1

for d in range(256):
    added=0
    newfish=defaultdict(int)
    for k,v in fish.items():
        if k==0:
            newfish[8]+=v
            newfish[6]+=v
        else:
            newfish[k-1]+=v
    fish=newfish
print(sum(fish.values()))
