# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:57:55 2020

@author: Rares2
"""
from itertools import permutations
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

                
            