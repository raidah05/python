char = str(input("Enter the character: "))
string = str(input("Enter the word: "))

i = 0
count = 0

while (i< len(string)):
    if (string[i] == char):
        count = count + 1
    i = i + 1
print("The character ", char , "is used ", count,"times")
