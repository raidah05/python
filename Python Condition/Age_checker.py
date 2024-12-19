from datetime import date
a = date.today()
y = a.year

n = int(input("Enter your birth-year: "))
age = y - n
if age <= 10 :
    print("You are" ,age, "years old.")
    print("You are too young")
elif age > 10 and age <= 20:
    print("You are" ,age, "years old.")
    print("You are young")
else:
    print("You are" ,age, "years old.")
    print("You are ageing")