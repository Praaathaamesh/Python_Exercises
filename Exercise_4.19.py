# Initializing a list
my_list = [1, 2, 3, 4, 5]
# append() : Adds an item at the end of the list
my_list.append(6) 
print("After append(6):", my_list)
# clear(): Removes all items from the list, leaving it empty
my_list.clear()
print("After clear():", my_list)

my_list = [1, 2, 3, 4, 5]

# copy() : Creates a copy of the list
list_copy = my_list.copy()
print("Copied list:", list_copy)
# count(): Counts how many times a value appears in the list
count_of_3 = my_list.count(3)
print("Count of 3 in list:", count_of_3)
# extend(): Adds all the elements of another list to the current list
my_list.extend([6, 7])
print("After extend([6, 7]):", my_list)
# index(): Returns the index (position) of the first occurrence of an item
index_of_5 = my_list.index(5)
print("Index of 5:", index_of_5)
# insert(): Inserts an element at a specified position in the list
my_list.insert(2, 9)  # Inserts 9 at index 2
print("After insert(2, 9):", my_list)
# pop(): Removes and returns the item at the given index. If no index is specified, it removes the last item.
popped_item = my_list.pop()  # Removes and returns the last item
print("Popped item:", popped_item)
print("After pop():", my_list)
# reverse(): Reverses the elements of the list in place (changes the order from last to first)
my_list.reverse()
print("After reverse():", my_list)
# sort(): Sorts the list in ascending order (smallest to largest)
my_list.sort()
print("After sort():", my_list)