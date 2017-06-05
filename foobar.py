def isPrime(num):
    prime = True
    for i in range(2,num):
        if num % i == 0:
            prime = False
    return prime
def isPerfect(num):
    perfect = False
    #can stop searching at num/2 +1, no perfect square other than two is closer to num than num/2 
    for i in range (2, num/2+1):
        if i*i == num:
            perfect = True
    return perfect
def foobar():
    for i in range(100,100001):
        if isPrime(i):
            print "Foo"
        elif isPerfect(i):
            print "Bar"
        else: 
            print "Foobar"
foobar()
        
        
    

"""
def isPrime(num):
    prime = True
    for i in range(2,num):
        if num % i == 0:
            prime = False
    print prime
isPrime(13)
#prime numbers only divisible by 1 and themselves 
#perfect square: X*X = num  Number made by squaring an int 

If it is a prime number print "Foo". If it is a perfect square print "Bar". If it is neither print "FooBar".






Write a program that prints all the prime numbers and all the perfect squares for all numbers between 100 and 100000.

For all numbers between 100 and 100000 test that number for whether it is prime or a perfect square. If it is a prime number print "Foo". If it is a perfect square print "Bar". If it is neither print "FooBar". Do not use the python math library for this exercise. For example, if the number you are evaluating is 25, you will have to figure out if it is a perfect square. It is, so print "Bar".

This assignment is extra challenging! Try pair programming and pulling up a white board.

"""