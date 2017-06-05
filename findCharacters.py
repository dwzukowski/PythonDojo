#we declare a function called findCharacter which takes two parameters, list and a string 
def findCharacters(list, string):
    #we declare a variable called new_list which is an empty list
    new_list = []
    #we instantiate a for loop which begins at zero and ends at the end of the list
    for i in range(0, len(list)):
        #using the .find method, we determine if string is present in each list item; if it is we append it to new_list
        if list[i].find(string) >=0:
            new_list.append(list[i])
    print new_list

word_list = ['hello','world','my','name','is','Anna']
findCharacters(word_list, "o")



#print word_list[0]
#print word_list[0].find("hello")

"""
1) loop through each word in list
2) use .find method on each index; returns -1 if none found; if >= 0 append this index to new list
3) return newList

Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.

Here's an example:

# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
new_list = ['hello','world']
Copy
Hint: how many loops will you need to complete this task?

"""