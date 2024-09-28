# FIND FACTORIAL OF A NUMBER
invar = int(input("Enter a number: ")) # take an input
empvar=invar
for i in range(invar-1,0, -1):
    empvar *= i #Multiplying 
print(f"The factorial of {invar} is {empvar}")
