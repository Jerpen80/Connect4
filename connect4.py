import random

# board in nested lists
board = [[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']]

# draws the board
def boarddraw(board):
    print("  1   2   3   4   5   6   7")
    print("+---+---+---+---+---+---+---+")
    print("| "+board[0][0]+" | "+board[0][1]+" | "+board[0][2]+" | "+board[0][3]+" | "+board[0][4]+" | "+board[0][5]+" | "+board[0][6]+" |")
    print("+---+---+---+---+---+---+---+")
    print("| "+board[1][0]+" | "+board[1][1]+" | "+board[1][2]+" | "+board[1][3]+" | "+board[1][4]+" | "+board[1][5]+" | "+board[1][6]+" |")
    print("+---+---+---+---+---+---+---+")
    print("| "+board[2][0]+" | "+board[2][1]+" | "+board[2][2]+" | "+board[2][3]+" | "+board[2][4]+" | "+board[2][5]+" | "+board[2][6]+" |")
    print("+---+---+---+---+---+---+---+")
    print("| "+board[3][0]+" | "+board[3][1]+" | "+board[3][2]+" | "+board[3][3]+" | "+board[3][4]+" | "+board[3][5]+" | "+board[3][6]+" |")
    print("+---+---+---+---+---+---+---+")
    print("| "+board[4][0]+" | "+board[4][1]+" | "+board[4][2]+" | "+board[4][3]+" | "+board[4][4]+" | "+board[4][5]+" | "+board[4][6]+" |")
    print("+---+---+---+---+---+---+---+")
    print("| "+board[5][0]+" | "+board[5][1]+" | "+board[5][2]+" | "+board[5][3]+" | "+board[5][4]+" | "+board[5][5]+" | "+board[5][6]+" |")
    print("+---+---+---+---+---+---+---+")

# move for player 1
def movep1():
    p1move = int(input("Select which column you want to drop your piece: (1 - 7): "))
    return p1move

# move for player 2
def movep2():
    p2move = int(input("Select which column you want to drop your piece: (1 - 7): "))
    return p2move


# runs several fuctions to check boardstate for wins for player1
def checkwinp1(board):
    if winhorizontal1(board):
        return True
    elif winvertical1(board):
        return True
    elif windiagonala1(board):
        return True
    elif windiagonalb1(board):
        return True
    else:
        return False

# runs several fuctions to check boardstate for wins for player2
def checkwinp2(board):
    if winhorizontal2(board):
        return True
    elif winvertical2(board):
        return True
    elif windiagonala2(board):
        return True
    elif windiagonalb2(board):
        return True
    else:
        return False

# runs checkwin functions and displays winner
def winner():
    if checkwinp1(board):
        boarddraw(board)
        print("Player 1 won!!!")
        return True
    elif checkwinp2(board):
        boarddraw(board)
        print("Player 2 won!!!")
        return True
    else:
        return False

# checks if board is full, if so, the game is a draw
def free(board):
    if any(' ' in move for move in board):
        return True
    else:
        return False

# function to check which is the lowest row of the column that is free (player 1)
def dropp1(p1move):
    i = 0
    if board[i][p1move-1] != ' ':
        return False
    else:
        while board[i][p1move-1] == ' ':
            if i == 5:
               board[i][p1move-1] = 'X'
               return True
            i += 1
        board[i-1][p1move-1] = 'X'
        return True

# function to check which is the lowest row of the column that is free (player 2)
def dropp2(p2move):
    i = 0
    if board[i][p2move-1] != ' ':
        return False
    else:
        while board[i][p2move-1] == ' ':
            if i == 5:
                board[i][p2move-1] = 'O'
                return True
            i += 1
        board[i-1][p2move-1] = 'O'
        return True



# Horizontal check p1
def winhorizontal1(board):
    for column in range(6):
        for row in range(4):

            if board[column][row] + board[column][row+1] + board[column][row+2] + board[column][row+3] == 'XXXX':
                return True
            else:
                continue

# Vertical check p1
def winvertical1(board):    
    for column in range(3):
        for row in range(7):
            if board[column][row] + board[column+1][row] + board[column+2][row] + board[column+3][row] == 'XXXX':
                return True
            else:
                continue

# diagonal check a p1
def windiagonala1(board):    
    for column in range(3):
        for row in range(4):
            if board[column][row] + board[column+1][row+1] + board[column+2][row+2] + board[column+3][row+3] == 'XXXX':
                return True
            else:
                continue

# diagonal check b p1
def windiagonalb1(board):
    for column in range(3,6):
        for row in range(4):
            if board[column][row] + board[column-1][row+1] + board[column-2][row+2] + board[column-3][row+3] == 'XXXX':
                return True
            else:
                continue

# Horizontal check p2
def winhorizontal2(board):
    for column in range(6):
        for row in range(4):
            if board[column][row] + board[column][row+1] + board[column][row+2] + board[column][row+3] == 'OOOO':
                return True
            else:
                continue

# Vertical check p2
def winvertical2(board):    
    for column in range(3):
        for row in range(7):
            if board[column][row] + board[column+1][row] + board[column+2][row] + board[column+3][row] == 'OOOO':
                return True
            else:
                continue

# diagonal check a p2
def windiagonala2(board):    
    for column in range(3):
        for row in range(4):
            if board[column][row] + board[column+1][row+1] + board[column+2][row+2] + board[column+3][row+3] == 'OOOO':
                return True
            else:
                continue

# diagonal check b p2
def windiagonalb2(board):
    for column in range(3,6):
        for row in range(4):
            if board[column][row] + board[column-1][row+1] + board[column-2][row+2] + board[column-3][row+3] == 'OOOO':
                return True
            else:
                continue

# Game start
while free(board):
    boarddraw(board)
    p1move = movep1()
    while not dropp1(p1move):
        boarddraw(board)
        print("Column is full...")
        p1move = movep1()
    if winner():
        exit()
        
    boarddraw(board)
    p2move = movep2()
    while not dropp2(p2move):
        boarddraw(board)
        print("Column is full...")
        p2move = movep2()
    if winner():
        exit()

# only displayed if board is full
print("Board is full, it's a draw")