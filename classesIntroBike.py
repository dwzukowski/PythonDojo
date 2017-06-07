#we declare a class called bike 
class Bike(object):
    #we set some instance variables; the miles variable will start at zero for every instance of this class
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    #we declare a method called displayInfo that, when called, displays that instance's price, speed, and total miles traveled
    def displayInfo(self):
        print "${}".format(self.price) 
        print self.max_speed
        print "{} miles".format(self.miles)
    #we declare a method called ride which increments total miles by 10; we return self to allow method chaining
    def ride(self):
        print "Riding"
        self.miles+= 10
        return self 
    #we declare a method called reverse which decrements the instance's total miles by 5; we return self to allow method chaining
    def reverse(self):
        print "Reversing"
        self.miles-= 5
        if self.miles < 0:
            self.miles = 0
        return self

bike1 = Bike(200, "25 MPH")
bike2 = Bike(250, "26 MPH")
bike3 = Bike(200, "25 MPH")

#example of method chaining; ride three times, reverse twice, and display 
bike2.ride().ride().ride().reverse().reverse().displayInfo()


"""

Create a new class called Bike with the following properties/attributes:

price
max_speed
miles
Create 3 instances of the Bike class.

Use the __init__() function to specify the price and max_speed of each instance (e.g. bike1 = Bike(200, "25mph"); In the __init__() also write the code so that the initial miles is set to be 0 whenever a new instance is created.

Add the following functions to this class:

displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...
Have the first instance ride three times, reverse once and have it displayInfo(). Have the second instance ride twice, reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().

What would you do to prevent the instance from having negative miles?

Which methods can return self in order to allow chaining methods?

"""