"""4) Python class named Rectangle constructed by a length and width and
               a method which will compute the area of a rectangle. """


class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width


x=input("Enter Length: ")
y=input("Enter Width: ")
newRectangle = Rectangle(x,y)

print(newRectangle.rectangle_area())
