# 첫째 줄에 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 출력한다.

import sys
n = int(sys.stdin.readline())
result = list(map(int, sys.stdin.readline().split()))

result.sort()
sum = 0
mid = 0
for i in result:
  mid += i
  sum += mid
sys.stdout.write(str(sum)+'\n')