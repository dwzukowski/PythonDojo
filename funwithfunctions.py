def multiply(list, num):
    newList = []
    for val in list:
        newList.append(val*num)
    return newList

#we declare a function called layered_multiples which takes one parameter arr
def layered_multiples(arr):
    #we declare a variable called new_array which is an empty list
    new_array = []
    #we instantiate a for loop which iterates through all values in arr
    for val in arr:
        #we append a list of 1s equal to val in each coresponding index of new_arr
        new_array.append([1]*val)
    print new_array

layered_multiples(multiply([2,4,5],3))

"""
Hacker Challenge:
Write a function that takes the multiply function call as an argument. Your new function should return the multiplied list as a two-dimensional list. Each internal list should contain the number of 1's as the number in the original list. Here's an example:

def layered_multiples(arr)
  # your code here
  return new_array
x = layered_multiples(multiply([2,4,5],3))
print x
# output
>>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]



Create a series of functions based on the below descriptions.

Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.

The function should multiply each value in the list by the second argument. For example, let's say:




#We declare a function called odd_even that takes no parameters
def odd_even():
    #We instantiate a for loop beginning at 1 and ending after 2000 
    for i in range(1,2001):
        #Using the condition expression if, we check if the number is even or odd
        if i % 2 == 0:
            print "The number is " +str(i) + ". This is an even number"
        else:
            print "The number is " +str(i) +  ". This is an odd number" 
odd_even()

Odd/Even:
Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.



"""