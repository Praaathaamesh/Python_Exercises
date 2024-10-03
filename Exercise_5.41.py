# a program to sort the elements of a dictionary
# sorting according to keys
dict1= {6:161, 8:3883, 7:26322, 10:655, 9:44}
dictk = dict(sorted(dict1.items())) # using sorted function along with items() method of a dictionary
print(dictk)
# sorting according to values
dictv = dict(sorted(dict1.items(), key = lambda i : i[1]))
print(dictv)