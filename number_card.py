# n = 행의 개수, m = 열의개수
n, m = map(int, input().split())

result = 0

# 입력받아야 열과 행의 값
for i in range(n):
    data = list(map(int, input().split()))
    # 입력받은 값중 가장 작은값
    min_value = min(data)
    # 가장 작은 값중 제일 큰값
    result = max(result, min_value)

print(result)