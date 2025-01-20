
try:
    n = int(input("Enter a number: "))
    print(n)
except ValueError as ex:
    print("Please enter a valid number")

print("I am outside the try block")
