# PRINT DUPLICATE INTEGERS FROM THE LIST

list1 = [55,5,3,95,21,3,44,6,2,5,6,6]
list1.sort()
duplist = ['']
for i in range(len(list1)-1):
    if list1[i]== list1[i+1]:
        if duplist[-1] != list1[i]:
            duplist.append(list1[i])
print("The duplicate numbers are: ", duplist[1:])
