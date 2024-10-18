# validate an Email address entered by the user
import re
str1 = input("please enter your E-mail:")
# [numbers and lowercase letters]@[lowercase letters].[lowercase letters]
pattern = "^[a-z0-9]+@[a-z]+\.[a-z]{2,}$"

x = re.search(pattern,str1)
if x:
    print("E-mail is valid.")
else:
    print("Invalid E-mail")
