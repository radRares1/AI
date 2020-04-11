# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 21:56:37 2020

@author: Rares2
"""

from individ import Individ
from Repo import Repo
from random import randint,choice
import random
import operator
from sys import exit

class Controller:
    
    def __init__(self,repo):
        self.__repo = repo
        self.__repo.populate()
        self.__scores = {}
        self.__found = False
        self.__currentSolution = []
        self.__n = repo.getN()
        
        
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
    
    def getCurrentSolution(self):
        return self.__currentSolution
        
        
    def getPopulation(self):
        return self.__repo.getPopulation()
    
    def crossOver(self):
        
        
        population = self.getPopulation()
        
        newPopulation = []
        
        for i in range(0,len(population)//2):
            newIndivid1 = Individ(population[0].getSize())
            newIndivid2 = Individ(population[0].getSize())
            first = population[i].getIndivid()
            second = population[i+1].getIndivid()
            
            if(len(first) == 3):
                firstNew = []
                secondNew = []
                
                firstNew.append(second[2])
                firstNew.append(first[1])
                firstNew.append(second[0])
                
                secondNew.append(first[2])
                secondNew.append(second[1])
                secondNew.append(first[0])
                
                newIndivid1.setIndivid(firstNew)
                newIndivid2.setIndivid(secondNew)
                
                newPopulation.append(newIndivid1)
                newPopulation.append(newIndivid2)
                
            if(len(first) == 4):
                firstNew = []
                secondNew = []
                
                firstNew.append(second[3])
                firstNew.append(second[1])
                firstNew.append(second[2])
                firstNew.append(second[0])
                
                secondNew.append(first[3])
                secondNew.append(first[1])
                secondNew.append(first[2])
                secondNew.append(first[2])
                
                newIndivid1.setIndivid(firstNew)
                newIndivid2.setIndivid(secondNew)
                
                newPopulation.append(newIndivid1)
                newPopulation.append(newIndivid2)
                
            if(len(first) == 5):
                firstNew = []
                secondNew = []
                
                firstNew.append(second[0])
                firstNew.append(second[2])
                firstNew.append(second[1])
                firstNew.append(second[4])
                firstNew.append(second[3])
                
                secondNew.append(first[0])
                secondNew.append(first[2])
                secondNew.append(first[1])
                secondNew.append(first[4])
                secondNew.append(first[3])
                
                newIndivid1.setIndivid(firstNew)
                newIndivid2.setIndivid(secondNew)
                
                newPopulation.append(newIndivid1)
                newPopulation.append(newIndivid2)

  
                
        self.__repo.setPopulation(newPopulation)
        
        
    def mutation(self):
        
        if(self.__repo.getSize()==0):
            print("final sol")
            for item in self.__currentSolution.getIndivid():
                print(item)
            exit()
         
        population = self.getPopulation()
        
        sizePop = self.__repo.getSize()
        
        size = self.__repo.getN()
        
        randomChanges = randint(1,sizePop)
        
        #for i in range(0,randomChanges//4):

        randomRow = randint(0,size-1)
        randomRow2 = randint(0,size-1)
        randomCol = randint(0,size-1)
        randomCol2 = randint(0,size-1)
       
        randomIndivid = choice(population)
        values = randomIndivid.getIndivid()
        
      
        aux =  values[randomRow][randomCol]
        values[randomRow][randomCol] = values[randomRow2][randomCol2]
        values[randomRow2][randomCol2] = aux
    
    
        randomIndivid.setIndivid(values)
        
        
   
    

    #TODO           
    #mapez la fiecare permutare 0, si dupa cresc de fiecare data cand dau de ea in matrice
	#scoru individului ii suma de dubluri
	#daca am dat de 1 pt fiecare parte din permutare atunci scoru ii 0 matricea ii valida am gatat sarumana        
    def setScores(self):
        score = 0
        population = self.getPopulation()
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
            
            
    def getScores(self):
        return self.__scores
    
    def selectTheBest(self):
        
        x = self.__scores
        a = dict(sorted(x.items(), key=operator.itemgetter(1)))
        
        size = self.__repo.getSize()
        newGeneration = []
        
        
        #IT WORKS FOR 3 AS THIS CURRENT STATE OF THE APP
        #MODIFY DOWN HERE TO INCLUDE MORE POTENTIAL SOLUTIONS 
        counter=0
        for item in a.items():
            counter+=1
            if item[1] == min(a.values()):
                self.__currentSolution = item[0]
                self.isSolution()
                newGeneration.append(item[0])
                continue
            
            if counter < size//2:
                newGeneration.append(item[0])
                
                
        
   
 
            
        self.__repo.setPopulation(newGeneration)
        
        
        
class PSO:
    
    
    def __init__(self, popSize, neighSize,n, w, c1, c2):
        self.__repo=Repo(n, popSize)
        self.__repo.populate()
        self.__pop = self.__repo.getPopulation()
        print(len(self.__pop))
        self.computePersonalBest()
        self.__repo.splitNeighbours()
        self.__neigh = self.__repo.getNeigh()
        self.__popSize = popSize
        self.__neighSize = neighSize
        self.__w=w
        self.__c1=c1
        self.__c2=c2
        
        
    def computePersonalBest(self):
        for item in self.__pop:
            item.setScore()
            
    def computeBestNeigh(self):
        
        for hood in self.__neigh:
            min = 99999
            best = 0
            for individ in hood:
                if individ.getPersonalBest() < min:
                    min = individ.getPersonalBest()
                    best = individ
            
            for individ in hood:
                individ.setBestNeigh(best)
                

    def getPop(self):
        return self.__pop

 
    
    def getBestNeighbors(self, hoods):
        best=[]
        for item in hoods:
            best.append(item[0].getBestNeigh())
        return best
    
    def getDistance(part1, part2):
        p1 = list(part1)
        p2 = list(part2)
        n=len(p1)
        dist=0
        for i in range(n):
            dist+=abs(p1[i]-p2[i])
        return dist
    
    
    def updateVelocity(self, best):
        population = self.__pop
        for i in range(len(population)):
            for j in range(len(population[0].getVelocity())):
                newVelocity = self.__w * population[i].getVelocity()[j]
                newVelocity = newVelocity + self.__c1*random.random()*self.getDistance(population[best[i]].getIndivid()[j],population[i].getIndivid()[j])
                newVelocity=  newVelocity + self.__c2*random.random()*self.getDistance(population[i].getBestNeigh()[j], population[i].getIndivid()[j])
                current = population[i].getVelocity().copy()
                current[j]=newVelocity
                population[i].setVelocity(current)
        
    def updatePosition(self, best):
        population=self.__pop
        for i in range(len(population)):
            new=[]
            for j in range(len(population[0].getVelocity())):
                if random.random() < population[i].getVelocity()[j]:
                    new.append(population[best[i]].getBestNeigh()[j])
                else:
                    new.append(population[i].getIndivid()[j])
            population[i].setIndivid(new)
            
                 
    def iteration(self):
        bestNeighbors = self.getBestNeighbors(self.__neigh)
        self.updateVelocity(bestNeighbors)
        self.updatePosition(bestNeighbors)
        scores=[]
        for individ in self.__pop:
            scores.append(individ.getPersonalBest())
        

                
 
        
        
            

            
        