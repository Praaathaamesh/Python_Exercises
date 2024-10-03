# a program to demonstrate the looping through the dictionaries, printing keys and values separately and together

# declare a dictionary
dict1 = {'emp1':22, 'emp2':55, 'emp3':33, 'emp4':88, 'emp5':75}

# Accessing the keys
print(dict1['emp1'])

# print the keys
print("ALL THE KEYS: ")
for i in dict1:
    print(i)
print("ALL THE VALUES: ")
# print the values
for i in dict1:
    print(dict1[i])
print("ALL THE KEY-VALUE PAIRS: ")
# print key value pairs
for i in dict1:
    print(i, '==>', dict1[i])


    
