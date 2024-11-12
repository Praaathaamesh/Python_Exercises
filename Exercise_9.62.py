'''use of class and method to
calculate the area of a rectangle
for user-defined dimensions'''

class rec:
# __init__ method assigns the values for l and b
    def __init__(self, l, b):
        self.l = l
        self.b = b
# Object method to calculate the area
    def area(self):
        return self.l * self.b
# Input for L and B
L = float(input("Please enter the length!"))
B = float(input("Please enter the breadth!"))

dim = rec(L,B)
x = dim.area()
print("area of the rectangle is:",x)

