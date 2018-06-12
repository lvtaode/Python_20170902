# argument parameter 参数

# 1. 位置参数

# def power(x):
#     return x * x


# print(power(2))

def cube(x):
    return x * x * x


print(cube(2))


def power(x, n):
    p = 1
    while (n > 0):
        p = p * x
        n -= 1
    return p


print(power(2, 2))
print(power(2, 3))
print(power(3, 4))

print(power(1234, 1234))


# 2. 默认参数

def power2(x, n=2):
    p = 1
    while (n > 0):
        p = p * x
        n -= 1
    return p


print(power2(2, 3))
print(power2(2, 2))
print(power2(2))


def power3(x, n=2):
    p = 1
    while (n > 0):
        p = p * x
        n -= 1
    return p


def print_student_info(name, age, gender='Male', loc='Beijing'):
    print(name, age, gender, loc)
    return


print(print_student_info('Tom', 18))
print(print_student_info('Tom', 18, 'Female'))
print(print_student_info('Tom', 18, 'Female', 'Shanghai'))

print(print_student_info('Tom', 18, loc='Shanghai'))  # ?

# 3. 可变参数
print(max(-1, -2, -3, .4567))


def sum(*n):
    s = 0
    for i in n:
        s += i
    return s


print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sum(list1[0], list1[1], list1[-1]))

print(sum(*list1))
