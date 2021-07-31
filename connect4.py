import random
import time
import copy
import numpy
import math

# board in nested list
boardlist = [[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']]

# Convert boardlist into 2d array for AI iterations
board = numpy.array(boardlist)

# draws the board
def boardprint():
    print("\t  1   2   3   4   5   6   7")
    print("\t+---+---+---+---+---+---+---+")
    print("\t| "+board[0,0]+" | "+board[0][1]+" | "+board[0][2]+" | "+board[0][3]+" | "+board[0][4]+" | "+board[0][5]+" | "+board[0][6]+" |")
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

# Launch 2 player game and randomizer to determine who starts
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
    move = 0
    while move not in valid:
        try:
            move = int(input(player+ ", please select which column you want to drop your piece("+piece+"): (1 - 7): "))
        except ValueError:
            continue
    return move

# runs several fuctions to check boardstate for wins for player
def checkwin(board, piece):
    # Horizontal check
    for column in range(6):
        for row in range(4):
            if board[column][row] + board[column][row+1] + board[column][row+2] + board[column][row+3] == 4 * piece:
                return True
            
    # Vertical check
    for column in range(3):
        for row in range(7):
            if board[column][row] + board[column+1][row] + board[column+2][row] + board[column+3][row] == 4 * piece:
                return True
            

    # diagonal check a 
    for column in range(3):
        for row in range(4):
            if board[column][row] + board[column+1][row+1] + board[column+2][row+2] + board[column+3][row+3] == 4 * piece:
                return True
            
    # diagonal check b
    for column in range(3,6):
        for row in range(4):
            if board[column][row] + board[column-1][row+1] + board[column-2][row+2] + board[column-3][row+3] == 4 * piece:
                return True
                
# runs checkwin functions and displays winner
def winner(board):
    if checkwin(board, piece):
        boardprint()
        print("\n\t  -------------------------")
        print("\t       "+player+" won!!!")
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
def drop(board, move, piece):
    i = 0
    if board[i][move-1] != ' ':
        return False
    else:
        while board[i][move-1] == ' ':
            if i == 5:
               board[i][move-1] = piece
               return True
            i += 1
        board[i-1][move-1] = piece
        return True

def dropai(tempboard, row, move, aipiece):
    tempboard[row][move] = aipiece

# creating windows of 4x4 to make it easier to set move scores for AI with windowscore function
def scorepostion(board, piece):
    score = 0
    # Score center
    center = [i for i in list(board[:,7//2])]
    centercount = center.count(piece)
    score += centercount * 3
    # Horizontal score
    for row in range(6):
        rowarray = [i for i in list(board[row,:])]
        for column in range(4):
            window = rowarray[column:column+4]
            score += windowscore(window)
    # Vertical score
    for column in range(7):
        columnarray = [i for i in list(board[:,column])]
        for row in range(3):
            window = columnarray[row:row+4]
            score += windowscore(window)
    # Diagonal1 score
    for row in range(3):
        for column in range(4):
            window = [board[row+i][column+i] for i in range(4)]
            score += windowscore(window)
    # Diagonal2 score
    for row in range(3):
        for column in range(4):
            window = [board[row+3-i][column+i] for i in range(4)]
            score += windowscore(window)
    return score 

# Determining the points for the boardstate after a certain AI move while minimaxing
def windowscore(window):
    score = 0
    if window.count(aipiece) == 4:
        score +=100
    elif window.count(aipiece) == 3 and window.count(' ') == 1:
        score += 5
    elif window.count(aipiece) == 2 and window.count(' ') == 2:
        score += 2
    
    if window.count(humanpiece) == 3 and window.count(' ') == 1:
        score -= 4
    return score

# Checks if game is over during minimaxing
def endgame(board):
    return checkwin(board,aipiece) or checkwin(board, humanpiece) or len(getvalidlocation(board)) == 0

# minimax AI
def minimax(board, depth, alpha, beta, maximize):
    validlocations = getvalidlocation(board)
    if depth == 0 or endgame(board):
        if endgame(board):
            if checkwin(board, aipiece):
                return None, 10000000000
            if checkwin(board, humanpiece):
                return None, -10000000000
            else: # No more moves possible
                return None, 0
        else:
            return None, scorepostion(board, aipiece)
    if maximize:
        value = -math.inf # minus infinity
        move = random.randint(0,6)
        for move in validlocations:
            row = nextopenrow(board, move)
            boardcopy = copy.deepcopy(board)
            dropai(boardcopy, row, move, aipiece)
            newscore = minimax(boardcopy, depth-1, alpha, beta, False)[1]
            if newscore > value:
                value = newscore
                bestmove = move
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return bestmove, value

    else:
        value = math.inf # infinity
        move = random.randint(0,6)
        for move in validlocations:
            row = nextopenrow(board, move)
            boardcopy = copy.deepcopy(board)
            dropai(boardcopy, row, move, humanpiece)
            newscore = minimax(boardcopy, depth-1, alpha, beta, True)[1]
            if newscore < value:
                value = newscore
                bestmove = move
            beta = min(beta, value)
            if beta <= alpha:
                break
        return bestmove, value

def nextopenrow(board, column):
    	for row in reversed(range(6)):
            if board[row][column] == ' ':
                return row

# Function to see if column has a free spot for getvalidlocation
def valid(board, move):
    if board[0][move] == ' ':
        return True
    else:
        return False

# Creating a list of column with 1 or more free spots(valid function) for AI to put pieces when minimaxing
def getvalidlocation(board):
    validlocations = []
    for move in range(7):
        if valid(board, move):
            validlocations.append(move)
    return validlocations

# Player turn
def human():
    boardprint()
    move = pmove()
    while not drop(board, move, piece):
        boardprint()
        print("Column is full, please try again, "+player+"!")
        move = pmove()
    if winner(board):
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

# Start 2 player game
def start1p(starter = ['p1','p2']):
    name1 = input("Player 1 please enter your name: ")
    name2 = "Computer"
    print("\nHello, "+name1+"\n" )
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
    return starter, player1, player2

def difficulty(levels = ['1','2','3']):
    levelnr = '0'
    print("How hard do you want the AI to be?\n")
    print("Enter 1 for easy, 2 for medium, 3 for hard")
    while levelnr not in levels:
        levelnr = input("Enter 1, 2 or 3: ")
    if levelnr == '1':
        level = 2
    elif levelnr == '2':
        level = 3
    elif levelnr == '3':
        level = 5
    return level

# AI move
def computer(board):
    move, minmaxscore = minimax(board, level, -math.inf, math.inf, True)
    move += 1 
    boardprint()
    print("Thinking...")
    #time.sleep(1)
    drop(board,move, piece)
    if winner(board):
        exit()
    elif draw():
        exit()

# Game start
print("""
_________           AI Project 2              __      _____  
\_   ___ \  ____   ____   ____   ____   _____/  |_   /  |  | 
/    \  \/ /  _ \ /    \ /    \_/ __ \_/ ___\   __\ /   |  |_
\     \___(  <_> )   |  \   |  \  ___/\  \___|  |  /    ^   /
 \______  /\____/|___|  /___|  /\___  >\___  >__|  \____   | 
        \/            \/     \/     \/     \/           |__| 
\t\t\t\t\t   By Jeroen Penders
 """)
print("Welcome to Connect 4 version 1.2\n")
print("Heuristic minimax AI is implemented, still needs some balancing. Enjoy!\n")
print("Enter 1 to play against the Computer")
print("Enter 2 to play a 2 player game")
choices = ['1','2']
game = 0
if game not in choices:
    game = input("Enter 1 or 2: ")
if game == '1':
    # Start 1 player game
    level = difficulty()
    starter, player1, player2 = start1p()
    if starter == 'p1': # player(human) starts
        humanpiece = 'X'
        aipiece = 'O'
        while free():
            player = player1
            piece = 'X'
            human()
            player = player2
            piece = 'O'
            computer(board)
    
    else: # AI starts
        humanpiece = 'O'
        aipiece = 'X'
        while free():
            player = player1
            piece = 'X'
            computer(board)
            player = player2
            piece = 'O'
            human()

# Start 2 palyer game
else:
    player1, player2 = start2p()
    while free():
        player = player1
        piece = 'X'
        human()
        player = player2
        piece = 'O'
        human()
