a = 20
b = 10
c = 5 
d = 8
e = 15

sum =a+b+c+d+e
print("The total sum is " , sum)

average = sum/5
print("The total average is " , average)

#ammount

a = int(input("Please enter a ammount: "))

note_1 = a//100
note_2 = (a%100)//50
note_3 = ((a%100)%50)//10

print("notes of 100 taka:" , note_1)
print("notes of 50 taka:" , note_2)
print("notes of 10 taka:" , note_3)

#Percentage calculation

print("please enter your obtained marks")
math = int(input("Enter your Math's number: "))
eng = int(input("Enter your English's number: "))
rel = int(input("Enter your Religion's number: "))
sci = int(input("Enter your Science's number: "))

sum = math+eng+rel+sci
print("The total obtained marks is " , sum)

per = (sum/400)*100
print("The total percentage is " , per)

