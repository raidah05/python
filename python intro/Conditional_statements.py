print("How can you take command from user?")
ans = input("Enter your answer: ")
if (ans == "input"):
    print("Correct")
else:
    print(f"The answer is 'input' not {ans!r}")

print("Who is Albert Einstine?")
ans = input("Enter your answer: ")
if (ans == "Scientist"):
    print("Correct")
else:
    print(f"The answer is 'Scientist' not {ans!r}")


#Profit loss
cp = int(input("Enter your cp: "))
sp = int(input("Enter your sp: "))
if (sp>cp):
    print("profit")
    pr = sp-cp
    print(pr)
else:
    print("No profit")


#Odd-Even
n = int(input("Enter a number : "))
if (n%2==0):
    print(f"{n} is even")
else: 
    print(f"{n} is odd")


#Greater or smaller

x = 50
n = int(input("Guess the number: "))
if(n>x):
    print("opps! too big")
elif(n<x):
    print("opps! too small")
else:
    print("Your guess is correct!!")