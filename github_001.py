# 콘테스트(백준 5576) 정렬문제
result1 = []
result2 = []
for i in range(20):
    n = input()
    if i < 10:
        result1.append(int(n))
    else:
        result2.append(int(n))

result1.sort(reverse=True)
result2.sort(reverse=True)
sum1 = result1[0] + result1[1] + result1[2]
sum2 = result2[0] + result2[1] + result2[2]
print(sum1, sum2)