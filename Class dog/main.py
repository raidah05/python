class dog:
    species = "Dog"

    def __init__(self, color , age, place, name ):
        self.name = name 
        self.color = color 
        self.age = age 
        self.place = place 

German_Shepherd = dog("brown", "9-15" , "German" , "German Shepherd")
Bull_Dog = dog("white", "8-10" , "British" , "Bull Dog")
Boxer = dog("white", "10-12 ", "German" , "Boxer")
Beagle = dog("white", "12-15" , "England" , "Beagle")

print("The specie of German Shepherd is {}".format(German_Shepherd.species))
print("The specie of Bull dog is {}".format(Bull_Dog.species))
print("The specie of Boxer is {}".format(Boxer.species))
print("The specie of Beagle is {}".format(Beagle.species))


print("{} is of {} years old".format(German_Shepherd.name , German_Shepherd.age ))
print("{} is of {} color".format(German_Shepherd.name , German_Shepherd.color))
print("{} is from {} here".format(German_Shepherd.name ,German_Shepherd.place))


print("{} is of {} years old".format(Bull_Dog.name , Bull_Dog.age ))
print("{} is of {} color".format(Bull_Dog.name , Bull_Dog.color))
print("{} is from {} here".format(Bull_Dog.name ,Bull_Dog.place))

print("{} is of {} years old".format(Boxer.name , Boxer.age ))
print("{} is of {} color".format(Boxer.name , Boxer.color))
print("{} is from {} here".format(Boxer.name ,Boxer.place))


print("{} is of {} years old".format(Beagle.name , Beagle.age ))
print("{} is of {} color".format(Beagle.name , Beagle.color))
print("{} is from {} here".format(Beagle.name ,Beagle.place))
