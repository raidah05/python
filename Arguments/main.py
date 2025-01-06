print("Prime Numbers")

num = 29 
flag = False
for i in range(2 , num):
    if (num % i) == 0:
        flag = True
        break

if flag:
    print(num , "Is not a prime number")
else:
    print(num , "Is  a prime number")


print("Cubic calculator")
num1 = int(input("Please enter a number: "))

def cube(num1):
    return num1*num1*num1

print(f"The cube of {num1} is {cube(num1)}")

 



print("Factorial")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

number = int(input("Enter a number:"))   
if (number<0):
    print("Factorial does not work for negative numbers")
else:
    print(f"The factorial of {number} is {factorial(number)}")
    