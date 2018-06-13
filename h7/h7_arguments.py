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


# 5. 命名关键字参数

def student1(name, age, **kw):
    if 'loc' in kw:
        print('loc', kw.get('loc'))
    if 'gender' in kw:
        print('gender', kw.get('gender'))


dict2 = {'loc': 'Beijing', 'gender': 'Male'}  # ?

print('loc' in dict2)

student1('Tom', 18, **dict2)


def student2(name, age, *, loc, gender):
    print('loc', loc)
    print('gender', gender)


student2('Jerry', 18, loc='', gender='')

student2('Tester', 20, **dict2)


def student3(name, age, *args, loc, gender):
    print(name, age, args, loc, gender)


student3('Tom', 18, loc='Shanghai', gender='Male')
student3('Jeery', 18, 1, 2, 3, 4, 5, True, False, 1.234, loc='Guangzhou', gender='Female')
student3('Jeery', 18, 1, loc='Guangzhou', gender='Female')


def student4(name, age, *args, loc, gender='Male'):
    print(name, age, args, loc, gender)


student4('Tom', 18, loc='Beijing')


# function argument: 位置 / 默认值 / 可变 / 关键字 / 命名关键字

def test_function(a, b, c=0, *args, d, **kw):
    pass


