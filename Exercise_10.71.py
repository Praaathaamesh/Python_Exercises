'''
Overriding 
of Area methods 
with Multilevel Inheritance of
Class Sphere with 
derived class Diameter, Surface Area, and Volume 
using super Keyword
'''

import math
from ObjOp.SphMod import Sphere

class Diameter(Sphere):
    def __init__(self, radius):
        super().__init__(radius)   
    def diameter(self):
        return 2 * self.radius

class SurfaceArea(Diameter):
    def __init__(self, radius):
        super().__init__(radius)  
    def area(self):
        surface_area = super().area()
        print(f"Surface Area of the sphere is: {surface_area}")
        
class Volume(SurfaceArea):
    def __init__(self, radius):
        super().__init__(radius)
    def area(self):
        surface_area = super().area()
        volume = (4/3) * math.pi * (self.radius ** 3)
        print(f"Volume of the sphere is: {volume}")
        
radius = 5
sphere_volume = Volume(radius)
sphere_volume.area()