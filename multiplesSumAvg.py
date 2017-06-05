#we declare a function called avgList
def avgList(list):
    #we declare a variable called total with initial value zero
    total = 0
    #we instantiate a for loop which iterates through all values in a list
    for val in list:
        total += val
    #we print total divided by the length of the list which gives us the average
    print total/len(list)
a = [1, 2, 5, 10, 255, 3]
avgList(a)
"""
Assignment: Multiples, Sum, Average
This assignment has several parts. All of your code should be in one file that is well commented to indicate what each block of code is doing and which problem you are solving. Don't forget to test your code as you go!

Multiples
Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.

#we declare a fuction which has no parameters
def printOdds1to1000():
    #we instantiate a for loop begining at 1 and ending at 1000 
    for i in range(1,1001):
        #using an if statement, we check if i is odd
        if i % 2 != 0:
            print i 
printOdds1to1000()


Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.

#we decalre a function called multiples5toMillion which takes no pararmeters
def multiples5toMillion():
    #we instantiate a for loop which starts at 5 and ends at 1 million 
    for i in range (5, 1000001):
        #Using the condition statement if, we check if i is a multiple of 5
        if i%5 == 0: 
            print i
multiples5toMillion()


Sum List
Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]

#we declare a function called sumList
def sumList(list):
    #we declare a variable called total with initial value zero
    total = 0
    #we instantiate a for loop which iterates through all values in a list
    for val in list:
        total += val
    print total
a = [1, 2, 5, 10, 255, 3]
sumList(a)

Average List
Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]

"""