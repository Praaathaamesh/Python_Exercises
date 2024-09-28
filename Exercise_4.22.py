# USER INPUT TUPLE

n = int(input("Enter the number of elements in the tuple: "))
elements = []
# Use a loop to take input for each element
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    elements.append(element)
# Convert the list to a tuple
my_tuple = tuple(elements)
# Print the elements
print("The elements in the tuple are:")
for i in range(len(my_tuple)):
    print(my_tuple[i])