draws, *boards = open('4.txt').read().split('\n\n')

T = lambda xs: zip(*xs) # Transpose
flatten = lambda xs: [y for x in xs for y in x] # Flatten a 2d array
convert_board = lambda board: [[int(x) for x in row.split()] for row in board.splitlines()]
boards = [convert_board(b) for b in boards]

line_done = lambda xs: all(x in prev_drawn for x in xs)
board_done = lambda b: any(line_done(row) for row in b) or any(line_done(col) for col in T(b))

prev_drawn = set()
score = lambda b: sum(x for x in flatten(b) if x not in prev_drawn)
scores = list()

finished = [False for _ in boards]

for draw in map(int, draws.split(',')):
    prev_drawn.add(draw)

    for i, board in enumerate(boards): #not finished[i] and 
        if board_done(board):
            scores.append(draw * score(board))

            finished[i] = True

            if all(finished):
                print('Part 1', scores[0], 'Part 2', scores[-1])
                exit()