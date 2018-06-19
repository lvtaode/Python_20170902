# recursive 递归

# n! = n * (n - 1) * (n - 2) * ... * 1 = n * (n - 1)!

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

'''
// Java:

private static void hanoi(String src, String with, String dest, int n) {
    if (n == 1) {
        System.out.print(src + "->" + dest);    
    } else {
        hanoi(src, dest, with, n - 1);
        System.out.print(src + "->" + dest);
        hanoi(with, src, dest, n - 1);
    }
}

public static void main(String[] args) {
    hanoi("A", "B", "C", 3);
}
'''


def hanoi(src, use, dest, n):
    if n == 1:
        print(src, '->', dest)
    else:
        hanoi(src, dest, use, n - 1)
        print(src, '->', dest)
        hanoi(use, src, dest, n - 1)


hanoi('A', 'B', 'C', 3)
