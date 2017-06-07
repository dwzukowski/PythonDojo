def listToDict(arr1, arr2):
    #one line solution
    #print dict(zip(arr1, arr2))
    new_dict = {}
    for i in range(0,len(arr1)):
        new_dict[arr1[i]]=arr2[i]
        print new_dict

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

listToDict(name,favorite_animal)

"""
Assignment: Making Dictionaries
Create a function that takes in two lists and creates a single dictionary where the first list contains keys and the second values. Assume the lists will be of equal length.

Your first function will take in two lists containing some strings. Here are two example lists:

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
Copy
Here's some help starting your function.

def make_dict(arr1, arr2):
  new_dict = {}
  # your code here
  return new_dict

  """