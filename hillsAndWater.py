import time

from random import seed
from random import random

def current_milli_time():
    return round(time.time() * 1000)
   
seed(current_milli_time())

width=120
height=50
hill=[]

def generateHills():
    for y in range(0,height):
        for x in range(0,width):
            if y==0:
                hill.append(1)
            else:
                if random()>0.25 and hill[len(hill)-width]==1:
                    hill.append(1)
                else:
                    hill.append(0)
               
def printLinesInHills():
    for y in range(height,0,-1):
        print(getLine(width, y, hill))
   
def getLine(width, lineNumber, arr):
    startIndex = (lineNumber-1)*width
    returnString =''
    for x in range(startIndex,startIndex+width):
        if arr[x]==1:
            returnString = returnString + '#'
        else:
            returnString = returnString + '.'
    return returnString

def printWaterInHills():
    for y in range(height,0,-1):
        lineArray = list(getLine(width, y, hill))
        waterLine = ''

        for x in range(0,width):
            if lineArray[x]=='.' and isBoundedLeftAndRight(x, lineArray):
                waterLine = waterLine + '~'
            elif lineArray[x]=='#':
                waterLine = waterLine + '#'
            else:    
                waterLine = waterLine + ' '
        print(waterLine)

def isBoundedLeftAndRight(pos, lineArray):
    isBoundedLeft = False
    for i in range(pos, -1, -1):
        if lineArray[i]=="#":
            isBoundedLeft = True
           
    isBoundedRight = False
    for i in range(pos, width):
        if lineArray[i]=="#":
            isBoundedRight = True
   
    return (isBoundedLeft and isBoundedRight)        

if __name__ == "__main__":
    print("This prints out water (-) that could be stored in some random hills:")
    generateHills()
#    printLinesInHills()
    printWaterInHills()
