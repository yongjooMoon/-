# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

import sys
n = input()
result = list()
for i in range(int(n)):
  result.append(int(sys.stdin.readline()))

result.sort()
for i in result:
  sys.stdout.write(str(i)+'\n')