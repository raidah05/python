import math

n = input("Enter the name of the trigonometric value you want: ")
deg = input("Enter the degree: ")

if n =="sin" or n == "Sin" and deg == "0":
    print(math.sin(0))
elif n =="sin" or n == "Sin" and deg == "30":
    print(math.sin(30))
elif n =="sin" or n == "Sin" and deg == "45":
    print(math.sin(45))
elif n =="sin" or n == "Sin" and deg == "60":
    print(math.sin(60))
elif n =="sin" or n == "Sin" and deg == "90":
    print(math.sin(90))

elif n =="cos" or n == "Cos" and deg == "0":
    print(math.cos(0))
elif n =="cos" or n == "Cos" and deg == "30":
    print(math.cos(30))
elif n =="cos" or n == "Cos" and deg == "45":
    print(math.cos(45))
elif n =="cos" or n == "Cos" and deg == "60":
    print(math.cos(60))
elif n =="cos" or n == "Cos" and deg == "90":
    print(math.cos(90))

elif n =="tan" or n == "Tan" and deg == "0":
    print(math.tan(0))
elif n =="tan" or n == "Tan" and deg == "30":
    print(math.tan(30))
elif n =="tan" or n == "Tan" and deg == "45":
    print(math.tan(45))
elif n =="tan" or n == "Tan" and deg == "60":
    print(math.tan(60))
elif n =="tan" or n == "Tan" and deg == "90":
    print(math.tan(90))

else:
    print("Something is wrong:/")


