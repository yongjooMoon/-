# 통계학
import sys

n = int(sys.stdin.readline())
result = []
for i in range(n):
    result.append(int(sys.stdin.readline()))

# 산술평균 출력
if -1 < sum(list(result)) < 0:
    sys.stdout.write(0 +'\n')
else:
    sys.stdout.write(str(round(sum(list(result))/n)) +'\n')

# 중앙값 출력
result.sort()
sys.stdout.write(str(result[len(result)//2]) +'\n')

# 최빈값출력
maxCnt = {}
temp = []
for i in result:
    if i in maxCnt:
        maxCnt[i] += 1
    else:
        maxCnt[i] = 1
maxNum = 0
cnt = 0
for i, j in maxCnt.items():
    if j > maxNum:
        maxNum = j

for i, j in maxCnt.items():
    if j == maxNum:
        cnt += 1
        temp.append(i)

temp.sort()
binNumber = temp[0]
if cnt > 1:
    binNumber = temp[1]
sys.stdout.write(str(binNumber) +'\n')

# 범위출력
sys.stdout.write(str(result[n-1] - result[0]) +'\n')