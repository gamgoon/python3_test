import random

# 사용자의 리스트 크기 입력
while 1:
    try:
        listCount = int(input("리스트 크기 : "))
    except ValueError:
        print("숫자만 입력하삼")
        continue
    break

# unsorted list 생성
unsortedList = list(range(1, listCount+1))
random.shuffle(unsortedList)
print("unsorted list is : ", unsortedList)

# Sorting
maxCount = len(unsortedList) - 1

for i in range(maxCount):
    for j in range(maxCount - i):
        if unsortedList[j] > unsortedList[j+1]:
            unsortedList[j], unsortedList[j+1] = unsortedList[j+1], unsortedList[j]

print("sorted list is : ", unsortedList)