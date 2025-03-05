import array as arr

num = arr.array('i',[1,2,3,4,5,4,3,2,1,7,89,3])
print('the orignal array', str(num))

print('the number of occurance of 3')
print(str(num.count(3)))

arr.array.reverse(num)
print(str(num))