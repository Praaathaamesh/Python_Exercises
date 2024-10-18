#Extract IP address from file using Python
import re

file1 = "IPADD.txt"
f= open(file1, 'r')
str1 = f.read()
print("All IP addresses", str1)
pattern = "(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
x = re.findall(pattern, str1)
print("All valid IP addresses",x)
