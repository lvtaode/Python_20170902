# iterable

from collections import Iterable

print(isinstance('abcd', Iterable))

print(isinstance(['a', 2, 3], Iterable))

print(isinstance(('a', 2, 3), Iterable))

print(isinstance(1234, Iterable))

list1 = ['a', 'b', 'c', 'd']

for index, value in enumerate(list1):
    print(index, value)

for x, y in [(1, 2), (3, 4), (5, 6)]:
    print(x, y)
