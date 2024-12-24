n = int(input("Enter a number: "))
sum = 0
temp = n

while temp>=0:
    digit = temp%10
    if digit <=9:
        sum = sum

    sum= sum + 1
    temp//=10
print("There are total ", sum ,"digits in the given number")
