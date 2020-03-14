# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 19:10:43 2020

@author: Rares2
"""

from time import time
from copy import deepcopy

class Board:
    """
    the board of elements
    """
    def __init__(self,n):
        self.__size=n
        self.__board=[ [ 0 for i in range(self.__size) ] for j in range(self.__size) ] 
        
    def getSize(self):
        return self.__size
    
    def getBoard(self):
        return self.__board[:]
    
    def update(self,i,j):
        self.__board[i][j]=1

class State:
    """
    a possible state of the board
    having inside the board, the list of placed positions and their number
    """
    def __init__(self, board):
        self.__values = board
        self.__positions = []
        self.__counter = 0
        
    def setValues(self,newValues):
        self.__values = newValues[:]
        
    def getCounter(self):
        return self.__counter
    
    def getPositions(self):
        return self.__positions
        
    def getValues(self):
        return self.__values.getBoard()
    
    def toString(self):
        stateToString="";
        for row in self.__values.getBoard():
            stateToString+=str(row) +'\n'
            
        return stateToString
    
    def putOne(self,i,j):
        self.__counter+=1;
        self.__values.update(i,j)
        self.__positions.append([i,j])
        
class Problem:
    
    def __init__(self):
        self.__initialState = None
        
    
    def setInitial(self,newState):
        self.__initialState = newState
        
    def getInitial(self):
        return self.__initialState
        
    
    def expand(self, state):
        """
        for each empty place on the board we create a new possible state
        """
        empty = []
        currentState = state.getValues()
        
        for i in range(len(currentState)):
            for j in range(len(currentState)):
                if currentState[i][j]==0:
                    empty.append([i,j])
                    
        newStates = []
        for coords in empty:
            #i had here the problem that I created a new State with the same vals of state
            #instead of actually copying the given state
            #and it just couldn't find any sols
            newState = deepcopy(state)
            newState.putOne(coords[0],coords[1])
            newStates.append(newState)
            
        return newStates
    
    def maybeSol(self, state):
        """
        checks if there are more than one 1
        on the same rows and cols or on diagonal
        """
        
        #rows
        values=state.getValues()
        for row in values:
            if sum(row)>1:
                return False
            
        #cols
        for i in range(len(values)):
            s=0
            for j in range(len(values)):
                s+=values[j][i]
                if s > 1:
                    return False
                
        #diag
        firstDiag = [ row[i] for i,row in enumerate(values) ]
        if sum(firstDiag) > 1:
            return False
        
        secondDiag = [ row[-i-1] for i,row in enumerate(values) ]
        if sum(secondDiag) > 1:
            return False
        
        return True
        
    def isSolution(self,state):
        return (self.maybeSol(state) and len(state.getValues())==state.getCounter())
        
        
    def isAttacked(self,state,row,col):
        
        alreadyPlaced = state.getPositions()
        rowCoords = [coord[0] for coord in alreadyPlaced]
        colCoords = [coord[1] for coord in alreadyPlaced]
        
        #check if attacked from row or col
        if row in rowCoords or col in colCoords:
            return True
        
        #check if attacked from diagonal||tyInternet.jpg
        for coord in alreadyPlaced:
            attackRow = abs(coord[0]-row)
            attackCol = abs(coord[1]-col)
            if attackRow==attackCol:
                return True
            
        return False
    
    def badPos(self,state):
        values = state.getValues()
        counter=0
        
        for i  in range(len(values)):
            for j in range(len(values)):
                if values[i][j]==1 and self.isAttacked(state,i,j):
                    counter+=1
                    
        return counter
    
    def heuristic(self,state):
        
        score = 0
        
        if self.maybeSol(state) == False:
            return 1000
        
        values=state.getValues()
       
        
        for i in range(len(values)):
            for j in range(len(values)):
                if values[i][j]==0:
                    score+=1
        
        score = score-self.badPos(state)
        return score
    
    def readFile(self):
        with open('boardSize.txt','r') as f:
            size=int(f.readline())
        return size
    
class Controller:
    
    def __init__(self,problem):
        self.__problem = problem
        board=Board(problem.readFile())
        state = State(board)
        self.__problem.setInitial(state)
        
        
    def getProblem(self):
        return self.__problem
        
    def dfs(self, root):
        visited = []
        stack=[]
        stack.append(root)
        
        while len(stack) > 0:
            state = stack.pop()
            if self.__problem.isSolution(state):
                return state
            visited.append(state)
            if(self.__problem.maybeSol(state)):
                states = self.__problem.expand(state)
                
                for state in states:
                    if state not in visited:
                        stack.append(state)
                        
        return None
        
        
    def greedy(self,root):
        queue=[]
        queue.append(root)
        visited = []
        while len(queue)>0:
            state=queue.pop(0) 
            visited=visited+[state]
            if self.__problem.isSolution(state):
                return state
            if self.__problem.maybeSol(state):
                aux=[]
                states = self.__problem.expand(state)
                for state in states:
                    if state not in visited:
                        aux.append(state)
                aux = [(sol,self.__problem.heuristic(sol)) for sol in aux]
                aux.sort(key = lambda x:x[1])
                aux = [state[0] for state in aux]
                queue = [aux[0]]
                
        return None
            
class UI:
    def __init__(self,controller):
        self.__controller = controller
        
    def run(self):
        menu=""
        menu+="1.DFS\n"
        menu+="2.Greedy\n"
        menu+="0.Exit\n"
        
        print(menu)
        run=True
        while(run):
            choice=int(input("choice:"))
            if choice==0:
                run=False
            if choice == 1:
                self.dfs()
            if choice ==2:
                self.greedy()
                    
    def dfs(self):
        start = time()
        sol = self.__controller.dfs(self.__controller.getProblem().getInitial())
        if sol is None:
            print("No sol")
        else:
            print(sol.toString())
            
        print("it took: ", time()-start, "sec")
        
    def greedy(self):
        start = time()
        sol = self.__controller.greedy(self.__controller.getProblem().getInitial())
        if sol is None:
            print("No sol")
        else:
            print(sol.toString())
            
        print("it took: ", time()-start, "sec")
        
prob = Problem()
ctrl = Controller(prob)
Ui = UI(ctrl)
Ui.run()

    
    