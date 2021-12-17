from collections import defaultdict, Counter

template, rules = open('14.txt').read().split('\n\n')
test = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""
template, rules = test.split('\n\n')

rules = defaultdict(str, (r.split(' -> ') for r in rules.splitlines()))
#print(rules)

def bigrams(text):
    return [text[i:i+2] for i in range(len(text)-1)]


print(template)
#print(bigrams(template))
print(*map(rules.get, bigrams(template)))

def extend(text, rules):
    additions = [*map(rules.get, bigrams(template))]
    result = ''
    for i in range(len(text)-1):
        result += text[i]
        result += additions[i]
    return result + text[-1]

"""
for i in range(10):
    #print(i, len(template))
    template = extend(template, rules)

print(len(template))
count = Counter(template)
print(count)

mf = max(count, key = lambda x: count[x])
lf = min(count, key = lambda x: count[x])

print(count[mf] - count[lf])
"""
pair_mapping = defaultdict(tuple)
for k, v in rules.items():
    pair_mapping[k] = (k[0] + v, v + k[1])

pair_counts = Counter(bigrams(template))
for i in range(40):
    new_counts = Counter()
    for pair, c in pair_counts.items():
        for result in pair_mapping[pair]:
            new_counts[result] += c
    pair_counts = new_counts.copy()

def ct(cts):
    result = Counter()
    for k, v in cts.items():
        result[k[0]] += v
        result[k[1]] += v
    return result

#print(pair_mapping)
print(pair_counts)

#cts = [ct(k, pair_counts) for k in list(template)]

print(ct(pair_counts))

def rdp(n):
    if n % 2 == 0: return n//2
    return (n+1)//2

cts2 = {k: (v+1)//2 for k, v in ct(pair_counts).items()}
print(cts2)

print(max(cts2.values()) - min(cts2.values()))
#print(Counter(bigrams('NBBBCNCCNBBNBNBBCHBHHBCHB')))

#print(*cts)
#print(max(cts) - min(cts))