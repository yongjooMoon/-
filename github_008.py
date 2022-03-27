n = int(input())
result = []

for i in range(n):
    result.append(list(map(int, input().split())))

for i in range(n):
    k = 1
    for j in range(n):
        if i != j and result[i][0] < result[j][0] and result[i][1] < result[j][1]:
            k += 1
    print(k, end = " ")
