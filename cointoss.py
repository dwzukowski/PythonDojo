#we declare a function called cointoss which take no parameters
def cointoss():
    #we declare variables to count the number of heads and tails
    heads_count = 0
    tails_count=0
    #we instantiate a for loop begining at 1 and ending after 5000
    for i in range(1,5001):
        #we use the python random module and random.choice function to choose randomly from a seqence 0 or 1.  
        import random
        toss= random.choice([0,1])
        #using the conditional expression if, we determine whether the toss is a heads or tails, increment the associated counting variable, and print the result
        if toss == 1:
            heads_count+= 1 
            print "Attempt #{}: Throwing a coin... It's a heads! Got {} head(s) and {} tail(s) so far".format(i, heads_count, tails_count)
        else:
            tails_count+= 1
            print "Attempt #{}Throwing a coin... It's a tails! Got {} tails(s) and {} heads(s) so far".format(i, tails_count, heads_count)
cointoss()

"""

Assignment: Coin Tosses
Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.

Sample output should be like the following:

Starting the program...
Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
...
Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far
Ending the program, thank you!
Hint: Use the python built-in round function to convert that floating point number into an integer

x = .23945593
y = .798839238
x_rounded = round(x)
# x_rounded will be rounded down to 0
y_rounded = round(y)
# y_rounded will be rounded up to 1


import random

def toss(reps):
    # print new_toss
    attempt_count = 1
    head_count = 0
    tail_count = 0
    result = ""
    result_string_complete = ""

    for x in range(1, reps):
        new_toss = random.randint(0,1)
        if new_toss == 1:
            head_count += 1
            result = "head"
            print "Attempt #", attempt_count, ": Throwing a coin... It's a ", result, "! Got ", head_count, "head(s) so far and", tail_count, "tail(s) so far"
        else:
            tail_count += 1
            result = "tail"
            print "Attempt #", attempt_count, ": Throwing a coin... It's a ", result, "! Got ", head_count, "head(s) so far and", tail_count, "tail(s) so far"
        attempt_count += 1

toss(5001)
"""