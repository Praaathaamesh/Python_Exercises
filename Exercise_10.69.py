'''Overriding of Area methods
with Hierarchical Inheritance of
Class Square, Circle, Rectangle, and Triangle
Derived from Class Figure.
Super Keyword not required'''

from ObjOp.FigMod import figure

class square(figure):    
    def area(self):
        return (self.l)**2
    
class rectangle(figure):    
    def area(self):
        return (self.l)*(self.b)
    
class circle(figure):    
    def area(self):
        return (3.14*((self.r)**2))

class triangle(figure):    
    def area(self):
        return ((self.b)*(self.h))/2
    
obj_sq = square(5,6,2,4)
obj_rec = rectangle(5,6,2,4)
obj_circ = circle(5,6,2,4)
obj_tri = triangle(5,6,2,4)

area_sq= obj_sq.area()
area_rec= obj_rec.area()
area_circ= obj_circ.area()
area_tri= obj_tri.area()

print("Area of square is: ",area_sq)
print("Area of rectangle is: ",area_rec)
print("Area of circle is: ",area_circ)
print("Area of triangle is: ",area_tri)