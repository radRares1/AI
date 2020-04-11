# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:57:55 2020

@author: Rares2
"""
import random

class Individ:
    
       
        
   
    
    def generateValidRow(self):
        row = []
        remaining = self.__perms.copy()
        element = random.choice(remaining)
        row.append(element)
        remaining.remove(element)
        
        while len(row) < self.__n:
            ok = True
            element = random.choice(remaining)
            ok=True
            for item in row:
                if item[0] == element[0]:
                    remaining.remove(element)
                    ok=False
                    break
                elif item[1] == element[1]:
                    ok=False
                    remaining.remove(element)
                    break
                    
            if ok==True:
                row.append(element)
                remaining.remove(element)
                
            
        return row
                
    def __init__(self,n):
        self.__n = n;
        self.__perms = []
        list = range(1,n+1)
        for item in list:
            for jtem in list:
                self.__perms.append((item,jtem))
                
        self.__matrix = []
        for i in range(0,n):
            self.__matrix.append(self.generateValidRow())
        self.__personalBest = 0    
        self.__velocity = [0 for i in range(2*n)]
        self.__bestNeigh = 0
        
        
    def setScore(self):
        score = 0
        self.__scores = {}
        
        
        
        duplicates = {str((1,1)):-1,str((1,2)):-1,str((1,3)):-1,str((1,4)):-1,str((1,5)):-1,str((2,1)):-1,str((2,2)):-1,str((2,3)):-1,str((2,4)):-1,str((2,5)):-1,str((3,1)):-1,str((3,2)):-1,str((3,3)):-1,str((3,4)):-1,str((3,5)):-1,str((4,1)):-1,str((4,2)):-1,str((4,3)):-1,str((4,4)):-1,str((4,5)):-1,str((5,1)):-1,str((5,2)):-1,str((5,3)):-1,str((5,4)):-1,str((5,5)):-1}
    
        for row in self.getIndivid():
            for i in range(len(row)):
                    duplicates[str(row[i])]+=1
                     
        
        values = list(duplicates.values())
        
        for v in values:
            if v>0:
                score+=v 
       
        self.__personalBest = score
        
    def setPersonalBest(self,b):
        self.__personalBest = b;
        
    def getPersonalBest(self):
        return self.__personalBest
    
    def setVelocity(self,l):
        self.__velocity = l.copy()
        
    def getVelocity(self):
        return self.__velocity
    
    def getBestNeigh(self):
        return self.__bestNeigh
    
    def setBestNeigh(self,individ):
        self.__bestNeigh.setIndivid(individ.getIndivid())
            
    def toString(self):
        string = ""
        
        for row in self.__matrix:
            string += str(row) +"\n"
        return string
    
        
    def getIndivid(self):
        return self.__matrix
    
    def getSize(self):
        return self.__n
    
    def setIndivid(self,m):
        self.__matrix = m.copy()


