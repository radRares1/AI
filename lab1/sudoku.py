# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 10:50:37 2020

@author: Rares2
"""

"""
Representation:
    Sudoku represented on a list of lists, each list being a row in the board
    
Description:
    The initial boards are hardcoded and we hardcode the correct solution for each example
    Each time we generate the numbers we just add them in the board and check if the board
    matches the solution
    
"""



import numpy as np

def generateRandomNumbers(high,low,size):
    randomNumbersUniform = np.random.uniform(low,high,size)
    #print(randomNumbersUniform)
    return randomNumbersUniform




def isSolution(currentState,finalState):
    
    currentState.sort()
    finalState.sort()
    return currentState==finalState


def main1(numberOfAttempts):
    
    
    
    firstInitialBoard = [[3,0,0,2],
                         [0,1,4,0],
                         [1,2,0,4],
                         [0,3,2,1]]
    
    firstCurrentBoard = firstInitialBoard.copy()
    
    firstFinalBoard =   [[3,4,1,2],
                         [2,1,4,3],
                         [1,2,3,4],
                         [4,3,2,1]]
    
    firstNumbersToGenerate = 6
    
    secondInitialBoard= [[0,2,0,6,0,8,0,0,5],
                         [5,8,0,0,0,9,7,0,0],
                         [0,0,7,0,4,0,0,2,8],
                         [3,7,0,4,0,1,5,0,0],
                         [6,0,0,0,8,0,0,0,5],
                         [0,0,8,0,0,2,0,1,3],
                         [8,0,6,0,2,0,1,0,0],
                         [0,0,9,8,0,0,0,3,6],
                         [7,0,0,3,0,6,0,9,0]]
    
    secondCurrentBoard = [[0,2,0,6,0,8,0,0,5],
                         [5,8,0,0,0,9,7,0,0],
                         [0,0,7,0,4,0,0,2,8],
                         [3,7,0,4,0,1,5,0,0],
                         [6,0,0,0,8,0,0,0,5],
                         [0,0,8,0,0,2,0,1,3],
                         [8,0,6,0,2,0,1,0,0],
                         [0,0,9,8,0,0,0,3,6],
                         [7,0,0,3,0,6,0,9,0]]
    
    secondFinalBoard=   [[1,2,3,6,7,8,9,4,5],
                         [5,8,4,2,3,9,7,6,1],
                         [9,6,7,1,4,5,3,2,8],
                         [3,7,2,4,6,1,5,8,9],
                         [6,9,1,5,8,3,2,7,2],
                         [4,5,8,7,9,2,6,1,3],
                         [8,3,6,9,2,4,1,5,7],
                         [2,1,9,8,5,7,4,3,6],
                         [7,4,5,3,1,6,8,9,2]]
    
    secondNumbersToGenerate = 45
    
    
    choice = int(input("Choose 1.4x4 Board\n 2.9x9 Board"))
    

    found=False
    
    
    
    if(choice==1):
        
        
        while numberOfAttempts>0 and found==False :
            
            print("New Attempt:")
            
            indexForRandoms=0
            numbersForFirstBoard = generateRandomNumbers(1,5,firstNumbersToGenerate)
            
            
            for i in range(len(firstCurrentBoard)):
                for j in range(len(firstCurrentBoard[i])):
                    if firstCurrentBoard[i][j]==0 and indexForRandoms<6:
                        firstCurrentBoard[i][j] = int(numbersForFirstBoard[indexForRandoms])
                        indexForRandoms+=1
                        
            found = isSolution(firstCurrentBoard,firstFinalBoard)
            if found==False:
                print(firstCurrentBoard)
                firstCurrentBoard = [[3,0,0,2],
                                     [0,1,4,0],
                                     [1,2,0,4],
                                     [0,3,2,1]]
                numberOfAttempts-=1
            
            
        if found == True:
            print("solution found with random numbers:!\n")
            print(numbersForFirstBoard)
            
            
    else:
        
        while numberOfAttempts>0 and found==False :
        
            #print("New Attempt:")
            
            indexForRandoms=0
            numbersForSecondBoard = generateRandomNumbers(1,10,secondNumbersToGenerate)
            
            
            for i in range(len(secondCurrentBoard)):
                for j in range(len(secondCurrentBoard[i])):
                    if secondCurrentBoard[i][j]==0 and indexForRandoms<45:
                        secondCurrentBoard[i][j] = int(numbersForSecondBoard[indexForRandoms])
                        indexForRandoms+=1
                        
            found = isSolution(secondCurrentBoard,secondFinalBoard)
            if found==False:
                #print(secondCurrentBoard)
                secondCurrentBoard = [[0,2,0,6,0,8,0,0,5],
                                      [5,8,0,0,0,9,7,0,0],
                                      [0,0,7,0,4,0,0,2,8],
                                      [3,7,0,4,0,1,5,0,0],
                                      [6,0,0,0,8,0,0,0,5],
                                      [0,0,8,0,0,2,0,1,3],
                                      [8,0,6,0,2,0,1,0,0],
                                      [0,0,9,8,0,0,0,3,6],
                                      [7,0,0,3,0,6,0,9,0]]
                numberOfAttempts-=1
            
            
        if found == True:
            print("solution found with random numbers:!\n")
            print(numbersForSecondBoard)
            
        
            

    
    
    
    
    
    
    
    
    