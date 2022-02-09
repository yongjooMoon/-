n = int(input())    # 입력받을 값
result = []         # 이름을 입력받을 리스트
result1 = []        # 첫번째 성적
result2 = []        # 두번째 성적
result3 = []        # 세번째 성적
for i in range(n):
    data = list(map(str, input().split()))
    result.append(data[0])
    result1.append(int(data[1]))
    result2.append(int(data[2]))
    result3.append(int(data[3]))

name_index = result1.index(max(result1))    # 첫번짹 성적 1등의 index구하기

# 각 과목 성적구하기
second_sort = sorted(result2)
third_sort = sorted(result3)
second_sort.reverse()
third_sort.reverse()
print(result[name_index], second_sort.index(result2[name_index]) + 1
      , third_sort.index(result3[name_index]) + 1)