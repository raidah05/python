num = int(input("Enter the number: "))
t = num 
numlen = 0
while t > 0:
    numlen = numlen + 1
    t = int(t/10)
    
if numlen>= 4:
    numlen= int(numlen/2)
    chk = 0
    while num>0:
        rem = num%10
        if chk == numlen:
            midOne = rem
        elif chk == (numlen - 1):
            midtwo = rem
        num = int(num/10)
        chk = chk+1
    product = midOne*midtwo
    print("product of mid-digit is" , product)
else:
    print("The number is not 4-digit or more")