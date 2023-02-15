# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 22:36:47 2023

@author: dodsonj
"""
#This is my first attempt at a tiktaktoe game - human vs computer

#Generate a number board so users know what to enter to play a given space
def generate_board():
    num = 1
    board = [["" for x in range(3)] for y in range(3)]
    for i in range(3):
        for j in range(3):
            board[i][j] = num
            num += 1
    return board
        
board = [["" for x in range(3)] for y in range(3)]

#print the board to the users consol
def print_board(board):
    for i in range(len(board)):
        if i != 0:
            print("---------")
        for j in range(len(board[0])):
            
            if j != 0:
                print(" | ", end="")
            
            if board[i][j] == "" and j != 2:
                print(" ", end="")
            elif j != 2:
                print(str(board[i][j]), end="")
            else:
                print(str(board[i][j]))


#Function to determine the computer's next move based on optimal gameplay
def nextMove(board):    
    #check for 2 in a row of "O" in columns and rows, and check if there is blank spot (if so - win the game)
    for i in range(3):
        if board[i].count("O") == 2 and "" in board[i]:
            board[i][board[i].index("")] = "O"
            return board
        
        col = []
        for j in range(3):
            col.append(board[j][i])
        if col.count("O") == 2 and "" in col:
            board[col.index("")][i] = "O"
            return board
    
    #check for 2 "O" and blank spot in diagonals to win the game
    diag1, diag2 = [], []
    for i in range(3):
        diag1.append(board[i][i])
    if diag1.count("O") == 2 and "" in diag1:
        board[diag1.index("")][diag1.index("")] = "O"
        return board
    
    for x, y in [[0,2],[1,1],[2,0]]:
        diag2.append(board[x][y])
    if diag2.count("O") == 2 and "" in diag2:
        board[diag2.index("")][2 - diag1.index("")] = "O"
        return board
      
    #do the same checks as before but for "X" (aka check for 2 X's and a blank, then play an O)
    for i in range(3):
        if board[i].count("X") == 2 and "" in board[i]:
            board[i][board[i].index("")] = "O"
            return board
        
        col = []
        for j in range(3):
            col.append(board[j][i])
        if col.count("X") == 2 and "" in col:
            board[col.index("")][i] = "O"
            return board
    
    #check for 2 "X" and blank spot in diagonals to block the user from winning
    diag1, diag2 = [], []
    for i in range(3):
        diag1.append(board[i][i])
    if diag1.count("X") == 2 and "" in diag1:
        board[diag1.index("")][diag1.index("")] = "O"
        return board
    
    for x, y in [[0,2],[1,1],[2,0]]:
        diag2.append(board[x][y])
    if diag2.count("X") == 2 and "" in diag2:
        board[diag2.index("")][2 - diag2.index("")] = "O"
        return board
    
    #play the next move (starting with the corners)
    for x, y in [[0,0],[0,2],[0,2],[2,2]]:
        if board[x][y] == "":
            board[x][y] = "O"
            return board
    
    #find any available position to play
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "O"
                return board
    
    return board

    
#Function to check if the game is over
def checkOver(board):
    #check rows for 3 in a row
    for row in board:
        numO, numX = 0, 0
        for val in row:
            if val == "X": numX += 1
            elif val == "O": numO += 1
        if numX == 3: return False, "X"
        elif numO == 3: return False, "O"
    
    #check columns for 3 in a row
    for i in range(3):
        numO, numX = 0, 0
        for j in range(3):
            if board[j][i] == "X": numX += 1
            elif board[j][i] == "O": numO += 1
        if numX == 3: return False, "X"
        elif numO == 3: return False, "O"
    
    #check diagonals
    numO, numX = 0, 0
    for i in range(3):
        if board[i][i] == "X": numX += 1
        if board[i][i] == "O": numO += 1
    if numX == 3: return False, "X"
    elif numO == 3: return False, "O"

    numO, numX = 0, 0
    for x, y in [[0,2],[1,1],[2,0]]:
        if board[x][y] == "X": numX += 1
        if board[x][y] == "O": numO += 1
    if numX == 3: return False, "X"
    elif numO == 3: return False, "O"
    
    #check for available blanks
    blank = 0
    for row in board:
        for j in range(3):
            if row[j] == "":
                blank += 1
                break
        if blank > 0: break
    if blank == 0: return False, "Draw"
    
    return True, None 



def play(board):
    
    print("Please enter a number 1 through 9 to play in a given position. See the board below")
    print(print_board(generate_board()))
    
    play = True
    while play:
        
        user_value = int(input("Enter a number: "))
        if board[(user_value-1)//3][(user_value-1)%3] == "":
            board[(user_value-1)//3][(user_value-1)%3] = "X"
        else:
            print("That Position is filled, enter a valid number")
            continue
        
        play, winner = checkOver(board)
        if play == False:
            break
        
        board = nextMove(board)
        
        play, winner = checkOver(board)
        if play == False:
            break
        
        print_board(board)
    
    if winner == "Draw":
        print("This match is a draw, play again to see who the real winner is!!")
    else:
        print("The winner of the game is " + winner + " !!! Congratulations")
    print_board(board)
    return
        

play(board)


#user_val = input("Enter your move as a number: ")
#row = int(user_val[0])-1
#col = int(user_val[1])-1
#board[row][col] = "X"
#print_board(board)
            