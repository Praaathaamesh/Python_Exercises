# a program to take user-input dictionary elements and demonstrate the len() and del() function on Dictionaries

n = int(input("Specify the number of elements: "))

set1 = set()

for i in range(0,n):
    i = input("Enter keys one by one: ")
    set1.add(i)

dict1 = {}

for i in set1:
    y = input("Enter values one by one: ")
    dict1[i] = y

print("User defined dictionary is: ",dict1)

#length of the dictionary
print(len(dict1))

#using del keyword
del dict1['1'] # will the specified key-value pair
print("dictionary with a deleted element", dict1)
del dict1 # will delete the entire dictionary
print(dict1) # Will return an error
