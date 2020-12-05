# Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area. 

class Rectangle :

    def __init__(self ,x ,y) :
        self.length = x
        self.width = y

    def area(self) :
        return self.length * self.width

rect = Rectangle(10,23)

print(rect.area())