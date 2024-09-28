#ASTERISK PYRAMID PRINTING USING NESTED FOR LOOPS
str1 = "*"
# Print increasing pattern
for i in range(5):
    for j in range(i):
        print(str1, end="")
    print()  # Moves to the next line
# Print decreasing pattern
for i in range(5, 0, -1):
    for j in range(i):
        print(str1, end="")
    print()  # Moves to the next line