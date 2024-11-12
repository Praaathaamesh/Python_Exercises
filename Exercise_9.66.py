'''Hierarchical Inheritance.
Create Cone class 
with a methods to calculate height, 
area of base and circumference of a cone. 
Create two subclasses Volume and Surface Area to 
calculate volume and 
surface area of the cone respectively 
with user-defined Slant height and Radius.
    Volume = area of the base*height
    Surface Area= 1/3*area of base +1/2 (Circumference* height)'''
import math
class Cone:
    def __init__(self,r,l):
        self.r = r
        self.l = l
    def Barea(self):
        return (3.14*((self.r)**2))
    def Cirf(self):
        return (3.14*(self.r)*2)
    def height(self):
        return (math.sqrt((self.l)**2-(self.r)**2))
class Vol(Cone):
    def calc_vol(self):
        return (3.14*((self.r)**2))*(math.sqrt((self.l)**2-(self.r)**2))
class Sur_area(Cone):
    def calc_surf_area(self):
        return ((3.14*((self.r)**2))/3+((3.14*(self.r)*2))/(math.sqrt((self.l)**2-(self.r)**2)))

R = float(input("Please enter a radius of the base "))
L = float(input("Please enter a slant height "))
VOL = Vol(R,L)
SUR = Sur_area(R,L)
print(f"the volume of the cone is {VOL.calc_vol()} cubic cms") 
print(f"The surface area of the cone is {SUR.calc_surf_area()} sq.cms")
