import random
options = ["Rock" , "Papers" ,'Scissors']

user_choice = input("Rock, Papers or Scissors: ")
comp_choice = random.choice(options)

print("your choice" , user_choice)
print("computers choice" , comp_choice)

if user_choice==comp_choice:
    print("It's a tie!!")
elif user_choice == "Rock" or user_choice=="rock" and comp_choice=="Scissors" or comp_choice=="scissors":
    print("You win!!!!")
elif user_choice == "Paper" or user_choice=="paper" and comp_choice=="Rock" or comp_choice=="rock":
    print("You win!!!!")
elif user_choice == "Scissors" or user_choice=="scissors" and comp_choice=="paper" or comp_choice=="Paper":
    print("You win!!!!")
else:
    print("You lose :/")