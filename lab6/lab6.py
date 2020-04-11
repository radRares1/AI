# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 10:58:31 2020

@author: Rares2
"""
from helperClasses import *
import operator

#lab6 decision trees

def partition(rows,question):
    """
    splits the data set into paritions
    we split the data by answering the question(i.e: >=3)
    """
    trueRows = []
    falseRows = []
    for row in rows:
        if question.answer(row):
            trueRows.append(row)
        else:
            falseRows.append(row)
            
    return trueRows,falseRows

def giniIndex(rows):
    """
    get the giniIndex for a list of rows
    """
    stats = classCounts(rows)
    impurity = -1
    for label in stats:
        labelProb = stats[label] / float(len(rows))
        impurity -= labelProb**2
    return impurity

def infoGain(left,right,currentUncertainty):
    """
    uncertainty of starting node - weighted avg impourity of
    child nodes
    """
    
    weight = float(len(left)) / (len(left) + len(right))
    
    return currentUncertainty - weight*giniIndex(left) - (1-weight)*giniIndex(right)

def getBestSplit(rows):
    """
    get the best question by calculating the info gain of
    all values of each attribute
    """
    bestGain = 0
    bestQuestion= None
    
    currentUncertainty = giniIndex(rows)
    
    for attribute in range(1,len(rows[0])):
        
        values = set([row[attribute] for row in rows]) 
        
        
        for value in values:
            
            
            question = Question(attribute,value)
            
            
            trueRows,falseRows = partition(rows,question)
            
            #skip it if it won;t split
            if len(trueRows) == 0 or len(falseRows) ==0:
                continue
            
            #get the info gain of this split
            
            gain = infoGain(trueRows,falseRows,currentUncertainty)
    
            print(gain)
            
            #update the bestGain if better
            
            if gain >= bestGain:
                bestGain,bestQuestion = gain,question
    
    return bestGain,bestQuestion

def makeTree(rows):
    """
    we build the tree using recursion
    we perform the partitioning,
    get the info gain for each,
    return the question with the best gain
    """
    
    gain,question = getBestSplit(rows)
    
    #we stop if the gain is 0
    if gain == 0:
        print("yes")
        return Leaf(rows)
    
    #partition the data by answer to the question
    trueRows,falseRows = partition(rows,question)
    
    #start recursion for true and false child-trees
    trueBranch = makeTree(trueRows)
    
    falseBranch = makeTree(falseRows)
    
    return DecisionNode(question,trueBranch,falseBranch)
    
def printTree(node,string= ""):
    
    if isinstance(node,Leaf):
        print(string + "prediction:",  node.predictions)
        return
    
    print(string + str(node.question))
    
    print(string + "True branch:")
    printTree(node.trueSide, string+ " ")
    
    print("\n")
    
    print(string + "False branch:")
    printTree(node.falseSide, string+ " ")  
    
def classification(row,node):
    """
    again we go recurssively through the built tree
    """
    
    if isinstance(node,Leaf):
        return node.predictions
    
    #answer the question and go on the asociated branch
    
    if node.question.answer(row):
        return classification(row,node.trueSide)
    else:
        return classification(row,node.falseSide)


def main():
    
    file = open("balance-scale.data","r")
    
    lines = file.readlines()
    
    data = []
    
    for line in lines:
        newList = []
        for item in line:
            if item!= "," and item!="\n":
                newList.append(item)
        data.append(newList)
        
    tree = makeTree(data)
    
    printTree(tree)
    
    goodB=0
    goodR=0
    goodL=0
    
    for row in data:
        d = printLeaf(classification(row, tree))
        print ("Actual: %s. Predicted: %s" %(row[0],d))
           
         
        letter = max(d.items(), key=operator.itemgetter(1))[0]
         
        if row[0] == letter and row[0]=='L':
            goodL+=1
            
        if row[0] == letter and row[0]=='B':
            goodB+=1
            
        if row[0] == letter and row[0]=='R':
            goodR+=1
    
    print("\nit got right:\n")   
    print(goodL,"out of 288 left")     
    print(goodB,"out of 49 balanced")
    print(goodL,"out of 288 right\n")
    
    print("the ones left are just not predicted right")
    
main()