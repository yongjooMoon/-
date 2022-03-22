import sys
n ,m = list(map(int, input().split()))
card = list(map(int, input().split()))

sum = 0
result = []
chk = True
for i in range(n-2):
    if chk == False:
        break
    for j in range(i+1, n-1):
        if chk == False:
            break
        for k in range(j+1, n):
            sum = card[i] + card[j] + card[k]
            if sum == m:
                chk = False
                break
            elif sum < m:
                result.append(sum)

if chk == False:
    print(m)
else:
    # print(result.sort(reverse=True)[0])
    result.sort()
    print(result[-1])