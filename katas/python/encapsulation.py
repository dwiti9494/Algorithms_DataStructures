"""
Using OOP in Python, we can restrict access to methods and variables. 
This prevents data from direct modification which is called encapsulation. 
"""

class Computer: 
    def __init__(self):
        self.__maxprice = 900
    
    def sell(self):
        print("Selling price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# Change the price
c.__maxprice = 1400
c.sell()

# Using setter fucntion
c.setMaxPrice(1400)
c.sell()