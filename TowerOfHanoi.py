def moveTower(disks, fromPeg, viaPeg, toPeg):
    if disks > 0:
        moveTower(disks-1, fromPeg, toPeg, viaPeg)
        if fromPeg:
            toPeg.append(fromPeg.pop())
            # print("------- move --------")
            # print("source : " + ''.join(str(e) for e in sourcePeg))
            # print("aux    : " + ''.join(str(e) for e in auxPeg))
            # print("target : " + ''.join(str(e) for e in targetPeg))
            # print("---------------------")
            displayTower()
        moveTower(disks-1, viaPeg, fromPeg, toPeg)


def displayTower():

    for i in range(1, numOfDisks + 1):
        try:
            sourceDotCnt = sourcePeg[numOfDisks - i]
        except IndexError:
            sourceDotCnt = 0

        try:
            auxDotCnt = auxPeg[numOfDisks - i]
        except IndexError:
            auxDotCnt = 0

        try:
            targetDotCnt = targetPeg[numOfDisks - i]
        except IndexError:
            targetDotCnt = 0
        # if len(sourcePeg)-1 >= numOfDisks - i:
        #     sourceDotCnt = sourcePeg[numOfDisks - i]
        # else:
        #     sourceDotCnt = 0
        # if len(auxPeg)-1 >= numOfDisks - i:
        #     auxDotCnt = auxPeg[numOfDisks - i]
        # else:
        #     auxDotCnt = 0
        # if len(targetPeg)-1 >= numOfDisks - i:
        #     targetDotCnt = targetPeg[numOfDisks - i]
        # else:
        #     targetDotCnt = 0
        print("{:^10}  {:^10}  {:^10}".format("*" * sourceDotCnt, "*" * auxDotCnt, "*" * targetDotCnt))
    print("{:^10}  {:^10}  {:^10}".format("SOURCE PEG", "AUX PEG", "TARGET PEG"))


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

displayTower()

# print("------- start --------")
# print("source : " + ''.join(str(e) for e in sourcePeg))
# print("aux    : " + ''.join(str(e) for e in auxPeg))
# print("target : " + ''.join(str(e) for e in targetPeg))
# print("---------------------")

moveTower(numOfDisks, sourcePeg, auxPeg, targetPeg)