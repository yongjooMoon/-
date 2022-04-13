# 베스트셀러

n = int(input())
book = []
for i in range(n):
    book.append(input())

# 입력된 책들의 중복을 제거하여 책 종류만 리스트에 담는다.
bookList = list(set(book))

result = []

# 책 종류별로 몇권의 책이 있는지 개수를 리스트에 담는다.
for i in bookList:
    cnt = 0
    for j in book:
        if i == j:
            cnt += 1
    result.append(cnt)

overlap = 0
temp = []
# 책 종류별 개수와 현재 존재하는 책들중 가장 큰값을 비교하여 temp  임시 테이블에 담는다.
for i in range(len(result)):
    if result[i] == max(result):
        overlap += 1
        temp.append(bookList[i])

# max 값이 2개 이상인경우 책종류를 오름차순하여 첫번째 값의 책을 프린트해준다.
if overlap > 1:
    temp.sort()
    print(temp[0])
else:
    print(temp[0])