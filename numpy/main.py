import numpy as np 

data_type = [('name','S15'),('class', int), ('height', float)]
students_details = [('Raidah',10,128.9), ('Tuna',10,120.9),('Anisha',10,121.5)]
studenys = np.array(students_details,dtype= data_type)

print("Orignal Array:")
print(studenys)
print("Sort by height:")
print(np.sort(studenys, order='height'))