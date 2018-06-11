# dict - dictionary 字典

# list: []; tuple: (); dict: {};
dict1 = {'key1': 'value1', 'key2': 'value2'}  # Java Map

print(dict1['key1'])

dict2 = {'k1': True, 'k2': True, 'k3': 'value3'}

print(dict2['k2'])

dict2['k2'] = False

print(dict2['k2'])

# print(dict2['kl'])

print(dict2.get('kL'))
print(dict2.get('kL', -1))

print(dict2.pop('k1'))
# print(dict2.pop('k1'))

print(dict2.get('k1', -1))

# list

key = [1, 2, 3]
# dict2[key] = 'value'

dict2['k4'] = 123.456

print(dict2['k4'])

print(dict2.keys())

print(dict2.values())

print(dict2.items())


