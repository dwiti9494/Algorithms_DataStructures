"""
Using OOP in Python, we can restrict access to methods and variables. 
This prevents data from direct modification which is called encapsulation. 
"""

class Computer: 
    def __init__(self):
        self.__maxprice = 900 # meant to be private
    
    def sell(self):
        print("Selling price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        if (price > 1200):
            self.__maxprice = 1200
        else:
            self.__maxprice = price

    def getMaxPrice(self):
        return self.__maxprice

c = Computer()
c.sell()

# Change the price
c.__maxprice = 1400 # tryin to access private member variable outside class - bad practice
c.sell()

# Using setter fucntion
c.setMaxPrice(1400) # use setter to set a private member variable according to class spec
c.sell()

print(c.getMaxPrice())