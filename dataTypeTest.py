# 整数

print(123)

print(0)

print(-1234567)

print(2147483648214748364821474836482147483648214748364821474836482147483648214748364821474836482147483648)

# 0-9, a, b, c, d, e, f

print(0xabcdef)

print(0x4E00)  # unicode 一 : 19968


# 浮点数

print(1.0)

print(-123.456)

print(1.234e10)

print(9.87654321e-10)

# 字符串 String

print('你好！')

print("您好！")

print("'")

print('"')

print('\'\"')

print("\'\"")

print('\\')

print('\\\t\\')  # \    \

print(r'\\\t\\')  # regexp

print(r'\\')

print('白日依山尽，\n黄河入海流。')

print('''白日依山尽，
黄河入海流。''')

# 布尔 true false

print(True)

print(False)

print(1 < 2)

print(1 > 2)

print('---------')
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print('---------')
print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not True)
print(not False)

print(None)

# score = input('input student\'s score:')

passed = False

if passed:
    print('passed...')
else:
    print('failed...')
