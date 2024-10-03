# a program to take user-input set elements and demonstrate len() and del() function.

set1 = set()

n = int(input("specify the length of the set: "))

for i in range(0,n):
    i = int(input("enter the numbers: "))
    set1.add(i)
print("use defined set is: ",set1)
# length of the set
print(len(set1))
# using del keyword
del set1
print(set1) # Will return an error 

    
