# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 22:06:06 2020

@author: Rares2
"""

from Controller import Controller,PSO
from Repo import Repo
from hillClimb import HillController



def main():
    

    print("1.EA")
    print("2.Hill")
    print("3.PSO")
    choice = int(input("Choose a method"))
    
    
    
    
    
    if choice == 1:
    
        n = int(input("Size of the chromosome: "))
        no = int(input("Size of initial population: "))
        number = int(input("How many generations do you want: "))
        repo = Repo(n,no)
        controller = Controller(repo)
         
        ok = controller.isFound()
        
        while number > 0 and ok==False: 
          
        
            #print(len(controller.getPopulation()))
            controller.crossOver()
            #for item in controller.getPopulation():
            #    print(item.toString())
            controller.mutation()
            #3print("mute")
           # for item in controller.getPopulation():
            #    print(item.toString())
            
            controller.setScores()
            controller.selectTheBest()
            #print(controller.getCurrentSolution().toString())
            ok = controller.isFound()
            if ok == True:
                print("true")
            number-=1
            
        
        print("the best found solution is: ")
        print(controller.getCurrentSolution().toString())
        
    elif choice == 2:
        
        n = int(input("Size of the chromosome: "))
        number = int(input("How many generations do you want: "))
        repo = Repo(n,no)
        controller = HillController(repo)
        ok=False
        while number > 0 and ok==False: 
            
            controller.generateSolutions()
            controller.setScores()
            controller.selectTheBest()
            
            ok = controller.isFound()
            number-=1
            
        print("the best found solution is: ")
        print(controller.getCurrentSolution().toString())
        
    elif choice == 3:
        noGen = 100
        popSize = 10
        indSize = 4
        best=0
        w=1.0
        c1=1.2
        c2=0.7
        neighbourhoodSize = 2
        fitnessList=[]
        trials = []
        trialCounter = 0
        ctrl = PSO(popSize,neighbourhoodSize,indSize,w,c1,c2)
        for i in range(noGen):
            ctrl.iteration()
        if trialCounter<30:
            
            print(len(ctrl.getPop()))
            
            fitnessList.append(ctrl.getPop()[0].getPersonalBest())
            trials.append(trialCounter)
            trialCounter+=1
        
        pop = ctrl.getPop()    
        for i in range(popSize):
            if(pop[i].getPersonalBest()<pop[best].getPersonalBest()):
                best = i
                
        print("Best so far:")
        print(pop[best])

    
    
    
    
        
        
main()