from collections import deque
from functools import reduce

inp = [l.strip('\n') for l in open('10.txt')]
test = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""
#inp = [l.strip('\n') for l in test.splitlines()]
#print(inp)


left, right = set('([{<'), set(')]}>')
match = dict(zip('([{<', ')]}>'))
values = dict(zip(')]}>', (3, 57, 1197, 25137)))
scores = {'(': 1, '[': 2, '{': 3, '<': 4}

def score(comp):
    total = 0
    for c in comp[::-1]:
        total = 5*total + scores[c]
    
    return total

print(score('<{(['))

def valid(line):
    Q = deque()
    #print(f"line: {line}")
    for c in line:
        #print(f"c: {c}")
        if c in left:
            Q.append(c)
        else:
            t = Q.pop()
            #print(f"t: {t}, eq: {c == match[t]}")
            if c != match[t]:
                return (values[c], False)
    
    print(''.join(list(Q)))
    return (score(list(Q)), True)

#print(*(valid(l) for l in inp))

results = [valid(l) for l in inp]
part1 = [r for r, c in results if not c]
part2 = [r for r, c in results if c]

print(sum(part1))

part2 = sorted(part2)
print(part2[len(part2)//2])

#print(valid(inp[0]))