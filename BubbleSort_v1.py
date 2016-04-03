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
# print(maxCount)
while maxCount > 0:
    # print("xxx")
    for i in range(0, maxCount):
        # print(unsortedList[i])
        if unsortedList[i] > unsortedList[i+1]:
            # print("change ", unsortedList[i], ' and ', unsortedList[i+1])
            tmp = unsortedList[i]
            unsortedList[i] = unsortedList[i+1]
            unsortedList[i+1] = tmp
    maxCount -= 1

print("sorted list is : ", unsortedList)