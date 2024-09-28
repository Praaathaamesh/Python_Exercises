# User defined 2D list
Rnum = int(input("Define number of rows: "))
Cnum = int(input("Define number of cols: "))

emp_mat= []

for i in range(Rnum):
    a = []
    for j in range(Cnum):
        a.append(j)
    emp_mat.append(a)

print(emp_mat, end='')