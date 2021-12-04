inp = open('3.txt').read().splitlines()

cols = zip(*inp)

result = ''
for col in cols:
    if 2 * col.count('1') > len(col):
        result += '1'
    else:
        result += '0'

t = lambda x: x * (2**len(inp[0]) - x - 1)
print(int(result, 2))
print(t(int(result, 2)))