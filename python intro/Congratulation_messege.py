name = str(input("Enter your name:  "))
age = int(input("Enter your age:  "))
is_student = bool(input("Are you a student:  "))
class_stu = int(input("If yes, what class are you in: "))

print("Congratulations " , name , "\n You have succesfully completed" , age ,"years of your life on earth.")

#quiz 

print("How many phases are there in Mitosis cell division?")

ans = int(input("Please enter your answer:  "))
if(ans == 5):
    print("Your answer is correct!")
else:
    print("Your answer is incoreect!")   
