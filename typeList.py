#we declare a function called typeList that takes one paramater, list
def typeList(list):
    newStr = ""
    sum = 0
    #instantiate a for loop 
    for i in range(0,len(list)):
        if isinstance(list[i], int):
            sum+=list[i] 
        elif isinstance(list[i], float):
            sum+=list[i]           
        elif isinstance(list[i], str):
            newStr+= (list[i])+" "
    print sum
    print newStr
x= ['magical unicorns',19,'hello',98.98,'world']
typeList(x)

"""
Write a program that takes a list and prints a message for each element in the list, based on that element's data type.

Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the array contains. If it contains only one type, print that type, otherwise, print 'mixed'.

Here are a couple of test cases. Think of some of your own, too. What kind of unexpected input could you get?
"""