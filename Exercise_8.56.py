# to generate 6 digit random secure OTP

import random
otp = []
i = 1
while i <= 6:
    num = random.randint(0,10)
    otp.append(str(num))
    i+=1
OTP = ''.join(otp)
print("Randomly generated secure OTP:", OTP)

