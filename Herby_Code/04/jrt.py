#Day 4

#Part 1

import numpy as np

with open('day4.txt') as data:
    bingo = [x.strip('\n') for x in data.readlines()]

numbers = bingo[0]
bingo.remove(numbers)
numbers = numbers.split(',')


boards = []
for a in bingo:
    if a == '':
        pass
    else:
        board = a.split(' ')
        while len(board)>5:
            board.remove('')
        boards.append(board)

boardarrays = []
for i in range(0, int(len(boards)/5)):
    row1, row2, row3, row4, row5 = boards[5*i], boards[5*i+1], boards[5*i+2], boards[5*i+3], boards[5*i+4]
    board = np.array([row1, row2, row3, row4, row5])
    boardarrays.append(board)

def findwinningboard(numbers, boardarrays):
    for n in numbers:
            for winningindex, board in enumerate(boardarrays):
                board[np.where(board == n)] = 'm'
                for i in range(0,5):
                    if ''.join(board[i,:]) == 'mmmmm':
                        winningboard , finaln = board, n
                        return winningboard, finaln, winningindex
                    if ''.join(board[:,i]) == 'mmmmm':
                        winningboard , finaln = board, n
                        return winningboard, finaln, winningindex
    
winningboard, finaln, i = findwinningboard(numbers, boardarrays)
sumunmarked = 0
indices = zip(*np.where(winningboard != 'm'))
for i,j in indices:
    sumunmarked += int(winningboard[i, j])
print(sumunmarked*int(finaln))

#Part 2
def findlosingboard(numbers, boardarrays):
    numbersleft = numbers
    while len(boardarrays) > 1:
        winningboard, finaln, winningindex = findwinningboard(numbersleft, boardarrays)
        boardsleft = []
        for i, board in enumerate(boardarrays):
            if i != winningindex:
                boardsleft.append(board)
        boardarrays = boardsleft
        numbersleft = numbersleft[numbersleft.index(finaln):]
    return findwinningboard(numbersleft, boardarrays)

losingboard, finaln , losingindex= findlosingboard(numbers, boardarrays)
sumunmarked = 0
indices = zip(*np.where(losingboard != 'm'))
for i,j in indices:
    sumunmarked += int(losingboard[i, j])
print(sumunmarked*int(finaln))