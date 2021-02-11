class Shape:
    def __init__(self):
        self.Area = 0.0
        
    def DispArea(self):
        print(self.Area)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.Area = 2 * 3.14 * self.radius * self.radius
    

class Rect(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b
        self.Area = l *b
    


a = Circle(5)
b = Rect(2,3)
a.DispArea()
b.DispArea()