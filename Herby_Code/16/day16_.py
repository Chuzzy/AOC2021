from math import prod

inp = open('16.txt').read().strip()

pairs = [l.split(' = ') for l in """0 = 0000
1 = 0001
2 = 0010
3 = 0011
4 = 0100
5 = 0101
6 = 0110
7 = 0111
8 = 1000
9 = 1001
A = 1010
B = 1011
C = 1100
D = 1101
E = 1110
F = 1111""".splitlines()]

hex_to_bin = dict(pairs)
b = lambda bits: int(bits, 2)
zeros = lambda bits: all(b == '0' for b in bits)

inp_bin = ''.join(map(hex_to_bin.get, inp))

class Node():
    def __init__(self, version, type_id, value=None):
        self.version = version
        self.type_id = type_id
        self.value = value
        self.children = list()

def parse_literal(inp_bin, total_len = None):
    #print('parsing literal', inp_bin)
    literal_bin = ''
    rest = inp_bin[:]
    packet_len = 6
    while rest and rest[0] == '1':
        # Not last value
        literal_bin += rest[1:5]
        packet_len += 5
        rest = rest[5:]
    # Last value
    literal_bin += rest[1:5]
    #print('literal val', b(literal_bin))
    rest = rest[5:]
    #print('returning rest', rest)
    return rest, b(literal_bin)

def parse(bits):
    #print('\nparsing bits', bits)
    if zeros(bits): return '', 0
    # Parse the first thing and then return the rest
    ver_bin, type_id_bin, rest = bits[:3], bits[3:6], bits[6:]
    ver, type_id = b(ver_bin), b(type_id_bin)
    ver_total = ver

    val = 0

    packet_len = 6

    if type_id == 4:
        # Literal
        #print('Converting literal')
        rest_len_before = len(rest)
        rest, val = parse_literal(rest)
        packet_len += rest_len_before - len(rest)

    else:
        # Operator
        #print('Converting operator')
        length_type_id = rest[0]
        rest = rest[1:]
        packet_len += 1

        results = []


        if length_type_id == '0':
            op_length_bin, rest = rest[:15], rest[15:]
            packet_len += 15
            op_length = b(op_length_bin)
            #print('op length', op_length)

            while not zeros(rest[:op_length]):
                rest_len_before = len(rest)
                rest, ver, val_ = parse(rest)
                results.append(val_)
                ver_total += ver

                packet_len += rest_len_before - len(rest)
                op_length -= (rest_len_before - len(rest))


        elif length_type_id == '1':
            op_num_bin, rest = rest[:11], rest[11:]
            #print('op num bin', op_num_bin)
            packet_len += 11
            op_num = b(op_num_bin)
            #print('op num', op_num)
            for _ in range(op_num):
                rest_len_before = len(rest)
                #print('sending off', rest)
                rest, ver, val_ = parse(rest)
                results.append(val_)
                ver_total += ver

                packet_len += rest_len_before - len(rest)

        # values from operator
        if type_id == 0:
            val += sum(results)
        elif type_id == 1:
            val += prod(results)
        elif type_id == 2:
            val += min(results)
        elif type_id == 3:
            val += max(results)
        elif type_id == 5:
            val += results[0] > results[1]
        elif type_id == 6:
            val += results[0] < results[1]
        elif type_id == 7:
            val += results[0] == results[1]

    #print('before trimming', rest)
    #print('packet len', packet_len)

    #print('removing zeros')
    equals_zero = [b == '0' for b in rest]
    if equals_zero[0]:
        #print('Trimming zeros')
        #print('before', rest)
        first_nonzero = equals_zero.index(True)
        #print('after', rest[first_nonzero:])
        return rest[first_nonzero:], ver_total, val
    else:
        #print('no trimming')
        #print('returning', rest)
        return rest, ver_total, val
    



bs = lambda bits: ''.join(map(hex_to_bin.get, bits))
#print(parse(bs('C200B40A82')))

print(parse(bs(inp)))