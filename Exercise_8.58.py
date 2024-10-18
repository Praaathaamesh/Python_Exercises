# a string starts and ends with the same character or not
import re
string1 = input("Please enter a string: ")

pat1 = rf'\b{string1[0]}'
pat2 = rf'{string1[-1]}\b'
x = re.search(pat1, string1)
y = re.search(pat2, string1)

if x and y:
    print("Yes. The string starts and ends with a same character.")
else:
    print("No. The string doesnt starts and ends with a same character.")
