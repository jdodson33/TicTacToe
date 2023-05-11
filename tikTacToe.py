# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 22:36:47 2023

@author: dodsonj
"""
#This is my second design at a tiktaktoe game - human vs computer

class TicTacToe:
    def __init__(self):
        self.board = []
        
    #Generate a number board so users know what to enter to play a given space
    def numBoard(self):
        num = 1
        for i in range(3):
            row = []
            for j in range(3):
                row.append(num)
                num += 1
            self.board.append(row)
    
    #generate normal board
    def playBoard(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ""
    
    #print the board to the users consol
    def print_board(self):
        for i in range(3):
            if i != 0:
                print("---------")
            for j in range(3):
            
                if j != 0:
                    print(" | ", end="")
            
                if self.board[i][j] == "" and j != 2:
                    print(" ", end="")
                elif j != 2:
                    print(str(self.board[i][j]), end="")
                else:
                    print(str(self.board[i][j]))


    #Function to determine the computer's next move based on optimal gameplay
    def nextMove(self):    
        #check for 2 in a row of "O" in columns and rows, and check if there is blank spot (if so - win the game)
        for i in range(3):
            if self.board[i].count("O") == 2 and "" in self.board[i]:
                self.board[i][self.board[i].index("")] = "O"
                return
        
            col = []
            for j in range(3):
                col.append(self.board[j][i])
            if col.count("O") == 2 and "" in col:
                self.board[col.index("")][i] = "O"
                return
    
        #check for 2 "O" and blank spot in diagonals to win the game
        diag1, diag2 = [], []
        for i in range(3):
            diag1.append(self.board[i][i])
        if diag1.count("O") == 2 and "" in diag1:
            self.board[diag1.index("")][diag1.index("")] = "O"
            return
    
        for x, y in [[0,2],[1,1],[2,0]]:
            diag2.append(self.board[x][y])
        if diag2.count("O") == 2 and "" in diag2:
            self.board[diag2.index("")][2 - diag2.index("")] = "O"
            return 
      
        #do the same checks as before but for "X" (aka check for 2 X's and a blank, then play an O)
        for i in range(3):
            if self.board[i].count("X") == 2 and "" in self.board[i]:
                self.board[i][self.board[i].index("")] = "O"
                return 
        
            col = []
            for j in range(3):
                col.append(self.board[j][i])
            if col.count("X") == 2 and "" in col:
                self.board[col.index("")][i] = "O"
                return
    
        #check for 2 "X" and blank spot in diagonals to block the user from winning
        diag1, diag2 = [], []
        for i in range(3):
            diag1.append(self.board[i][i])
        if diag1.count("X") == 2 and "" in diag1:
            self.board[diag1.index("")][diag1.index("")] = "O"
            return
    
        for x, y in [[0,2],[1,1],[2,0]]:
            diag2.append(self.board[x][y])
        if diag2.count("X") == 2 and "" in diag2:
            self.board[diag2.index("")][2 - diag2.index("")] = "O"
            return
    
        #play the next move (starting with the corners)
        for x, y in [[0,0],[0,2],[0,2],[2,2]]:
            if self.board[x][y] == "":
                self.board[x][y] = "O"
                return
    
        #find any available position to play
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    self.board[i][j] = "O"
                    return
        return

    
    #Function to check if the game is over
    def checkOver(self):
        #check rows for 3 in a row
        for row in self.board:
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
                if self.board[j][i] == "X": numX += 1
                elif self.board[j][i] == "O": numO += 1
            if numX == 3: return False, "X"
            elif numO == 3: return False, "O"
    
        #check diagonals
        numO, numX = 0, 0
        for i in range(3):
            if self.board[i][i] == "X": numX += 1
            if self.board[i][i] == "O": numO += 1
        if numX == 3: return False, "X"
        elif numO == 3: return False, "O"

        numO, numX = 0, 0
        for x, y in [[0,2],[1,1],[2,0]]:
            if self.board[x][y] == "X": numX += 1
            if self.board[x][y] == "O": numO += 1
        if numX == 3: return False, "X"
        elif numO == 3: return False, "O"
    
        #check for available blanks
        blank = 0
        for row in self.board:
            for j in range(3):
                if row[j] == "":
                    blank += 1
                    break
            if blank > 0: break
        if blank == 0: return False, "Draw"
    
        return True, None 



    def play(self):
        
        self.numBoard()
        print("Please enter a number 1 through 9 to play in a given position. See the board below")
        print(self.print_board())
        self.playBoard()
    
        play = True
        while play:
        
            user_value = int(input("Enter a number: "))
            if self.board[(user_value-1)//3][(user_value-1)%3] == "":
                self.board[(user_value-1)//3][(user_value-1)%3] = "X"
            else:
                print("That Position is filled, enter a valid number")
                continue
        
            play, winner = self.checkOver()
            if play == False:
                break
        
            self.nextMove()
        
            play, winner = self.checkOver()
            if play == False:
                break
        
            self.print_board()
    
        if winner == "Draw":
            print("This match is a draw, play again to see who the real winner is!!")
        else:
            print("The winner of the game is " + winner + " !!! Congratulations")
        self.print_board()
        return
        

tic_tac_toe = TicTacToe()
tic_tac_toe.play()


            