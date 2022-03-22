# 2959 백준)파이썬 거북이
x = list(map(int, input().split()))
x.sort(reverse=True)
print(x[1] * x[3])