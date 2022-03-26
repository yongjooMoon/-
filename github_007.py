# 2231 분해합

import sys

n = int(sys.stdin.readline())

num = 1
minResult = 0
for i in range(n):

    result = num + sum(list(map(int, str(num))))

    if result == n:
        minResult = num
        break
    num += 1
sys.stdout.write(str(minResult)+'\n')