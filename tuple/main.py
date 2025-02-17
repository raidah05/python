x = ("tuple", False,3.2,5)
print(x)

y = x +(400,)
print(y)

z = (50,40,30,60,40,30,)
print(z.count(30))

a = (1,2,3,4,5,6,7,8,9,0)
slice4 = a[4:7]
print(slice4)

slice40 = a[:9]
print(slice40)


#palindrome

def palind(r):
    e = len(r) - 1
    s = 0 
    while (s<e):
        if(r[s] != r[e]):
            return False
        s +=1
        e -=1
    return True

r =(1,2,3,4,5,5,4,3,2,1)

if(palind(r)):
    print("The tuple is flip-flop")
else:
    print("The tuple is not flip-flop")