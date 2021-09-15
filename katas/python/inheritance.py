"""
Inheritance is a way of creating a new class for using details of an existing class without modifying it. 
The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).
"""

# Parent class
class Bird:
    def __init__(self):
        print("Bird is ready")
    def whoIsThis(Self):
        print("Bird")
    def swim(self):
        print("Swim faster")

# Child class
class Pegion(Bird):
    def __init__(self):
        # call super() function
        super().__init__()
        print("Pegion is ready")

    def whoIsThis(self):
        print("Pegion")
    
    def run(self):
        print("Run faster")

peggy = Pegion()
peggy.whoIsThis()
peggy.swim()
peggy.run()
