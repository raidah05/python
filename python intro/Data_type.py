a = 5 
print("Data type of a : " , type(a)) 

b = 4.5
print("Data type of b : " , type(b)) 

c = "Raidah"
print("Data type of c : " , type(c)) 

d = True 
print("Data type of d :" , type(d))


#Type casting 

name = "Raidah"
age = 16
student = True
weight = 45

print("The name is " , name)
print("The data type of name :" , type(name))

print("Age is " , age)
print("The data type of age :" , type(age))

print("Are you student " , student)
print("The data type of student :" , type(student))

print("What is your weight " , weight)
print("The data type of weight :" , type(weight))

print("After Type-casting")
age = float(age)
print("The data type of age :" , type(age))
weight = int(weight)
print("The data type of weight :" , type(weight))

#string opertion

text = str(input("Enter a string:  "))
revtext = text[::-1]
print("The reversed text is:  " , revtext)


