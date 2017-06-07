user = {}
user["name"]="Dave"
user["age"]=31
user["country"]="United States"
user["language"]="JavaScript"
print user

user2 = {}
user2["name"]="Amanda"
user2["country"]="Spain"
user2["age"]=30
user2["language"]="Python"

def makedictionary(dict):
    print "my name is {}".format(dict["name"])
    print "my age is {}".format(dict["age"])
    print "my country of birth is {}".format(dict["country"])
    print "my favorite language is {}".format(dict["language"])

makedictionary(user)
makedictionary(user2)


"""
Create a dictionary containing some information about yourself. The keys should include name, age, country of birth, favorite language.

Write a function that will print something like the following as it executes:

My name is Anna
My age is 101
My country of birth is The United States
My favorite language is Python
Copy
There are two steps to this process, building a dictionary and then gathering all the data from it. Write a function that can take in and print out any dictionary keys and values.

Note: The majority of data we will manipulate as web developers will be hashed in a dictionary using key-value pairs. Repeat this assignment a few times to really get the hang of unpacking dictionaries, as it's a very common requirement of any web application.
"""