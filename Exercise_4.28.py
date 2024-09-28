# program to generate the random numbers from 1 to 10 and add them in a defined list

import random
randlist = []
for i in range (11):
    randlist.append(random.randrange(1,10))
print("Random number generated list is: ",randlist)