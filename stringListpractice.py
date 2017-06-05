def splitNewList(list):
    tempList = []
    newList =[]
    #use sort to put list in ascending order
    list.sort()
    count = 0
    #instantiate a while loop begining at zero and ending halway through the list; append each value to tempList
    while count < len(list)/2:
        tempList.append(list[count])
        count +=1
    print tempList
    #insert templist at index zero of newList
    newList.insert(0, tempList)
    print newList
    #instantiate a for loop begining where our while loop above left off and ending at the end of the list; append the 2nd half of list to newList
    for i in range(count,len(list)):
        newList.append(list[i])
    print newList

x = [19,2,54,-2,7,12,98,32,10,-3,6]
splitNewList(x)

"""






Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!


insert(index, x)


s= "It's thanksgiving day. It's my birthday,too!"
print s.find('day')
newString = s.replace("day","month")
print newString


def firstLastNewList(list):
    newList= []
    newList.append(list[0])
    newList.append(list[len(list)-1])
    print newList
x = ["hello",2,54,-2,7,12,98,"world"]
firstLastNewList(x)

def minMax(array):
    min = array[0]
    max = array[0]
    for val in array:
        if val > max:
            max = val
        if val < min:
            min = val
    print min, max 
    
x = [2,54,-2,7,12,98]
minMax(x)
"""