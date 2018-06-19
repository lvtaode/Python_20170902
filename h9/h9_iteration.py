# iteration 迭代

# for ... in

list1 = [0, 1, 2, 3, 4, 5]

for i in list1:
    print(i)

dict1 = {'k1': 'v1', 'k2': 123, 'k3': False}

for tom in dict1:  # 隐式调用了: keys()
    print(tom, dict1[tom])

for key in dict1.keys():
    print(key)

for v in dict1.values():
    print(v)

for item in dict1.items():
    print(item[0], item[1])

for char in 'ABCEDFG':
    print(char)


