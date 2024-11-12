'''
Encapsulation 
for displaying the characteristics 
of the Circle.
'''

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            print("Radius must be positive")
    def diameter(self):
        return self.__radius*2
    def get_radius(self):
        return self.__radius
    def calculate_area(self):
        return 3.1416 * (self.__radius ** 2)
    def calculate_circumference(self):
        return 2 * 3.1416 * self.__radius
    def display_characteristics(self):
        print(f"Circle Characteristics is:")
        print(f"Radius is: {self.__radius}")
        print(f"Diameter is: {self.diameter()}")
        print(f"Area is: {self.calculate_area()}")
        print(f"Circumference is: {self.calculate_circumference()}")

circle = Circle(5)
circle.display_characteristics()
circle.set_radius(7)
circle.display_characteristics()
