# USE OF LIST OPERATORS

ListVar = ['Banana', 'Apple', 'Grapes', 'kiwi', 'Mango']
ListVar2 = ['Watermelon', 'Orange','Blueberry']
# Using "+" operator to add two lists together
FinalList = ListVar + ListVar2
print("Combination of two lists", FinalList)
print("Attachment of two distincrt elements: ", ListVar[0] + ListVar2[1]) # Attaching two distinct elements together 

ListVar3 = [11,55,33,9,5]
# Multiply the elements of the list using "*" operator  
MultList = ListVar*2
print("Multiplied list: ", MultList)
print("Multiplied certain element: ", ListVar[2]*2) # Multiplying a perticular element of the list
