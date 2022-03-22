key = []
for i in range(9):
  key.append(int(input()))

sum = sum(key)
finalList = []
check = False
for i in range(8):
  if check:
    break
  for j in range(i+1, 9):
    minus = key[i] + key[j]
    if (sum - minus == 100):
      finalList.append(i)
      finalList.append(j)
      check = True
      break

result = []
for i in range(9):
  if i in finalList:
    continue
  else:
    result.append(key[i])
result.sort()
for i in range(7):
  print(result[i])