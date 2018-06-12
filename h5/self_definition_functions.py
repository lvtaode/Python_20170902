# 自定义函数

# def: definition

def self_abs(n):
    if not isinstance(n, (int, float)):
        raise TypeError('bad operand type')
    if n > 0:
        return n
    else:
        return -n


print(self_abs(-123))


# 定义函数 area / perimeter 求圆形的面积和周长，并测试

def circle_area(r):
    return 3.14 * r * r


print(circle_area(1.23))


def circle_perimeter(r):
    return 3.14 * r * 2


print(circle_perimeter(1.23))


def nothing():
    pass


print(nothing())


# print(self_abs('x'))  # TypeError: '>' not supported between instances of 'str' and 'int'

# print(abs('x'))  # TypeError: bad operand type for abs(): 'str'

def none_return_func(x, y):
    x + y
    return


print(none_return_func(1, 2))


def multiple_return_func(x, y):
    return x, y


a, b = multiple_return_func(1, 2)

print(a, b)

print(multiple_return_func(1, 2))  # tuple

# int i, j, k = 0;

i, j, k = 0, 1, 2

print(i, j, k)
