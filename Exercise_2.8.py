#PROGRAM DEMONTRATING USE OF STRING METHODS

str1  = "the world has 7 wonders and all of them are AMAZING!"

capvar = str1.capitalize() #capitalises first character
print("Capitalised string:", capvar)
lowvar = str1.lower() #converts to lowercase
print("lowercased string:", lowvar)
upvar = str1.upper() #converts to uppercase
print("uppercased string:", upvar)
titvar = str1.title() #converts first letter of each word in a string to uppercase
print("string converted to the title: ", titvar)
cfvar = str1.casefold() #Return a version of the string suitable for caseless comparisons.
print("casefolded string:", cfvar)

print("\n")
# Swap case of characters
str2, str3, str4 = "iT is Mixed CaSe", "it is all lower case", "IT IS ALL UPPER CASE"
print("Original strings are:\n", str2, "\n",str3,"\n" ,str4)
print("Swapcased strings are:\n",str2.swapcase(),"\n",str3.swapcase(),"\n",str4.swapcase())

print("\n")
# Center the string
greet = "Hello lovely people"
print("Original string is:", greet)
greetvar = greet.center(22, '*') #Return a centered string of length width
print("The centered string is:", greetvar)

print("\n")
# Justify the string
txt = "Morning"
print("original string is:", txt)
leftJvar = txt.ljust(12, "*") #Return a left-justified string of length width. Padding is done using the specified fill character (default is a space).
rightJvar = txt.rjust(12, "*") #Return a right-justified string of length width.
Zfillvar = txt.zfill(14) #Pad a numeric string with zeros on the left, to fill a field of the given width.
print("Left justified string is:", leftJvar)
print("Right justified string is:", rightJvar)
print("Padded string with 0 is:", Zfillvar)

print("\n")
# String operations
txt2 = "I love candies, candies are the best"
print("original string:",txt2)
countvar = txt2.count("candies") #Return a copy with all occurrences of substring.
replacevar = txt2.replace("candies", "apples") #Return a copy with all occurrences of substring old replaced by new.
print("The number of times the substring candies occured is:",countvar)
print("Copy of a replaced string where candies is replaced by apples is:",replacevar)
startvar = txt2.startswith("I") #Returns true if string starts with given argument
endvar = txt2.endswith("best") #Returns true if string ends with given argument
print("The truth value of given string starting with I is:",startvar)
print("The truth value of given string ending with best is",endvar)

print("\n")
# Expand tabs
txt3 = "c\ta\tr"
print("original string:", txt3)
expVar = txt3.expandtabs(3) #Return a copy where all tab characters are expanded using spaces.
print("String with all expanded character is:",expVar)

print("\n")
# String formatting
txt4 = "car is {}"
txt4_1 = "fast"
formatvar = txt4.format(txt4_1) #Replaces placeholders with the given argument
print("Formatted string is:",formatvar)

print("\n")
# Finding and indexing substrings
print("Original string:", txt2)
findvar = txt2.find("we") #Return the lowest index in string where substring sub is found, if not present; returns -1
Rfindvar = txt2.rfind("candies") #Return the highest index in string where substring sub is found
indexvar = txt2.index("are") #Return the lowest index in string where substring sub is found, if not present; returns an error
rindexvar = txt2.rindex("candies") #Return the highest index in string where substring sub is found
print("The word we was found at the index:",findvar)
print("The highest index where the word candies is found:",Rfindvar)
print("the word are was found at the index:", indexvar)
print("The highest index where the word candies is found:", rindexvar)

print("\n")
# String checks
print("Original string:", str1)
alphacheck = str1.isalpha() #Return True if the string is an alphabetic string, False otherwise.
print("the string is not an alphabetic string, hence:",alphacheck)
alphanumcheck = str1.isalnum() #Return True if the string is an alpha-numeric string, False otherwise.
print("the string is not an alphanumeric string, hence:",alphanumcheck)
digitcheck = str1.isdigit() #Return True if the string is a digit string, False otherwise.
print("the string is not an digit string, hence:",digitcheck)
numcheck = str1.isnumeric() #Return True if the string is a numeric string, False otherwise.
print("the string is not an numeric string, hence:",numcheck)
identcheck = str1.isidentifier() #Return True if the string is a valid Python identifier, False otherwise.
print("the string is not an valid identifier, hence:",identcheck)
lowercheck = str1.islower() #Return True if the string is a lowercase string, False otherwise.
print("the string is not an lowercase string, hence:",lowercheck)
uppercheck = str1.isupper() #Return True if the string is an uppercase string, False otherwise.
print("the string is not an uppercase string, hence:",uppercheck)
titlecheck = str1.istitle() #Return True if the string is a title-cased string, False otherwise.
print("the string is not an title-cased string, hence:",titlecheck)
spacecheck = str1.isspace() #Return True if the string is a whitespace string, False otherwise.
print("the string is not an whitespaced string, hence:",spacecheck)

print("\n")
# Strip whitespace
var5 = "    toy    "
strvar = var5.strip() #Return a copy of the string with all left and right whitespace removed.
print("the string with all left and right whitespace removed:",strvar)
rstrpvar = var5.rstrip() #Return a copy of the string with right whitespace removed.
print("the string with allright whitespace removed:",rstrpvar)
lstrpvar = var5.lstrip() #Return a copy of the string with left whitespace removed.
print("the string with all left whitespace removed:",lstrpvar)
