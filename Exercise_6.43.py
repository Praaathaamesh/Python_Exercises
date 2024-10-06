# Determine if number is armstrong or not
n = str(input("Enter the number please! "))
digits = len(n)

def arms(num):
    num0 = 0
    for i in num:
        num0 += int(i)**digits
    if num0 == int(n):
        print(f"the number {n} is an armstrong number. ")
    else:
        print(f"the number {n} is not an armstrong number. ")
arms(n)    
    
