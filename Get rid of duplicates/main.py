students_item = {'id1':
                 {'name': ['raidah'],
                  'class': ['V'],
                   'subject integration' : ['English','Science']},

                   'id2':
                   {'name': ['zaara'],
                    'class': ['V'],
                   'subject integration' : ['English','Science']},

                   
                   'id3':
                   {'name': ['raidah'],
                    'class': ['V'],
                   'subject integration' : ['English','Science']}

                   }

result = {}

for key,value in students_item.items():
    if value not in result.values():
        result[key] = value

print(result)



test = {'codingal': 2, 'is':2, 'best': 2, 'for': 2, 'coding': 1}
print("The orignal dic:"+ str(test))
k = 2 
res = 0 
for key in test:
    if test[key]== k:
        res = res +1

print(res)


country_code = {'India' : '0091',
                'Bangladesh': '0880',
                'Australia' : '0998'}

print("Country code for India-")
print(country_code.get('India','Not Found'))

print("Country code for japan-")
print(country_code.get('japan','Not Found'))