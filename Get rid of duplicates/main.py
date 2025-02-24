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