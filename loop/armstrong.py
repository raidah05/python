n = int(input("Enter a number: "))

sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum += digit**3
    temp //=10

if n == sum:
    print("Number is an armstrong number.")
else:
    print("Number is not an armstrong number")