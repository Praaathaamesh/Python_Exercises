# SUM OF ALL NUMBERS FROM ONE TO GIVEN NUMBER
Input_var = input("Enter the given number:")
var1 = 0 #Declare an empty variable
for i in range(1,int(Input_var)+1):
    var1 += i # Add each element rom range to an empty variable    
print(f"Sum of all numbers from 1 to {Input_var} is {var1}")
