# ten-character alphanumeric password.

import random
import string

Alphanum= list(string.ascii_uppercase)+list(string.ascii_lowercase)+list(string.digits)
PASS = []
for i in range(1,11):
  x = random.choice(Alphanum)
  PASS.append(x)
print("Password generated: ",("".join(PASS)))