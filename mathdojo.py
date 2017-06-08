class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self,num1, num2=0):
        self.result+=num1
        self.result+=num2
        return self
    def subtract(self,num1, num2=0):
        self.result-=num1
        self.result-=num2
        return self

md= MathDojo()
print md.add(2).add(2,5).subtract(3,2).result
""" 

Assignment: MathDojo
HINT: To do this exercise, you will probably have to use 'return self'. If the method returns itself (an instance of itself), we can chain methods.

PART I
Create a Python class called MathDojo that has the methods add and subtract. Have these 2 functions take at least 1 parameter.

Then create a new instance called md. It should be able to do the following task:

MathDojo().add(2).add(2, 5).subtract(3, 2).result
Copy
which should perform 0+2+(2+5)-(3+2) and return 4.
Assignment: Call Center
You're creating a program for a call center. Every time a call comes in you need a way to track that call. One of your program's requirements is to store calls in a queue while callers wait to speak with a call center employee.

You will create two classes. One class should be Call, the other 