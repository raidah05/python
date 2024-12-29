n = int(input("Enter the number of rows you want: "))

for i in range(n):
    for j in range(i+1):
        print("*" , end=" ")
    print()
    
for i in range(n):
    for j in range(n-i-1):
        print("*" , end=" ")
    print()
    