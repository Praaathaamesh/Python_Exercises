#Categorize Password as Strong or Weak 
import re

str1 = input("Please enter the password:")
# must contain a capital letter
# must contain letters
# must contain digits
# must contain any special character(!,@,#,$,%,&,*)

pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"

x = re.findall(pattern, str1)
if x:
    print("It is a strong password")
else:
    print("It is a weak password")
