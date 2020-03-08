# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 14:48:30 2020

@author: Rares2
"""

from sudoku import main1
from cryptarithmetic import main2
from figures import main3


def main():
    
    choice=-1
    
    while(choice!=0):
    
        
        print("1.Sudoku")
        print("2.Cryptarithmetic")
        print("3.Figures")
        print("0.exit")
        
        choice = int(input("Select problem:"))
        
        
        
        if(choice==1):
            numberOfAttempts = int(input("Select number of attempts"))
            main1(numberOfAttempts)
        elif(choice==2):
            numberOfAttempts = int(input("Select number of attempts"))
            main2(numberOfAttempts)
        elif(choice==3):
            numberOfAttempts = int(input("Select number of attempts"))
            main3(numberOfAttempts)
        else:
            break;
            
main()
        
        
    
    