# n = 어떠한수, k = 나누기 할 값
n, k = map(int, input().split())

result = 0
while True:
    if n == 1:          # n값이 1되면 루프탈출
        break
    if n % k == 0:      # n 은 k로 나뉘어 질때만 나누기 가능하다
        n /= k

    if n % k != 0 and n != 1:   # n이 k로 나누어지지 않고 1이 아닐경우 -1을 한다
        n -= 1

    result += 1

print(result)