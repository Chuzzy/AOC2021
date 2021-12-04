from copy import deepcopy, copy
test = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""
draws, *boards = open('4.txt').read().split('\n\n')
#draws, *boards = test.split('\n\n')

#print(boards[:5])

t = lambda xs: list(map(int, xs))
#draws = [int(x) for x in draws]
draws = t(draws.split(','))

b = lambda xs: [list(map(int, x.split())) for x in xs.splitlines()]
#boards = [list(map(int, x.split())) for board in boards for x in board.splitlines()]
boards = [b(ys) for ys in boards]
old_boards = deepcopy(boards)

#print(draws)
#print(boards[:5])
#print('\n\n')
#print(boards[0])

boards = deepcopy(boards)
filled = deepcopy([[[False]*5]*5 for _ in boards])
c = lambda xs: xs[:]
filled = [c([x[:] for x in f[:]]) for f in filled]
boards = [c([x[:] for x in b[:]]) for b in boards]

print('0', filled[0])
filled[0][0][0] = True
print('0 again', filled[0])

print('1', filled[1])


def win(f):
    for row in f:
        #print(f, row)
        if all(row):
            #print('row won with', row)
            return True
    
    for col in zip(*f):
        if all(col):
            #print('col won with', col)
            return True
    
    return False

finished = [copy(False) for _ in boards]
finished = finished[:]
print('FIN', finished)
prev_finished = 0

for z, draw in enumerate(draws):
    # Update
    print(boards == old_boards)

    for k, b in enumerate(boards):
        for i, x in enumerate(b):
            for j, y in enumerate(x):
                if y == draw:
                    #print('\n', draws[:z], draw)
                    #print('board changing', *b, sep='\n')
                    #print('filled', *filled[k], sep='\n')
                    #print('test', f[i][j])
                    filled[k][i][j] = True
                    #print('test2', f[i][j])

        
        ##for row in b:
        #    if all(x in draws[:k])

        if win(filled[k]) and not finished[k]:
            print('\n\n!!! WIN')
            print('Board', *b, sep='\n')
            print()
            print('Filled', *filled[k], sep='\n')
            print()
            print('Draws', draws[:z])

            fsum = 0
            for brow, frow in zip(b, filled[k]):
                for alpha, beta in zip(brow, frow):
                    if not beta: fsum += alpha

            print(fsum, draw)
            print('Part 1', fsum * draw)
            #print(draws)

            print('?', finished)
            finished[k] = True
            print('???', finished)
            prev_finished = k

            #exit()
    if all(finished):
        print(finished)
        print(prev_finished)
        print(*boards[prev_finished], sep = '\n')

        fsum = 0
        for brow, frow in zip(boards[prev_finished], filled[prev_finished]):
            for alpha, beta in zip(brow, frow):
                if not beta: fsum += alpha

        print(fsum, draw)
        print('Part 2', fsum * draw)
        exit()