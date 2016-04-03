print("구구단 몇단을 계산할까요?")
dan = int(input())

print(dan)

print("구구단", dan, "단을 계산합니다.")
for idx in range(1, 10):
    print(dan, 'X', idx, '=', dan * idx)
else:
    print("EOP")