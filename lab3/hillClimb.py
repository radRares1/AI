# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 21:10:05 2020

@author: Rares2
"""

from individ import Individ
from random import randint
from itertools import combinations,product
import operator
class HillController:
    
    def __init__(self,repo):
        self.__repo = repo
        self.__scores = {}
        self.__found = False
        self.__currentSolution = Individ(self.__repo.getN())
        self.__n = repo.getN()
        self.__generation = []
        list1 = []
        for i in range(1,self.__n+1):
            list1.append(i)
            
        self.__perms = list(product(list1, repeat=2))
        
    def getCurrentSolution(self):
        return self.__currentSolution
        
    def isFound(self):
        return self.__found
    
    def isSolution(self):
        s = self.__currentSolution.getIndivid()
        size = self.__currentSolution.getSize()
        ok = True
         
        for column in range(0,size):
            if ok == False:
                    break
            for i in range(size-1):
                if ok == False:
                    break
                for j in range(i+1,size):
                    if s[i][column][0] == s[j][column][0]:
                        ok = False
                        break
                    if s[i][column][1] == s[j][column][1]:
                        ok = False
                        
        for row in range(0,size):
            if ok == False:
                    break
            for i in range(size-1):
                if ok == False:
                    break
                for j in range(i+1,size):
                    if s[row][i][0] == s[row][j][0]:
                        ok = False
                        break
                    if s[row][i][1] == s[row][j][1]:
                        ok = False
                     
        self.__found = ok         
    
    
    def generateSolutions(self):
        
        randomRow = randint(0,self.__n-1)
        newGen = []
        
        newIndivid = Individ(self.__n)
        
        
        for perm in list(combinations(self.__perms,3)):
            sol = self.__currentSolution.getIndivid()
            
            sol[0] = list(perm).copy()
            '''
            for item in sol:
                print(item)
            print("new")
            '''
            newIndivid.setIndivid(sol)
            newGen.append(newIndivid)
     
            
        self.__generation = newGen.copy()
            
    
    def setScores(self):
        score = 0
        population = self.__generation
        self.__scores = {}
        
        
        for item in population:
            score=0
            duplicates = {str((1,1)):-1,str((1,2)):-1,str((1,3)):-1,str((1,4)):-1,str((1,5)):-1,str((2,1)):-1,str((2,2)):-1,str((2,3)):-1,str((2,4)):-1,str((2,5)):-1,str((3,1)):-1,str((3,2)):-1,str((3,3)):-1,str((3,4)):-1,str((3,5)):-1,str((4,1)):-1,str((4,2)):-1,str((4,3)):-1,str((4,4)):-1,str((4,5)):-1,str((5,1)):-1,str((5,2)):-1,str((5,3)):-1,str((5,4)):-1,str((5,5)):-1}

            for row in item.getIndivid():
                for i in range(len(row)):
                        duplicates[str(row[i])]+=1
                         
            
            values = list(duplicates.values())
            
            for v in values:
                if v>0:
                    score+=v
           
            self.__scores[item] = score
            
            
        
        
    def selectTheBest(self):
        
        x = self.__scores
        a = dict(sorted(x.items(), key=operator.itemgetter(1)))
        
        print(list(a.values())[0])
        
        self.__currentSolution = list(a.keys())[0]
        self.isSolution()
        
        
        
        
        
        
        
        
        
        
        
        