n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin = [500, 100, 50, 10]

for don in coin:
    count += n // don  # 현재 금액에서 큰금액부터 거슬러주기
    n %= don
print(count)


# 그리디 알고리즘 가장 큰수 구하기 1
# n = 배열개수, m = 더하기 횟수, k = 연속더하기 횟수
# N ,M, K 를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

# 입력받은 수들 정렬
data.sort()
first = data[n-1]  # 가장 큰수
second = data[n-2] # 두번째로 큰수

result = 0

while True:
    for i in range(k):  # 가장 큰 수를 K번 더하기
        if m == 0:      # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1          # 더할때 마다 1씩 빼기
    if m == 0:          # m이 0이라면 반복문 탈출
        break
    result += second    # 두번째로 큰수 더하기
    m -= 1              # 더할때 마다 1씩 빼기
print(result)

# 그리디 알고리즘 가장 큰수 구하기 2
# n = 배열개수, m = 더하기 횟수, k = 연속더하기 횟수
# N ,M, K 를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

# 입력받은 수들 정렬
data.sort()
first = data[n-1]  # 가장 큰수
second = data[n-2] # 두번째로 큰수

count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += count * first
result += (m-count) * second
print(result)