'''Polymorphism
for Display and Area methods for
Class Triangle, Rectangle, Square, and Circle.
Use For Loop'''

class triangle:
    def __init__(self, h, b):
        self.h = h
        self.b = b
    def area(self):
        return (1/2*((self.h)*(self.b)))
    def display(self):
        print("Area of triangle is: ",self.area())

class rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b
    def area(self):
        return ((self.l)*(self.b))
    def display(self):
        print("Area of rectangle is: ",self.area())

class square:
    def __init__(self, s):
        self.s = s
    def area(self):
        return (self.s)**2
    def display(self):
        print("Area of square is: ",self.area())

class circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return ((self.r)**2)*3.14
    def display(self):
        print("Area of circle is: ",self.area())

tri_1= triangle(6,5)
rec_1= rectangle(6,5)
sqr_1= square(4)
circ_1= circle(6)

for i in (tri_1, rec_1, sqr_1, circ_1):
    i.area()
    i.display()
        
