n = int(input())

if n < 100:
    print(n)
else:
    cnt = 0
    for i in range(100, n + 1):
        result = list(map(int, str(i)))
        a = result[0] - result[1]
        b = result[1] - result[2]

        if a == b:
            cnt += 1
    print(cnt + 99)