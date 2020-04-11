# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 21:58:22 2020

@author: Rares2
"""

from individ import Individ

class Repo:
    
    def __init__(self,n,no):
        self.__no = no
        self.__n = n
        self.__population = []
        self.__neigh = []
        
    def populate(self):
        for i in range(self.__no):
            new = Individ(self.__n)
            self.__population.append(new)
            
            
    def getPopulation(self):
        return self.__population
    
    def getSize(self):
        return len(self.__population)
    
    def getN(self):
        return self.__n;
    
    def setPopulation(self,p):
        self.__population = p.copy()
        
        
    def splitNeighbours(self):
        pop = self.__population
        while len(pop)>0:
            
            neigh = []
            for i in range(4):
                if len(pop) > 0:
                    neigh.append(pop[0])
                    pop.pop(0)
            self.__neigh.append(neigh)
            
    def getNeigh(self):
        return self.__neigh
            
        