from GeoOp import D2_Op
from GeoOp import D3_Op

# 2D shapes geometry opertaions
print("Calculate the area of circle:")
r = int(input("enter the radius in cm: "))
print(f'the area of circle with radius {r}cm is {D2_Op.CirA(r)}')

print("Calculate the area of triangle:")
b = int(input("enter the base in cm: "))
h = int(input("enter the height in cm: "))
print(f'the area of triangle is {D2_Op.triA(b,h)}')

print("Calculate the area of square:")
a = int(input("enter the side in cm: "))
print(f'the area of square is {D2_Op.SqrA(a)}')

print("Calculate the area of rectangle:")
l = int(input("enter the length in cm: "))
w = int(input("enter the width in cm: "))
print(f'the area of rectangle is {D2_Op.RecA(l,w)}')

print("Calculate the area of parallelogram:")
b = int(input("enter the base in cm: "))
h = int(input("enter the height in cm: "))
print(f'the area of parallelogram is {D2_Op.ParaA(b,h)}')

print("Calculate the area of trapezium:")
a = int(input("enter the side in cm: ")) 
b = int(input("enter the base in cm: "))
h = int(input("enter the heigh0t in cm: "))
print(f'the area of trapezium is {D2_Op.TrapA(a,b,h)}')

# 3D shapes geometry opertaions
print("Calculate the area of cube:")
a = int(input("enter the side in cm: "))
print(f'the area of cube is {D3_Op.CubA(a)}')

print("Calculate the area of rectangular prism:")
l = int(input("enter the length in cm: "))
w = int(input("enter the width in cm: "))
h = int(input("enter the height in cm: "))
print(f'the area of triangle is {D3_Op.PrismA(l,w,h)}')

print("Calculate the area of Cylinder:")
r = int(input("enter the radius in cm: "))
h = int(input("enter the height in cm: "))
print(f'the area of square is {D3_Op.CylA(r,h)}')

print("Calculate the area of Cone:")
r = int(input("enter the radius in cm: "))
l = int(input("enter the length in cm: "))
print(f'the area of cone is {D3_Op.ConeA(r,l)}')

print("Calculate the area of sphere:")
r = int(input("enter the radius in cm: "))
print(f'the area of sphere is {D3_Op.SphereA(r)}')

print("Calculate the area of hemisphere:")
r = int(input("enter the radius in cm: "))
print(f'the area of sphere is {D3_Op.HemiA(r)}')
