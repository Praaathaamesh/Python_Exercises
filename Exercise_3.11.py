# PROGRAM FOR IDENTIFYING AN ARMSTRONG NUMBER.
n = int(input("enter a number: "))#taking input
empvar = 0
str_n = str(n)#Typecasting to a string

for i in str_n:
    empvar += int(i)**3

if empvar == n:
    print(f"The given number {n} is an Armstrong number!")
else:
    print(f"The given number {n} is not an Armstrong Number!")
