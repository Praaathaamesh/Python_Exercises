'''Multiple Inheritance. 
Create class with radius information 
and create a sub class to access the radius from parent class 
and calculate area and circumference of a circle'''

class dim:
    def __init__(self,r):
        self.r = r

class calc:
    def __init__(self,r):
        self.r = r
    def area(self):
        return (3.14*((self.r)**2))
    def circum(self):
        return (2*(self.r)*2.14)

class Circ(dim, calc):
    def __init__(self, r):
        super().__init__(r)
    def display(self):
        AREA = self.area()
        CIRCUM = self.circum()
        print("The area of a cicle is", AREA)
        print("The circumference of the circle is", CIRCUM)

x = Circ(float(input("Please enter the radius: ")))
FINAL = x.display()
