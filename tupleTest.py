# tuple 元组

tuple1 = ('a', 'b', 'c', 'd')

print(tuple1)

# tuple1[0] = 'x'

# 1, 2, 3, 4

tuple2 = ()

print(tuple2)

tuple3 = (123.456,)

print(tuple3)  # (True)?

tuple4 = (1, 2, 3, [4, 5, 6])

print(tuple4)

print(tuple4[-1])

tuple4[-1].append(7)  # ?

print(tuple4[-1])

print(tuple4)

# tuple4[-1] = [4, 5, 6, 7]

print(tuple4)
