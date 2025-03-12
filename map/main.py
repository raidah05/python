number1 = [1,2,3]
number2 = [4,5,6]
res = map(lambda x,y:x+y, number1,number2)
print('Addition of lists:')
print(list(res))

num = [1,2,3,4,5]
def sq(n):
    return n*n
square = list(map(sq, num))
print(square)


#Zip it!!
s1 ={2,3,4}
s2= {'a','b','c'}
s3 = list(zip(s1,s2))
print(s3,'\n')

l1 = [12,78,5]
l2 = [100,200,300]

for x ,y in zip(l1,l2[::-1]):
    print(x,y)


stocks = ['bata','zara','apex']
prices = [2234,5689,8998]
new_dict = {stocks : prices for stocks, prices in zip(stocks,prices)}
print('\n{}'.format(new_dict))




#exit

for i in range(10):
    if i ==5:
        print(exit)
        exit()