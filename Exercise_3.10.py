# DETERMINE IF GIVEN NUMBER IS PRIME OR NOT
var1 = int(input("Enter the desired number:")) #take input integer
if var1 == 1 or var1 == 2:
    print(f"the number {var1} is prime.")
else:
    for i in range (2,var1+1):
        if var1%i ==0:
            break
    if i == var1:
        print("Number is prime")
    else:
        print("Not a prime number!")
