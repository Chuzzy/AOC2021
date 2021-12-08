spl = lambda xs: xs.split(' ')

inp = [[spl(x) for x in l.split(' | ')] for l in open('8.txt').read().splitlines()]

signals, outputs = zip(*inp)

unique_counts = lambda xs: sum([len(x) for x in xs].count(i) for i in [2, 3, 4, 7])

def decode(signals):
    one   = next(filter(lambda xs: len(xs) == 2, signals))
    four  = next(filter(lambda xs: len(xs) == 4, signals))
    seven = next(filter(lambda xs: len(xs) == 3, signals))
    eight = next(filter(lambda xs: len(xs) == 7, signals))
    print('1', one, '4', four, '7', seven, '8', eight)
    a = (set(seven)-set(one)).pop()
    e_g = set(eight)-(set(four).union(set(seven)))
    b_d = set(four)-set(one)
    print(a)

    zero_six_nine = set(filter(lambda xs: len(xs) == 6, signals))
    zero = next(filter(lambda xs: len(set(xs)-b_d) == 5, zero_six_nine))
    zero_six_nine.remove(zero)
    six = next(filter(lambda xs: len(set(xs)-e_g) == 4, zero_six_nine))
    zero_six_nine.remove(six)
    nine = zero_six_nine.pop()

    len_five = set(filter(lambda xs: len(xs) == 5, signals))
    five = next(filter(lambda xs: len(set(xs)-b_d) == 3, len_five))
    three = next(filter(lambda xs: len(set(xs)-set(one)) == 3, len_five))
    len_five.remove(five)
    len_five.remove(three)
    two = len_five.pop()

    s = lambda sx: ''.join(sorted(sx))
    return {s(zero):0, s(one):1, s(two):2, s(three):3, s(four):4, s(five):5, s(six):6, s(seven):7, s(eight):8, s(nine):9}

def output_value(d, o):
    s = lambda sx: ''.join(sorted(sx))

    return 1000*d[s(o[0])] + 100*d[s(o[1])] + 10*d[s(o[2])] + d[s(o[3])]

print(sum(unique_counts(o) for o in outputs))

test = decode("acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab".split(' '))

print(output_value(test, "cdfeb fcadb cdfeb cdbaf".split(' ')))

def part2(inp):
    return sum(
        output_value(decode(x), y) for x, y in inp
    )

print(part2(inp))