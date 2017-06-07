def tupleToDict(dict):
    newList= []
    for key,val in dict.iteritems():
        temp = (key, val)
        print temp
        newList.append(temp)
        print newList

my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

tupleToDict(my_dict)

"""
Write a function that takes in a dictionary and returns a list of tuples where the first tuple item is the key and the second is the value. Here's an example:

# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#function output
[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]



x = 5
print x
print type(x)
print type(str(x))

"""