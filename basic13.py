#the basic 13 in Python
#print 1 to 255
"""
def print1to255():
    for i in range(1,256)
        print i

print1to255()


def printOdds1to255():
    for i range(1,256)
        if i % 2 == 0:
            print i

printOdds1to255



def printIntsAndSum0to255():
    var sum = 0
    for i in range(0,256)
        sum += i
        print i, sum

printIntsAndSum0to255()


def printArray(arr):
    for i in range(0,len(array)):
        print i


def printArray(arr):
    for val in arr:
        print val

def findAndPrintMax(array):
    max = array[0]
    for in range(1,len(array)):
        if array[i] > max:
            max = array[i]
    print max 



def getAndPrintAverage(array):
    sum = 0
    for in range (0,len(array)):
        sum +=array[i]
    print sum/len(array)

      
def arrayWithOdds():
    list = []
    for i in range(1,256):
        if i%2 != 0
            list.append(i)
    print list 

squareTheValue(array):
    for i in range(0,len(array)):
        array[i] = array[i]*array[i]
    print array

def greatherThanY(array, y):
    count = 0
    for i in range(0,len(array)):
        if array[i] > y:
            count +=1
    print count 

def zeroOutNegativeNumbers(array):
    for i in range (0, len(array)):
        if array[i] == 0:
            array[i] = 0
    print array

def MaxMinAvg(array):
    max = array[0]
    min = array[0]
    sum = 0

def shiftArrayValues(array):
    for i in range (0,len(array)-1):
        array[i] = array[i+1]
    array[len(array)-1] = 0
"""
def swapStringForArrayNegativeValues(array):
    for i in range (0, len(array)):
        if array[i] < 0:
            array[i] = "Dojo"
    print array

arr = [1,2,4,-9,-10,2]
swapStringForArrayNegativeValues(arr)