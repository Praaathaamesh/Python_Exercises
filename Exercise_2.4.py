# Declare the two integer variables
x = 22
y = 33
#Using Arithmetic operators
Expo_Var = x**y #Exponential
FloorDiv_Var = x//y #Floor Division
Mod_Var = x%y #Modulus
#Printing the results of arithmatic operations
print(f"Exponent Value of {x}**{y} is {Expo_Var}")
print(f"Floor Division of {x}//{y} is {FloorDiv_Var}")
print(f"Modulus of {x}%{y} is {Mod_Var}")

#Declaring two new integer Variables
a = 33
b = 77
#Using Assignment Operators
print(f"the two variables are a={a} and b={b}")
a += 3 # Adding assigned value to a variable
print(f"Added assigned value to variable a and the new value is {a}")
b -= 5 # subtracting assigned value from a variable
print(f"Subtracting assigned value from variable b and the new value is {b}")
a *= 2 # Multiplying assigned value to a variable
print(f"Multiplied assigned value to variable a and the new value is {a}")
b /= 5 #Diving assigned value from a variable
print(f"divided assigned value from variable b and the new value is is {b}")
a%= 5 #assigning a modulus operator to a variable
print(f"Assigned %=5 to variable a and the new value is {a}")
b//= 6 #floor division assignment
print(f"Floor divided assigned value to variable b and the the new value is {b}")
a**= 2 #Exponential assignment
print(f"exponential assignment for a variable a and the new value is {a}")

#declare two variables
i = 22
j = 44
#Using Logical Operators
k = ((i<j) and (j>i))
l = ((i>j) or (j>i))
m = not(i==j)
print(f"The comparison between i and j as i is smaller than j and j is greater than i  is {k}")
print(f"The comparison between i and j as i is greater than j or j is greater than i is {l}")
print(f"inverse of the comparison between i and j as i is equal to j is {m}")

#declare two sequences
seq1 = (1,2,3,4,5)
seq2 = (3,4)
In_Var =(seq2 in seq1) 
NotIn_Var = (seq2 not in seq1)
#Using Membership operators
print(f"Since sequence 2 is present in sequence 1, the value is {In_Var}")
print(f"Since sequence 2 is not present in sequence 1, the value is {NotIn_Var}")

str1 = "Car"
str2 = "Car"
str3 = "Dog"
IsVar = (str1 is str2)
IsNotVar = (str1 is not str3)
#using identity operators
print(f"since alphanumeric string literal in variable str1 is same as str2, the value is {IsVar}")
print(f"since alphanumeric string literal in variable str1 is not same as str3, the value is {IsNotVar}")
