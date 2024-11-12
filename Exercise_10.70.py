'''
Overriding 
of Volume and Surface Area for 
Class Sphere, Cylinder, Cone, Cube, and Prism 
using the Super Keyword and For Loop.
'''

class figure:
    def __init__(self, name):
        self.name = name

    def volume(self):
        print("Volume is calculated")

    def surf_area(self):
        print("Surface area is calculated")

class Sphere(figure):
    def __init__(self,r):
        super().__init__("Sphere")
        self.r = r

    def volume(self):
        return 3.14*self.r*self.r
    
    def surf_area(self):
        return 4*(3.14*self.r*self.r)
    
class Cylinder(figure):
    def __init__(self,r,h):
        super().__init__("Cylinder")
        self.r = r
        self.h  = h

    def volume(self):
        return 3.14*self.r*self.r*self.h
    
    def surf_area(self):
        return 2*(3.14*self.r*self.h)
    
class Cone(figure):
    def __init__(self,r,h,l):
        super().__init__("Cone")
        self.r = r
        self.h  = h
        self.l = l

    def volume(self):
        return (3.14*self.r*self.r*self.h)/3
    
    def surf_area(self):
        return 2*(3.14*self.r*self.l)
    
class Cube(figure):
    def __init__(self,a):
        super().__init__("Cube")
        self.a = a

    def volume(self):
        return (self.a**3)
    
    def surf_area(self):
        return 6*(self.a**2)
    
class Prism(figure):
    def __init__(self,w,h,l):
        super().__init__("Prism")
        self.w = w
        self.h  = h
        self.l = l

    def volume(self):
        return self.l*self.w*self.h
    
    def surf_area(self):
        return 2*(self.l*self.w+self.h*self.h+self.h*self.l)
    
obj_sph =Sphere(2)
obj_cyl = Cylinder(2,5)
obj_cone = Cone(2,5,4)
obj_cube = Cube(6)
obj_pri = Prism(2,5,6)

print(f"The volume of sphere is {obj_sph.volume()} and the surface area is {obj_sph.surf_area()}")
print(f"The volume of cylinder is {obj_cyl.volume()} and the surface area is {obj_cyl.surf_area()}")
print(f"The volume of sphere is {obj_cone.volume()} and the surface area is {obj_cone.surf_area()}")
print(f"The volume of sphere is {obj_cube.volume()} and the surface area is {obj_cube.surf_area()}")
print(f"The volume of sphere is {obj_pri.volume()} and the surface area is {obj_pri.surf_area()}")