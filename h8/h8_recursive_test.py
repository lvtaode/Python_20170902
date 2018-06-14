# recursive 递归

# n! = n * (n - 1) * (n - 2) * ... * 1

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

print(fact(1))

print(fact(9))

# print(fact(1000))

# hanoi

# A B C n


