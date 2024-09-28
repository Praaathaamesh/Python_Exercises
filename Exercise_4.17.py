# USER INPUT LIST AND PRINT THE ELEMENTS
# Define the number of inputs
DefVar = input("Define the number of the elements: ")
Listvar = [] #Declare an empty list
# use a for loop to add elements to the list 
for i in range(0, int(DefVar)):
    i = input("add each element: ")
    Listvar.append(i)
# print the elements
print(Listvar)
for j in range(len(Listvar)):
    print(Listvar[j])

