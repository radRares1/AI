# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 14:24:34 2020

@author: Rares2
"""

from decimal import Decimal
import random



def f(x1,x2,x3,x4,x5,b1,b2,b3,b4,b5):
    return b1*x1+b2*x2+b3*x3+b4*x4+x5*b5


if __name__== "__main__":
    
    file = open("db.txt","r")
    
    lines = file.readlines()
    
    data = []
    for line in lines:
        if line != "\n":
            a = line.split(" ")
            newList = []
            for item in a:
                if item != "\n":
                    newList.append(float(item))
            data.append(newList)
    
    
    bestMin=9999
    bb1=9999
    bb2=9999
    bb3=9999
    bb4=9999
    bb5=9999

    b1=random.randint(-40, 40)
    b2=random.randint(-40, 40)
    b3=random.randint(-40, 40)
    b4=random.randint(-40, 40)
    b5=random.randint(-40, 40)
    
    rate = 0.1
    for current in data:
        
        #x's
        
        x1=current[0]
        x2=current[1]
        x3=current[2]
        x4=current[3]
        x5=current[4]
        
        #value of the function
        
        total=current[5]
        
        #the gradients of each attribute
        #since we have a linear function, and we differentiate w.r.t one attribute at the time
        #the other attributes will be 0
        
        d1=x1*b1
        d2=x2*b2
        d3=x3*b3
        d4=x4*b4
        d5=x5*b5
        
        #we compute the new coefficents at once
        #we do this to work with the old coefficients not the new ones
        
        temp1 = round(b1-rate*d1, 2)
        temp2 = round(b2-rate*d2, 2)
        temp3 = round(b3-rate*d3, 2)
        temp4 = round(b4-rate*d4, 2)
        temp5 = round(b5-rate*d5, 2)
        
        #and now we assign the new coefficents to the actual coefficents
        
        b1 = temp1
        b2 = temp2
        b3 = temp3
        b4 = temp4
        b5 = temp5
        
        currentValue = f(x1,x2,x3,x4,x5,b1,b2,b3,b4,b5)
        
        
        h = total-currentValue
       
        if h < bestMin:
            bestMin = total-currentValue
            bb1=b1
            bb2=b2
            bb3=b3
            bb4=b4
            bb5=b5
        
        
    print("the local minimum is found with the coefficients: ")
    print(bb1,bb2,bb3,bb4,bb5)
        
        
        
        
        
        
        
        
        
        
        
