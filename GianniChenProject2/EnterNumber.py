'''
Created on Apr 9, 2016

@author: Gianni
'''
import re

# Functions

def getAverage(aList):
    'prints the average of the list'
    
    n = len(aList)
    total = 0
    for element in aList:
        total += element
    
    print ('The average is: ')
    print (total/n)

def getLargest(aList):
    'prints the largest number in the list'
    
    big = 0
    for element in aList:
        if (element > big):
            big = element
    
    print ('The largest number is: ')
    print (big)

def getSmallest(aList):
    'prints the smallest number in the list'
    
    small = aList[0]
    for element in aList:
        if (element < small):
            small = element
    
    print ('The smallest number is: ')
    print (small)

def isOrdered(aList):
    'prints whether the list is sorted or not'
    
    sortedList = []
    for element in aList:
        sortedList.append(element)
    sortedList.sort()
    
    reverseSort = []
    for element in sortedList:
        reverseSort.append(element)
    reverseSort.reverse()
    
    if (aList == sortedList):
        print ('The list is sorted in ascending order')
    elif(aList == reverseSort):
        print ('The list is sorted in descending order')
    else:
        print ('The list is not sorted at all')
    
# Main part of the program

print('Welcome to the Number Analyzer Program')
inputList = [int(x) for x in re.split(', |,', input('Please input a list of 5 numbers separated by commas: '))]
print ('You have entered the following list: ')
print (inputList)

getAverage(inputList)
getLargest(inputList)
getSmallest(inputList)
isOrdered(inputList)