# 백준 4673 셀프넘버
num = 1

# 리스트 10000개로 생성
result = []*10000

#  생성자 리스트에 담기
while(True):
    n_list = list(map(int, str(num)))
    sum = 0
    for i in range(len(n_list)):
        if i == 0:
            sum = n_list[i] + num
        else:
            sum += n_list[i]
    num += 1
    result.append(sum)
    if sum >= 10000:
        break

result2 = []*10000
num2 = 1
# 1 - 10000 까지 숫자가 담긴 리스트 생성
for j in range(10000):
    result2.append(num2)
    num2 += 1

# 셀프넘버인 값을 구하기 위해 10000까지 담긴 리스트에서 생성자가 담긴 리스트 차집합
set1 = set(result)
set2 = set(result2)
final = list(set2 - set1)
final.sort()
for k in range(len(final)):
    # 10000 보다 작거나 같은 셀프넘버이기에 9993 이하로 출력
    if final[k] <= 9993:
        print(final[k])