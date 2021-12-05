inp = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""".split()

#inp = [x for x in open('3.txt')]
inp = open('3.txt').read().split()
print(inp)



def bin(s):
    return sum(2**i*(b=='1') for i, b in enumerate(s[::-1]))

counts = [0] * len(inp[0])

for l in inp:
    for i, x in enumerate(l):
        counts[i] += (x=='1')

final = ''.join(['1' if 2*y > len(inp) else '0' for y in counts])

print(final)
result = bin(final)
print(result)
print(len(final))
print((2**len(final) - result-1))
print((2**len(final) - result-1)*result)


ox, co2 = inp.copy(), inp.copy()

i = 0
while len(ox) > 1:
    freq = sum(o[i]=='1' for o in ox)
    common = '1' if 2*freq >= len(ox) else '0'
    ox = [o for o in ox if o[i] == common]
    i += 1

i = 0
while len(co2) > 1:
    freq = sum(o[i]=='1' for o in co2)
    common = '0' if 2*freq >= len(co2) else '1'
    co2 = [o for o in co2 if o[i] == common]
    i += 1

print(ox, co2)
print(bin(ox[0]) * bin(co2[0]))