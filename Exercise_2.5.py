# PROGRAM OF USING IN-BUILT MATH FUNCTIONS IN PYTHON

import math

#Declaring variables
var1 = 44
var2 = 56
var3 = 2
var4 = 3.7
#Using In-Built mathematical functions

AbsoluteVar = math.fabs(var1)
SqrtVar = math.sqrt(var2)
PowVar = math.pow(var1,var3)
CeilVar = math.ceil(var4)
FloorVar = math.floor(var4)
FactVar = math.factorial(var3)

#print the results
print(f"The absolute value for {var1} is {AbsoluteVar}")
print(f"The square root for {var2} is {SqrtVar}")
print(f"{var3} to the power of {var1} is {PowVar}")
print(f"The ceiling value of {var4} is {CeilVar}")
print(f"The Floor value of {var4} is {FloorVar}")
print(f"The Factorial of {var1} is {FactVar}")
