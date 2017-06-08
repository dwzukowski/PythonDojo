class Product(object):
    def __init__(self, price, item, weight, brand, cost):
        self.price = price
        self.item = item
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "For Sale"
    def Sell(self):
        #print "Selling"
        self.status = "Sold"
        return self 
    def AddTax(self, tax):
        total=self.price
        total+= self.price*tax
        print "Cost with tax is {}".format("%.2f"%total)
    def DisplayInfo(self):
        print " Item: {} \n Status: {} \n Price: {} \n Cost: {} \n Weight: {} \n Brand: {} \n".format(self.item, self.status, self.price, self.cost, self.weight, self.brand)
    def Return(self, reason):
        if reason == "defective":
            self.status = "Defective"
            self.price = 0
        elif reason =="in box":
            self.status ="For Sale"
        elif reason =="opened":
            discount=0.20
            self.price*= (1-discount) 
        else:
            print "Please enter one of the following: 'defective', 'in box', or 'opened'"
        return self
      
#product1 =Product(500.1, "computer", "5 lb", "Lenovo", 300)
#product1.DisplayInfo()
#product1.Return("unknown")
#print product1.Sell().status




"""
Return: takes reason for return as a parameter and changes status accordingly.  If it is being returned in the box, like new mark it as for sale. If the box has been opened set status to used and apply a 20% discount.


Assignment: Product
The owner of a store wants a program to track products. Create a product class to fill the following requirements.
f
Product Class:
Attributes:

Price

Item Name

Weight

Brand

Cost

Status: default "for sale"
Methods:

Sell: changes status to "sold"

Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax

Return: takes reason for return as a parameter and changes status accordingly. If the item is being returned because it is defective change status to defective and change price to 0. If it is being returned in the box, like new mark it as for sale. If the box has been opened set status to used and apply a 20% discount.

Display Info: show all product details.
Every method that doesn't have to return something should return self so methods can be chained.
"""