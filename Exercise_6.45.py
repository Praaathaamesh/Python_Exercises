# lambda function all odd and even numbers separately from a user defined range

n1 = int(input("Please specify the start: "))
n2 = int(input("Please specify the stop: "))
n3 = int(input("Please specify the step: "))

list1 = list(range(n1,n2+1,n3))
print("use defined list: ",list1)
print("List of even numbers: ", list(filter(lambda i: i% 2 == 0, list1)))
print("List of odd numbers: ", list(filter(lambda i: i% 2 != 0, list1)))
