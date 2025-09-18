import math

# ADD YOUR SHAPES CLASSES HERE
class Shape:   
    def get_area(self):
        pass
    
    def get_perimeter(self):
        pass

class Rectangle(Shape):   
    def __init__(self, width: float, height: float):
        super().__init__()
        self.width = width
        self.height = height

    def get_area(self):
        return self.height * self.width
    
    def get_perimeter(self):
        return (self.width * 2) + (self.height * 2)
    
class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__()
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)
    
    def get_perimeter(self):
        return (2 * math.pi) * self.radius