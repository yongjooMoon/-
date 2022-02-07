n = int(input())    # n*m 사이즈 지도
x, y = 1, 1
plans = input().split() # 상하좌우 위치 성정
nx, ny = 1, 1

for i in plans:
    if i == "R":
        ny = y + 1

    if i == "L":
        ny = y - 1

    if i == "U":
        nx = x - 1

    if i == "D":
        nx = x + 1

    # 지도에서 벗어날 경우 제외
    if nx < 1 or ny < 1 or nx > n or ny > n:
        print("test5")
        continue

    x, y = nx, ny

print(x, y)