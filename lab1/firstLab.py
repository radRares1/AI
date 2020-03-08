# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 10:50:37 2020

@author: Rares2
"""


import numpy as np
import matplotlib.pyplot as plt

def main():
   
    choice=0
    
    print('1.Unifrom')
    print('2.Binomial')
    print('3.exit')
    choice=int(input('Choose a distribution:'))
    
    
    if choice==1:
          low=float(input('low: '))
          high=float(input('high: '))
          size=int(input('size: '))
          randomNumbersUniform = np.random.uniform(low,high,size)
          plt.plot(randomNumbersUniform,'ro')
    else:
        if choice==2:
            n=int(input('n: '))
            p=float(input('p: '))
            size=int(input('size: '))
            randomNumbersBinomial = np.random.binomial(n,p,size)
            plt.plot(randomNumbersBinomial,'bo')
                
        
        
        
        
        
    
    
    
    

# Main program starts here
main()