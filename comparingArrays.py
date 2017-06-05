#we declare a function called compareArrays which takes two parameters, list one and list two
def compareArrays(list_one, list_two):
    #we delcare a variable answer which is string
    answer = ""
    #we compare the lengths of teh two lists; if they are not equal the list cannot be the same
    if len(list_one) != len(list_two):
        answer= "The lists are not the same"
    else:
        #we instantiate a for loop begining at zero and ending at the end of the list
        for i in range (0,len(list_one)):
            #we compare the value at each index of the list; we exit the loop the first time two indexes are not equal
            if list_one[i] != list_two[i]:
                answer= "The lists are not the same"
                break
            else:
                answer= "The lists are the same"
    print answer

list_one = ['celery','carrots','bread']
list_two = ['celery','carrots','bread',]
compareArrays(list_one, list_two)

"""
Write a program that compares two lists and prints a message depending on if the inputs are identical or not.

Your program should be able to accept and compare two lists: list_one and list_two. If both lists are identical print "The lists are the same". If they are not identical print "The lists are not the same." Try the following test cases for lists one and two:

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

"""