# PROGRAM DEMONSTRATING THE STRING OPERATORS

str1  = "Buenas noches Jose" # Declarig a string Variable
# ARRAY ACCESSING A STRING
print(f"Accessed string character is {str1[3]}") 
# UPDATING A STRING
print("Updated string is", str1[:7] + "day")
# SLICING A STRING
print(f"Sliced string is {str1[:5]}")
# RANGE SLICING A STRING
print(f"Range sliced string is {str1[0:8]}")
# DEMOSTRATING NEGETIVE INDEXING
print(f"Sliced string from index -5 to -1 is {str1[-5:-1]}")
print(f"Sliced string from index -3 to -1 is {str1[-3:-1]}")
print(f"Sliced string from index -7 to -2 is {str1[-7:-2]}")
# USING STRING FUNCTION CALLED "len()"
print(f"Length of the string is {len(str1)}")

# SPECIAL STRING OPERATORS
#Declaring two string variables
strA = "Greetings"
strB = "Populus" 
Concat = strA + strB # CONCATENATION OF TWO STRINGS
Repete = strB*2 # REPETITION OF ONE STRING
InVar = "G" in strA 
print(f"The truth value for the presence of character \'G\' in {strA} is {InVar}") # USING in MEMBERSHIP OPERATOR
NotInVar = "u" in strB
print(f"The truth value for the presence of character \'u\' in {strB} is {NotInVar}") # USING not in MEMBERSHIP OPERATOR
