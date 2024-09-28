# PROGRAM DEMONSTRATING USE OF format()

# Declaring various string and integer variables
StrVar2 = "Soda"
StrVar3 = "Evening"
StrVar4 = 4
State1 = "Nothing is better than a cold can of {}, in the {}, at {} o' clock!"

#Implying the format() method
formatVar = State1.format(StrVar2, StrVar3, StrVar4) # Declare varibale with format() method
print("The new formatted string is ", formatVar) #Print the formatted string containing variable