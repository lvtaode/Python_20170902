# 4. 关键字参数


def sum(*n):
    pass


def student(name, age, **kw):
    print('name:', name, 'age:', age, 'keywords:', kw)


student('Tom', 18)

student('Jerry', 18, loc='Beijing')

student('Jerry', 18, loc='Beijing', gender='Female')

dict1 = {'loc': 'Shanghai', 'gender': 'Male', 'married': False}

student('Tester', 20, loc=dict1['loc'], gender=dict1['gender'])

student('Tester', 20, **dict1)
