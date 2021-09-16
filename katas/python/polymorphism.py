"""
Polymorphism is an ability (in OOP) to use a common interface 
for multiple forms (data types).
"""

import math

# common interface
class Shape:
    def __init__(self):
        pass

    def name(self):
        print("Shape class is abstract. Does not have name")
        pass

    def area(self):
        print("Shape class is abstract. Can not compute area")
        pass

    def draw(self):
        print("Shape class is abstract. Can not draw")
        pass

class Square(Shape):
    def __init__(self, name, side):
        self.__area = side * side
        self.__name = name

    def name(self):
        return self.__name

    def area(self):
        print("Computing {} area as {}".format(self.__name, self.__area))
        return self.__area
    
    def draw(self):
        print("Drawing a square...")

class Circle(Shape):
    def __init__(self, name, radius):
        self.__area = math.pi * radius * radius # mve compute intensive code here so that is only called once
        self.__name = name

    def name(self):
        return self.__name

    # override the base shape class method here
    def area(self):
        print("Computing {} area as {}".format(self.__name, self.__area))
        return self.__area

    def draw(self):
        print("Drawing a circle...")

def find_max_area(shapes):
    max_area = 0
    max_i = -1
    for i, s in enumerate(shapes):
        area = s.area()
        if area > max_area:
            max_area = area
            max_i = i
    return (shapes[max_i], max_area)

def find_max_area_shape(shapes):
    shape_max = shapes[0]
    for s in shapes:
        shape_max = s if s.area() > shape_max.area() else shape_max 
    return shape_max

def main():
    # create 4 objects from various parent classes
    s1 = Circle("circle1", 5)
    s2 = Circle("circle2", 10)
    s3 = Square("square1", 5)
    s4 = Square("square2", 10)

    # find a shape with maximum area and draw it
    (shape, area) = find_max_area([s1, s2, s3, s4])

    print(shape)

    print("Maximum area {} of shape {}".format(area, shape.name()))
    shape.draw()

    # Method 2
    max_shape = find_max_area_shape([s1, s2, s3, s4])
    print(max_shape)

    print("Maximum area {} of shape {}".format(max_shape.area(), max_shape.name()))
    max_shape.draw()

if __name__ == "__main__":
    main()

# class Parrot:
#     def fly(self):
#         print("Parrot can fly")

#     def swim(self):
#         print("Parrot can't swim")

# class Hippo:
#     def fly(self):
#         print("Hippo can't fly")

#     def swim(self):
#         print("Hippo can swim")

# # common interface
# def flying_test(bird):
#     bird.fly()

# # inatantiate objects
# i_parrot = Parrot()
# i_hippo = Hippo()

# # passing the object
# flying_test(i_parrot)
# flying_test(i_hippo)
