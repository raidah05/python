class student:
    grade = 10 
    print('Hi I am a student of grade', grade)

object = student()

#Class vehicle
class vehicle:

    def __init__(self, maxspeed,mileage):
        self.maxspeed = maxspeed
        self.mileage = mileage

modelaudi = vehicle(360, 40)
modelX = vehicle(230, 30)

print("Audi's maxspeed", modelaudi.maxspeed)
print("Audi's mileage", modelaudi.mileage)
print("model's maxspeed", modelX.maxspeed)
print("model's mileage", modelX.mileage)

#class parrot

class parrot:
    species = "Bird"

    def __init__(self, name , age):
        self.name = name
        self.age = age

blu = parrot("blu" , 10)
woo = parrot("woo" , 15)

print("blu is of species named as {} ".format(blu.species))
print("woo is of species named as {} ".format(woo.species))

print("{} is {} years old ".format(blu.name, blu.age))
print("{} is {} years old ".format(woo.name, woo.age))
