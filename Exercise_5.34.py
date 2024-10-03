# a program to demonstrate the declaration and usage of frozen sets.
# declare a set
set1 = {22,55,45,4,9,66,32}

set1.add(59)
print(set1)
# cast the set into a frozen set
set3 = frozenset(set1)
print(set3)
# attempt the element updation on a frozen set
set3.add(76)
print(set3) # Will return an error
