# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 22:46:14 2020

@author: Rares2
"""

"""
Representation:
   We keep the board as a 5x6 matrix of 0s
   for the geometric forms we use 1,2,3,4,5 in the board matrix
    
Description:
    We generate two random coordinates to start the figure from,
    form the first figure,
    generate again, form second..
    I also won't event start generating the figures only if they are not duplicates or the y coord is <= 4
    if at any point two figures collide, stop the execution and print <Solution not found>
"""

import numpy as np

def generateCoordinates(high,low):
    
    coordinates=[]
    
    for i in range(5):
        randomNumbersUniform = np.random.uniform(low,high,2)
        coordinates.append(list(randomNumbersUniform))
        for coord in coordinates:
            coord[0] = int(coord[0])
            coord[1] = int(coord[1])
    
    return coordinates


def generateFirstFigure(coords,board):
    
    x=coords[0]
    y=coords[1]
    
    board[x][y] = 1
    board[x][y+1] = 1
    board[x][y+2] = 1
    board[x][y+3] = 1
    
    return board


def generateSecondFigure(coords ,board):
    
    x=coords[0]
    y=coords[1]
    
    if(board[x][y]==0 and board[x-1][y] == 0 and board[x][y+1] == 0 and board[x][y+2] == 0):
        board[x][y] = 2
        board[x-1][y] = 2
        board[x][y+1] = 2
        board[x][y+2] = 2
    else:
        raise Exception("Not a solution!")
        
        
    return board

def generateThirdFigure(coords, board):
    
    x=coords[0]
    y=coords[1]
    
    if(board[x][y]==0 and board[x-1][y] == 0 and board[x][y+1] == 0 and board[x][y+2] == 0 and board[x-1][y+2] == 0):
        
        board[x][y] = 3
        board[x-1][y] = 3
        board[x][y+1] = 3
        board[x][y+2] = 3
        board[x-1][y+2] = 3
    else:
        raise Exception("Not a solution!")
        
    return board

def generateFourthFigure(coords, board):
    
    x=coords[0]
    y=coords[1]
    
    if(board[x][y]==0 and board[x][y+1] ==0 and board[x][y+2] == 0 and board[x+1][y+2] == 0):
        
        board[x][y] = 4
        board[x][y+1] = 4
        board[x][y+2] = 4
        board[x+1][y+2] = 4
        
    else:
        raise Exception("Not a solution!")
        
    return board

def generateFifthFigure(coords, board):
    
    x=coords[0]
    y=coords[1]
    
    if(board[x][y] == 0 and board[x][y+1] == 0 and board[x][y+2] == 0 and board[x-1][y+1] == 0):
        
        board[x][y] = 5
        board[x][y+1] = 5
        board[x][y+2] = 5
        board[x-1][y+1] = 5
        
    else:
        raise Exception("Not a solution!")
        
        
    return board
    
    
    


def main3(numberOfAttempts):
    
    
    
    found=False
    
    
    while(found==False):
        
        board = [[0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0]]
        
        coordinates = generateCoordinates(0,6)
        #print(coordinates)
        ok=True
        
        for coord in coordinates:
            if coordinates.count(coord) > 1 and coord[1] > 3:
                #print("Coordinates can't yield solution!")
                ok=False
                break
                
        if(ok==True):
            try:
            
                board = generateFirstFigure(coordinates[0],board)
                #print(board)
                board = generateSecondFigure(coordinates[1],board)
                #print(board)
                board = generateThirdFigure(coordinates[2],board)
                #print(board)
                board = generateFourthFigure(coordinates[3],board)
                
                board = generateFifthFigure(coordinates[4],board)
                print("Solution found!")
                for item in board:
                    print(item)
                print("---------------------")
                numberOfAttempts=0
                found=True
            
            except:
                pass
                #print("Not a solution1!")
                
            
            
            
            
            
        numberOfAttempts-=1    
            

