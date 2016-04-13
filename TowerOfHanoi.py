def moveTower(disks, fromPeg, viaPeg, toPeg):
    if disks > 0:
        moveTower(disks-1, fromPeg, toPeg, viaPeg)
        if fromPeg:
            toPeg.append(fromPeg.pop())
            print("------- move --------")
            print("source : " + ''.join(str(e) for e in sourcePeg))
            print("aux    : " + ''.join(str(e) for e in auxPeg))
            print("target : " + ''.join(str(e) for e in targetPeg))
            print("---------------------")
        moveTower(disks-1, viaPeg, fromPeg, toPeg)

numOfDisks = 0
while numOfDisks == 0:
    try:
        numOfDisks = int(input("디스크 개수 입력 (프로그램 종료는 0 ) : "))
        if numOfDisks == 0:
            print("프로그램 종료")
            exit()
    except ValueError:
        print("숫자만")
        numOfDisks = 0

sourcePeg = list(reversed(range(1, numOfDisks + 1)))
auxPeg = []
targetPeg = []

print("------- start --------")
print("source : " + ''.join(str(e) for e in sourcePeg))
print("aux    : " + ''.join(str(e) for e in auxPeg))
print("target : " + ''.join(str(e) for e in targetPeg))
print("---------------------")

moveTower(numOfDisks, sourcePeg, auxPeg, targetPeg)