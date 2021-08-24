import time

from random import seed
from random import random

#Write a method that returns a sum of a list of input numbers
def calculateSum(intList):
    cumulativeTotal = 0
    for i in range(0, len(intList)):
        cumulativeTotal = cumulativeTotal + intList[i]
    return cumulativeTotal

#Write a method to calculate x! using a for loop    
def calculateFactorialUsingForLoop(x):
    runningTotal = 1
    for i in range(x,0,-1):
        runningTotal = runningTotal * i
    return runningTotal

#Write a method to calculate x! using a while loop    
def calculateFactorialUsingWhileLoop(x):
    runningTotal = 1
    i = x
    while i>0:
        runningTotal = runningTotal * i
        i-=1
    return runningTotal

#Write a method to calculate x! using recursion
def calculateFactorialUsingRecursion(x):
    if x == 1 or x==0:
       return 1    
    return x*calculateFactorialUsingRecursion(x-1)

#Write a method that accepts a list of strings and returns them sorted in increasing/decreasing length    
def getListOfLengthsAscending(arr):
    returnList = []
    currentShortestString = ''
    for i in range(len(arr)-1, -1, -1):
        for i in range(len(arr)-1, -1, -1):            
            if i==len(arr)-1:           
                currentShortestString = arr[i]                
            else:
                if len(arr[i])<len(currentShortestString):
                    currentShortestString = arr[i]
        arr.remove(currentShortestString)
        returnList.append(currentShortestString)
    return returnList

def getListOfLengthsDescending(arr):
    returnList = []
    currentLongestString = ''
    for i in range(len(arr)-1, -1, -1):
        for i in range(len(arr)-1, -1, -1):            
            if i==len(arr)-1:           
                currentLongestString = arr[i]                
            else:
                if len(arr[i])>len(currentLongestString):
                    currentLongestString = arr[i]
        arr.remove(currentLongestString)
        returnList.append(currentLongestString)
    return returnList

#Write a method that returns the mean of a list of numbers        
def calculateMeanOfList(arr):
    totalSum = 0
    for i in range(0,len(arr)):
        totalSum += arr[i]
        
    return totalSum/len(arr)

#Write a method that returns the median of a list of numbers        
def calculateMedianOfList(arr):
    sortedArr = sorted(arr)
    
    for i in range(0,len(sortedArr)):
        if len(sortedArr)%2==1 and (len(sortedArr)-1)/2==i: ##length is odd
            return sortedArr[i]
        elif len(sortedArr)%2==0 and (len(sortedArr)/2)-1==i:
            return (sortedArr[i] + sortedArr[i+1])/2
          
if __name__ == "__main__":
    assert calculateSum([1,2,3,4])==10, "FAILED"
    assert calculateSum([1,2,3,-4])==2, "FAILED"
    
    assert calculateFactorialUsingForLoop(0)==1, "FAILED"
    assert calculateFactorialUsingForLoop(1)==1, "FAILED"
    assert calculateFactorialUsingForLoop(2)==2, "FAILED"
    assert calculateFactorialUsingForLoop(3)==6, "FAILED"
    
    assert calculateFactorialUsingWhileLoop(0)==1, "FAILED"
    assert calculateFactorialUsingWhileLoop(1)==1, "FAILED"
    assert calculateFactorialUsingWhileLoop(2)==2, "FAILED"
    assert calculateFactorialUsingWhileLoop(3)==6, "FAILED"
   
    assert calculateFactorialUsingRecursion(0)==1, "FAILED"
    assert calculateFactorialUsingRecursion(1)==1, "FAILED"
    assert calculateFactorialUsingRecursion(2)==2, "FAILED"
    assert calculateFactorialUsingRecursion(3)==6, "FAILED"
    
    assert getListOfLengthsAscending(['aaaa','aa','aaa'])==['aa', 'aaa', 'aaaa'], "FAILED"
    assert getListOfLengthsAscending(['aaaa','a','aa','aa','aaa'])==['a','aa','aa', 'aaa', 'aaaa'], "FAILED"

    assert getListOfLengthsDescending(['aaaa','aa','aaa'])==['aaaa', 'aaa', 'aa'], "FAILED"
    assert getListOfLengthsDescending(['aaaa','a','aa','aa','aaa'])==['aaaa','aaa','aa', 'aa', 'a'], "FAILED"

    assert calculateMeanOfList([3,4,5,6,7])==5, "FAILED"   
    assert calculateMeanOfList([5,6,7,4])==5.5, "FAILED"
    
    assert calculateMedianOfList([4,5,18,7,-3])==5, "FAILED"   
    assert calculateMedianOfList([9,5,6,8])==7, "FAILED"
    
