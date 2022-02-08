def factorial_interative(n):
    result = 1

    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return  n * factorial_recursive(n - 1)

print(factorial_interative(5))
print(factorial_recursive(5))

import sys

sys.setrecursionlimit(10**7)

def factorial_recursive(n):
    if n <= 1:
        return 1
    return  n + factorial_recursive(n - 1)

a = int(input())
print(factorial_recursive(a))