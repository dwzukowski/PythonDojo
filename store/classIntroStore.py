#linking previous assignment 
from classIntroProduct import Product
class Store(object):
    def __init__(self, owner, address):
        self.owner = owner
        self.address = address
        self.products = []
    def add_product(self,product):
        self.products.append(product)
        return self
    def remove_product(self, product):
        itemLocationInProducts = store1.products.index(product) 
        self.products.pop(itemLocationInProducts)
        return self
    def inventory(self):
        print "--- STORE INVENTORY ---"
        for i in range(0,len(self.products)):
            print self.products[i].DisplayInfo()


product1 =Product(500.10, "computer", "5 lb", "Dell", 300)
product2 =Product(70, "keyboard", "2 lb", "Corsair", 50)
product3 =Product(2000, "gold coin", "1 oz", "Mint", 1900)
store1= Store("Dave Z", "1447 Chanute")
store1.add_product(product1)
store1.add_product(product2)
store1.add_product(product3)
#print store1.products[2].DisplayInfo()
#print store1.products
#print store1.products
#print store1.products[1].DisplayInfo()
#store1.remove_product(product2)
#print store1.products.index(product2)   return index of products
store1.inventory()
"""

Optional Assignment: Store
Now, let's build a store to contain our products by making a store class and putting out products into an array.

Store class:
Attributes:
products: an array of products objects
location: store address
owner: store owner's name
Methods:

add_product: add a product to the store's product list

remove_product: should remove a product according to the product name

inventory: print relevant information about each product in the store
You should be able to test your classes by instantiating new objects of each class and using the outlined methods to demonstrate that they work.




"""