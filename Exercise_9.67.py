'''Multilevel Inheritance. 
Create Cone class with a methods 
to calculate height and circumference of a cone. 
Create second class to calculate the area of base and volume of the cone. 
Create third class to 
calculate the surface area of the cone and 
display height ,circumference, area of base, volume and surface area of the cone 
with user-defined Slant height and Radius. 
The hierarchy should be as follows:
    i.Grand Parent class:Height and circumference
    ii.Parent class: Area of base and Volume
    iii.Child Class:Surface Area and display'''

import math
class Cone:
    def __init__(self,r,l):
        self.r = r
        self.l = l
    def Cirf(self):
        return (3.14*(self.r)*2)
    def height(self):
        return (math.sqrt((self.l)**2-(self.r)**2))

class calc_Barea_vol(Cone):
    def Barea(self):
        return (3.14*((self.r)**2))
    def calc_vol(self):
        return (3.14*((self.r)**2))*(math.sqrt((self.l)**2-(self.r)**2))

class calc_SurArea_Display(calc_Barea_vol):
    def __init__(self, r, l):
        super().__init__(r, l)
    def calc_surf_area(self):
        return ((3.14*((self.r)**2))/3+((3.14*(self.r)*2))/(math.sqrt((self.l)**2-(self.r)**2)))
    def display(self):
        H = self.height()
        CIRCUM = self.Cirf()
        BAREA = self.Barea()
        VOL = self.calc_vol()
        SURF = self.calc_surf_area()

        print(f"The height of the cone is {H}")
        print(f"The circumference of the base of the cone is {CIRCUM}")
        print(f"The Base area of the cone is {BAREA}")
        print(f"The volume of the cone is {VOL}")
        print(f"The surface area of the cone is {SURF}")

R = float(input("Please enter the radius of the base of the cone: "))
L = float(input("Please enter the slant height of the cone: "))

obj_x = calc_SurArea_Display(R,L)
print(obj_x.display()) 