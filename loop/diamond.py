rowSize = int(input("Enter the number of rows you want: "))
if rowSize%2==0:
    halfdiamond = int(rowSize/2)
else:
    halfdiamond = int(rowSize/2) +1
space = halfdiamond-1
for i in range(1, halfdiamond+1):
    for j in range(1 , space+1):
        