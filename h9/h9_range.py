# range 范围 列表生成式

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list1)

list2 = list(range(1, 1001))

print(list2)

print(range(1, 10))

list3 = []

for x in range(1, 11):
    list3.append(x * x)

print(list3)

list4 = [x * x for x in range(1, 11)]  # ***

print(list4)

list5 = [x * x for x in range(1, 11) if x % 2 == 0]

print(list5)

# 全排列

str1 = '123'
str2 = 'abc'

list6 = [m + n for m in str1 for n in str2]

print(list6)
