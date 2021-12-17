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

print(pairs)
hex_to_bin = dict(pairs)

inp = open('16.txt').read().strip()
inp = "8A004A801A8002F478"
inp_bin = ''.join(map(hex_to_bin.get, inp))

b = lambda bits: int(bits, 2)
zeros = lambda bits: all(b == '0' for b in bits)

ver_total = 0
total_len = 0

def parse_literal(inp_bin, total_len = None):
    literal_bin = ''
    rest = inp_bin[:]
    packet_len = 6
    while rest and rest[0] == '1':
        #print('rest', rest)
        # Not last value
        literal_bin += rest[1:5]
        packet_len += 5
        rest = rest[5:]
    # Last value
    literal_bin += rest[1:5]
    print('literal val', b(literal_bin))
    rest = rest[5:]
    #rest = rest[packet_len%4 + 5:]
    return rest, packet_len
    #if total_len == None:
    #    return rest, packet_len
    #else:
    #    return inp_bin[total_len:], total_len


rest = inp_bin[:]
while not zeros(rest):
    #print('!!', rest)
    ver_bin, type_id_bin, rest = inp_bin[:3], inp_bin[3:6], inp_bin[6:]
    #type_id_bin = inp_bin[3:6]
    #rest = inp_bin[6:]
    ver, type_id = b(ver_bin), b(type_id_bin)
    ver_total += ver

    packet_len = 6

    if type_id == 4:
        # Literal
        print('Converting literal')
        rest, len_ = parse_literal(rest)
        packet_len += len_

    else:
        # Operator
        print('Converting operator')
        length_type_id = rest[0]
        rest = rest[1:]
        if length_type_id == '0':
            op_length_bin, rest = rest[:15], rest[15:]
            #print('rest', rest)
            #print('??', op_length_bin)
            op_length = b(op_length_bin)
            print('op length', op_length)
            sub_len = 0
            while not zeros(rest) and (sub_len + parse_literal(rest[6:])[1]) <= op_length:
                ver_bin, type_id_bin, rest = rest[:3], rest[3:6], rest[6:]
                ver, type_id = b(ver_bin), b(type_id_bin)
                ver_total += ver
                packet_len += 6
                sub_len += 6

                print('??', rest)
                print('parsing another')
                rest, len_ = parse_literal(rest)
                sub_len += len_
                packet_len += len_
                print('rest after that', rest)


            #rest, len_ = parse_literal(rest, op_length)
            #packet_len += len_
        elif length_type_id == '1':
            op_num_bin, rest = rest[:11], rest[11:]
            op_num = b(op_num_bin)
            print('op num', op_num)
            for _ in range(op_num):
                ver_bin, type_id_bin, rest = rest[:3], rest[3:6], rest[6:]
                ver, type_id = b(ver_bin), b(type_id_bin)
                ver_total += ver
                packet_len += 6

                rest, len_ = parse_literal(rest)
                packet_len += len_


    #total_len += len(inp_bin) - len(rest)
    # Deal with binary length
    # Remove all 0s
    if packet_len%4 == 0:
        pass
    else:
        rest = rest[4-packet_len%4:]
    #inp = inp[]
    
    print('rest now', rest)
    try:
        zeros_len = [rest[i:i+4]=='0000' for i in range(0, len(rest), 4)].index(False)
        inp_bin = rest[zeros_len:]
    except:
        inp_bin = rest[:]

print(ver_total)

"""
def parse(inp):
    if all(x == '0' for x in inp): return
    ver_bin = inp_bin[:3]
    type_id_bin = inp_bin[3:6]
    rest = inp_bin[6:]
    ver, type_id = b(ver_bin), b(id_bin)
    ver_total += ver

    packet_len = 6

    if type_id == 4:
        # Literal
        pass

        parse(rest)
    else:
        # Operator
        pass"""