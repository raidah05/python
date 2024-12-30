print("Area of circle")

r = float(input("Enter the radius of circle: "))

def circle_circumference (r):
    return 2*3.14*r

print(circle_circumference(9))






print("Weathercondition")

def weather_condition ():
    print("Weather is pleasent in ", spring)
    print("Weather is same in ", autumn)

spring = "autumn"
autumn = "winter"
weather_condition()






print("Calculator")

def add (X , Y):
    return (X + Y)

def substract (X , Y):
    return (X - Y)

def multiply (X , Y):
    return (X*Y)

def divide (X , Y):
    return(X/Y)

print("Which operator do u want?")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.divide")

operator = int(input("Enter your choice : "))
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if operator == 1:
    print(num1,"+", num2, "=" , add(num1,num2))
elif operator == 2:
    print(num1,"-", num2, "=" , substract(num1,num2))
elif operator == 3:
    print(num1,"x", num2, "=" , multiply(num1,num2))
elif operator == 4:
    print(num1,"/", num2, "=" , divide(num1,num2))
else:
    print("Error")
  
