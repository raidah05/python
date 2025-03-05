set0= {1,2,3}
print(set0)

set1= {1.0,'hello',(1,2,3)}
print(set1)

myset = {1,2,3,4,3212,4,3,2}
print(myset)

mysetm= set([1,2,3,4,5,32,1,4,1])
print(mysetm,"\n")

mysetn= set([1,2,4,5,32,1,4,1])
print('The orignal set:', mysetn)
mysetn.pop()
print("After removing", mysetn)

#intersection

x = {"yellow",'blue'}
y = {'green', 'blue'}
print(x)
print(y)
z = x.intersection(y)
a = x.union(y)
print('The intersection of x and y is', z)
print('The union of x and y is', a)



#Csymmetric diffrence

setx = {'yellow','blue'}
sety = {'yellow','green','pink'}
b = setx.intersection(sety)
c = setx.union(sety)
v = c-b
print(v)