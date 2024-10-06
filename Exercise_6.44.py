# calculate the factorial of the number entered by the user

n = int(input("Enter the number: "))

def facto(num):
    if num == 1 or num == 0:
        return 1
    elif num<0:
        return "Valid number please"
    else:
        return  num * facto(num-1)
        
print(facto(n))
