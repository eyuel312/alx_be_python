import math

class Shape:
    def area(self):
        """Base method meant to be overridden in derived classes."""
        raise NotImplementedError("Subclasses must implement the area() method.")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Area of a rectangle: length × width"""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Area of a circle: π × r²"""
        return math.pi * (self.radius ** 2)
