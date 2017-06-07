#we declare a function printstar that takes one paramter, list
def printstar(list):
    #we instantiate a for loop begining at 0 and iterating through all values in the list
    for val in list:
        #we use if conditional to output appropriate response based on datatype
        if isinstance(val, int) or isinstance(val, float):
            print "*"*val
        elif isinstance(val,str):
            #print "isinstance string OK"
            #print val  access first value of string by index, convert to lowercase and multiply by number of characters in the string 
            print val[0].lower()*len(val) 
printstar([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])
"""



Create a function called draw_stars() that takes a list of numbers and prints out *.

For example:

x = [4, 6, 1, 3, 5, 7, 25]
Copy
draw_stars(x)should print the following in when invoked:

****
******
*
***
*****
*******
*************************


Part II
Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. When a string is passed, instead of displaying *, display the first letter of the string according to the example below. You may use the .lower() string method for this part.

For example:

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
Copy
draw_stars(x) should print the following in the terminal:

****
ttt
*
mmmmmmm
*****
*******
jjjjjjjjjjj


Instructor solution:

def stars(arr):
    for x in arr:
        print "*" * x


nums = [6,2,5,7,9]
stars(nums)

def stars2(arr):
    for x in arr:
        if isinstance(x, int):
            print "*" * x
        elif isinstance(x, str):
            length = len(x)
            letter = x[0].lower()
            print letter * length

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
stars2(x)
"""
