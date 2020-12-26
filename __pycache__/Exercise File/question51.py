# Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area

import math


class Circle(object):
    def __init__(self, r):
        self.radius = int(r)

    def area(self):
        return math.pi * 2 * self.radius


e = Circle(3)

print(e.area())