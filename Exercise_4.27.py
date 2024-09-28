# AVERAGE OF USER DEFINED LIST
# Define a list using inputs
n = int(input("How many elements in the list?, Specify: "))
# Make a list of user inputs
Listvar = []
for i in range (n):
  i = int(input("Enter each element: "))
  Listvar.append(i)
# Calculate the average of the list elements
sumvar = 0
for j in range(len(Listvar)):
  sumvar += Listvar[j]
print("The avverage of numbers in list: ",sumvar/len(Listvar))