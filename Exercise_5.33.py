# programs for demonstrating the usage of all the different Set methods

set1 = {"tokyo","osaka","sendai","fukouka"}
set2 = {"kochi","chennai","mumbai","delhi","banglore","osaka","tokyo"}
# adding an element
set1.add("kiyv")
print("element added in set1, new set is: ",set1)
# copying th entire set
set3 = set1.copy()
print("copy ceated of set1: ", set3)
# difference 
print("disjoint values: ", set1.difference(set2))
# discard
set2.discard("kochi")
print("discarded kochi from set2: ", set2)
# intersection
print(set1.intersection(set2))
# isdisjoint/issubset
print("is a disjoint set? :",set1.isdisjoint(set2))
print("is a subset?: ",set1.issubset(set2))
# pop
set2.pop()
print(set2)
# symmetric difference and update
print("symmetric difference: ",set1.symmetric_difference(set2))
set1.symmetric_difference_update(set2)
print("set updated using symetric difference: " ,set1)

# Declare another set
set4 = {22,66,55,4,88}
# union and update
set1.union(set4)
set1.update(set4)
print(set1)
