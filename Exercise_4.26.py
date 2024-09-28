# CALCULATE POSITIVE AND NEGETIVE NUMBERS WITHIN THE LIST
Listvar = [0,22,-2,99,-63,-99,6635,635,-7]
PosList = []
Neglist = []
for i in Listvar:
    if i == 0:
        print(Listvar[i]," is Present in the given list.")
    elif i > 0:
        PosList.append(i)
    else:
        Neglist.append(i)

print(f"Positive numbers are: {PosList}")
print(f"Negetive numbers are: {Neglist}")