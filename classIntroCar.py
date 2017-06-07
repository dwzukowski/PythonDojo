#we declare a class Car
class Car(object):
    #we set instance variables and display these variables using the display_all method defined below once all attributes have been defined
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        #we instantiate a conditional statement to define tax based on the price attribute
        if self.price > 10000:
            self.tax = "15%"
        else:
            self.tax = "12%"
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.display_all()
    #we define a method called display all which prints a string consisting of the instance's attributes
    def display_all(self):
        print " Price: {} \n Speed: {} \n Fuel Level: {} \n Mileage: {}".format(self.price, self.speed, self.fuel, self.mileage)

car1=Car(2000, "35 mph", "full", "35 mpg")
car2=Car(12000, "60 mph", "empty", "45 mpg")
car3=Car(16000, "71 mph", "full", "25 mpg")
car4=Car(15000, "40 mph", "full", "20 mpg")
car5=Car(13000, "55 mph", "full", "36 mpg")
car6=Car(7000, "135 mph", "full", "15 mpg")
#car6.display_all()


"""
Create a class called  Car. In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%. 

Create six different instances of the class Car. In the class have a method called display_all() that returns all the information about the car as a string. In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.

"""