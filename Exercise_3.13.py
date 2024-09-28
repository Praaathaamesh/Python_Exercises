# ODD OR EVEN
#Taking input 
StartVar = int(input("start bound: "))
StopVar = int(input("stop bound: "))
StepVarstr = input("step bound: ")
# If theres no step enter the valid step value
while StepVarstr == "":
    print("Print a valid number!")
    StepVarstr = input("step bound: ")    
StepVar = int(StepVarstr) #Covert it to an integer
# Declare empty strings and add each element of tthe range.
Evestr = ''
Oddstr = ''
for i in range (StartVar, StopVar, StepVar):
    if i % 2 == 0:        
        Evestr += str(i) 
    else:       
        Oddstr += str(i)
# Separate each element by a comma
x = ','.join(Evestr)
y = ','.join(Oddstr)
print(f"There are {len(y)} Odd numbers: {y} and There are {len(x)} Even numbers: {x}")