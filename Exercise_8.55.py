'''generate a 15-character alphanumeric password 
with at least one lowercase character, 
at least one uppercase character, 
at least one special character, and at least three digits.'''

import random
import string

Lc = list(string.ascii_lowercase)
Uc = list(string.ascii_uppercase)
Dig = list(string.digits)
spchar = ["@","!",",", ".", "$"]
Char = Lc+Uc
PW = []
for i in range(1,12):
  x = random.choice(Char)
  PW.append(x)
for i in range(1,4):
  y = random.choice(Dig)
  PW.append(y)
z = random.choice(spchar)
PW.append(z)
print(''.join(PW))