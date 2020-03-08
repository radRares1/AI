# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 13:12:59 2020

@author: Rares2
"""

"""
Representation:
    We use a dictionary to keep the words mapped as LETTER-RANDOM NUMBER
    
Description:
    We generate for each letter present in the words a random number from 0-15
    Then we map in the dictionaries for each letter the generated random number
    We perform the carry addition of each letter of the first two letters then check if the result is the same as the 
    third word
    If they match we print the word and the hexa code associated
    
"""


import numpy as np

def generateRandomNumber(high,low):
    randomNumberUniform = np.random.uniform(low,high)
    #print(randomNumbersUniform)
    return randomNumberUniform

def generateLetters(words):
    lettersDictionary = {}
    for word in words:
        for letter in list(word):
            lettersDictionary[letter] = int(generateRandomNumber(0,16))
            
    return lettersDictionary

def populateWordDictionary(word,letterDict):
    auxDictionary = {}
    for letter in list(word):
        auxDictionary[letter] = letterDict[letter]
        
    return auxDictionary

def computeResult(first,second,letters):
    auxDict = {}
    firstValues = list(first.values())
    firstValues.reverse()
    secondValues = list(second.values())
    secondValues.reverse()
    auxList = []
    
    carry=0
    """
    so check which of them have the longest length, put empty data in the auxDict respectively with the max val
    
    and append the one that remains with the last carry

    """
    
    if(len(firstValues)<=len(secondValues)):
        min=len(firstValues)
    else:
        min=len(secondValues)

    for i in range(min):
        a=firstValues[i]
        b=secondValues[i]
        if(a+b+carry > 16):
            r=(a+b+carry)%16
            carry=(a+b+carry)//16
        else:
            r=a+b+carry
            carry=0
         
        
        auxList.append(r)
    
        
    if(carry!=0):
        auxList.append(carry)
        
    auxList.reverse()
    
    for letter,number in letters.items():
        for no in auxList:
            if(no==number):
                auxDict[letter] = number
                
    return auxDict
            
    
def isSolution(d1,d2):
    return d1==d2

def main2(numberOfAttempts):
    
    
        
    words = [line.rstrip('\n') for line in open("C:\\Users\\Rares2\\.spyder-py3\\words.txt")]
    
    print(words)
    
    firstWord = words[0]
    secondWord= words[1]
    resultWord = words[2]
    
    lettersDictionary = {}
    firstDictionary = {}
    secondDictionary = {}
    thirdDictionary = {}
    resultDictionary = {}
    
    
    while(numberOfAttempts > 0):
        ok=False
        
        while ok==False:
            lettersDictionary = generateLetters(words).copy()
            firstDictionary = populateWordDictionary(firstWord,lettersDictionary).copy()
            secondDictionary = populateWordDictionary(secondWord,lettersDictionary).copy()
            thirdDictionary = populateWordDictionary(resultWord,lettersDictionary).copy()
            
            if(firstDictionary[list(firstDictionary.keys())[0]] == 0 or list(secondDictionary.keys())[0]==0 or list(thirdDictionary.keys())[0] == 0):
                ok=False
            else:
                ok=True
                
        
    
        resultDictionary = computeResult(firstDictionary,secondDictionary,lettersDictionary).copy()
         
        print(resultDictionary)
        
        if(isSolution(resultDictionary,thirdDictionary)==True):
            print("Solution found:")
            a = ''.join(str(resultDictionary[x]) for x in sorted(resultDictionary))
            print(hex(int(a)))
        
        else:
            print("Solution not found")
        
        numberOfAttempts-=1

    

        
    
    
