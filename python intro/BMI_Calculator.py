h = float(input("Enter your height in meter:  "))
w = float(input("Enter your weight in kg:  "))

bmi = w/(h**2)

if bmi <= 18.4:
    print("You are underweight")
elif bmi <= 24.9:
    print("You are healthy")
elif bmi <= 29.9:
    print("You are too healthy")
elif bmi <= 34.9:
    print("You are overweight")
elif bmi <= 39.9:
    print("You are severely obesse")
else:
    print("You are obesse")