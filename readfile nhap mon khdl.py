t=r'c:\Users\Chinh\Desktop\VNUIS 22070554.txt'

"""
file = open(file=t, mode='r')
text = file.readlines()
print(text)

"""
"""
with open(file=t, mode="a") as f:
    f.write('ISTEPS dance club')

"""
"""

data_dictionary = {'books': 12,
                   'articles': 100,
                   'subjects': ['math',
                                'programming',
                                'data science']}
import json
json_string = json.dumps(data_dictionary)
print(json_string)

with open('reading.json', 'w') as f:
    json.dump(data_dictionary, f)

with open('reading.json') as f:
    loaded_data = json.load(f)
print(loaded_data)

"""

import pickle as pk
data_dictionary = { 'books': 12,
                   'articles':100,
                   'subjects': ['math',
                                'programming',
                                'data science']}
with open('reading.pk', 'wb') as f:
    pk.dump(data_dictionary, f)

print('\n-----\n');
with open('readings.pk', 'rb') as f:
    data = pk.load(f)
print(data)