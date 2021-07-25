import random

# board in nested lists
board = [[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']]

# draws the board
def boardprint():
    print("\t  1   2   3   4   5   6   7")
    print("\t+---+---+---+---+---+---+---+")
    print("\t| "+board[0][0]+" | "+board[0][1]+" | "+board[0][2]+" | "+board[0][3]+" | "+board[0][4]+" | "+board[0][5]+" | "+board[0][6]+" |")
    print("\t+---+---+---+---+---+---+---+")
    print("\t| "+board[1][0]+" | "+board[1][1]+" | "+board[1][2]+" | "+board[1][3]+" | "+board[1][4]+" | "+board[1][5]+" | "+board[1][6]+" |")
    print("\t+---+---+---+---+---+---+---+")
    print("\t| "+board[2][0]+" | "+board[2][1]+" | "+board[2][2]+" | "+board[2][3]+" | "+board[2][4]+" | "+board[2][5]+" | "+board[2][6]+" |")
    print("\t+---+---+---+---+---+---+---+")
    print("\t| "+board[3][0]+" | "+board[3][1]+" | "+board[3][2]+" | "+board[3][3]+" | "+board[3][4]+" | "+board[3][5]+" | "+board[3][6]+" |")
    print("\t+---+---+---+---+---+---+---+")
    print("\t| "+board[4][0]+" | "+board[4][1]+" | "+board[4][2]+" | "+board[4][3]+" | "+board[4][4]+" | "+board[4][5]+" | "+board[4][6]+" |")
    print("\t+---+---+---+---+---+---+---+")
    print("\t| "+board[5][0]+" | "+board[5][1]+" | "+board[5][2]+" | "+board[5][3]+" | "+board[5][4]+" | "+board[5][5]+" | "+board[5][6]+" |")
    print("\t+---+---+---+---+---+---+---+")

# randomizer to determine who starts
def start2p(starter = ['p1','p2']):
    name1 = input("Player 1 please enter your name: ")
    name2 = input("Player 2 please enter your name: ")
    print("\nHello, "+name1+" and "+name2+"!\n" )
    input("Please press enter to see who begins\n")
    starter = random.choice(starter)
    if starter == 'p1':
        player1 = name1
        player2 = name2
        print(name1+" begins!\n")
        input("Press enter to begin...")
    else:
        player2 = name1
        player1 = name2
        print(name2+" begins!\n")
        input("Press enter to begin...")
    return player1, player2

# player move
def pmove(valid = [1,2,3,4,5,6,7]):
    pmove = 0
    while pmove not in valid:
        try:
            pmove = int(input(player+ ", please select which column you want to drop your piece("+piece+"): (1 - 7): "))
        except ValueError:
            continue
    return pmove

# runs several fuctions to check boardstate for wins for player
def checkwin():
    if winhorizontal():
        return True
    elif winvertical():
        return True
    elif windiagonala():
        return True
    elif windiagonalb():
        return True
    else:
        return False

# runs checkwin functions and displays winner
def winner():
    if checkwin():
        boardprint()
        print("\n\t  -------------------------")
        print("\t     "+player+" won!!!")
        print("\t  -------------------------\n")
        return True
    else:
        return False

# checks if board is full, if so, the game is a draw
def free():
    if any(' ' in move for move in board):
        return True
    else:
        return False

# function to check which is the lowest row of the column that is free
def drop(pmove):
    i = 0
    if board[i][pmove-1] != ' ':
        return False
    else:
        while board[i][pmove-1] == ' ':
            if i == 5:
               board[i][pmove-1] = piece
               return True
            i += 1
        board[i-1][pmove-1] = piece
        return True

# Horizontal check
def winhorizontal():
    for column in range(6):
        for row in range(4):

            if board[column][row] + board[column][row+1] + board[column][row+2] + board[column][row+3] == 4 * piece:
                return True
            else:
                continue

# Vertical check
def winvertical():    
    for column in range(3):
        for row in range(7):
            if board[column][row] + board[column+1][row] + board[column+2][row] + board[column+3][row] == 4 * piece:
                return True
            else:
                continue

# diagonal check a 
def windiagonala():    
    for column in range(3):
        for row in range(4):
            if board[column][row] + board[column+1][row+1] + board[column+2][row+2] + board[column+3][row+3] == 4 * piece:
                return True
            else:
                continue

# diagonal check b
def windiagonalb():
    for column in range(3,6):
        for row in range(4):
            if board[column][row] + board[column-1][row+1] + board[column-2][row+2] + board[column-3][row+3] == 4 * piece:
                return True
            else:
                continue

# Player 1 turn
def human1():
    boardprint()
    p1move = pmove()
    while not drop(p1move):
        boardprint()
        print("Column is full, please try again, "+player+"!")
        p1move = pmove()
    if winner():
        exit()
    elif draw():
        exit()
    
# Player 2 turn    
def human2():
    boardprint()
    p2move = pmove()
    while not drop(p2move):
        boardprint()
        print("Column is full, please try again, "+player+"!")
        p2move = pmove()
    if winner():
        exit()
    elif draw():
        exit()

# print when the game is a draw    
def draw():
    if free():
        return False
    else:
        print("\nThe game ended in a draw (no more moves available)\n")
        return True


# Game start
print("""
_________                                     __      _____  
\_   ___ \  ____   ____   ____   ____   _____/  |_   /  |  | 
/    \  \/ /  _ \ /    \ /    \_/ __ \_/ ___\   __\ /   |  |_
\     \___(  <_> )   |  \   |  \  ___/\  \___|  |  /    ^   /
 \______  /\____/|___|  /___|  /\___  >\___  >__|  \____   | 
        \/            \/     \/     \/     \/           |__| 
\t\t\t\t\t   By Jeroen Penders
 """)
print("Welcome to Connect 4 version 1.1\n")
print("AI is coming soon, for now this is only a 2 player game, enjoy!\n")
player1, player2 = start2p()
while free():
    player = player1
    piece = 'X'
    human1()
    player = player2
    piece = 'O'
    human2()
