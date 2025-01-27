import random
playing = True
num = str(random.randint(10,20))

print("Guess the random number between 10 to 20.")
number = input("Guess the number :")
while playing:
    if number==num:
        print("your guess is correct.")
        break
    else:
        print("Oops! Try again.")