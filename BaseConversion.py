print("This is program for converting a decimal number (10-base) to hex, oct, or binary number")
print("If you input 0, this program will be finished")

convertorType = ['hex', 'oct', 'bin']


def convertValue(inputNumber, convType):

    typeVlu = 2
    if convType.upper() == 'OCT':
        typeVlu = 8
    elif convType.upper() == 'HEX':
        typeVlu = 16

    resultList = []

    a, b = divmod(inputNumber, typeVlu)
    resultList.insert(0, b)
    while a > 0:
        a, b = divmod(a, typeVlu)
        resultList.insert(0, b)

    return displayResult(resultList, convType)


def displayResult(resultList, convType):
    resultStr = ""
    for i in resultList:
        if convType.upper() == 'HEX':
            if i == 10:
                resultStr += "A"
            elif i == 11:
                resultStr += "B"
            elif i == 12:
                resultStr += "C"
            elif i == 13:
                resultStr += "D"
            elif i == 14:
                resultStr += "E"
            elif i == 15:
                resultStr += "F"
            else:
                resultStr += str(i)
        else:
            resultStr += str(i)
    return resultStr

while 1:
    try:
        inputNumber = int(input("Input Decimal Number: "))
    except ValueError:
        print("숫자만 입력해!!")
        continue

    if inputNumber == 0:
        print("Program Finish!")
        break

    message = ""
    idx = 0
    for i in convertorType:
        message += i
        idx += 1
        if idx < len(convertorType):
            message += ", "

    convType = input("Choose conversion type: " + message + "\n")

    while convType not in convertorType:
        convType = input("Choose conversion type: " + message + "\n")

    print("Decimal Number " + str(inputNumber) + " is converted to " + convType.upper() + " type")
    print(convertValue(inputNumber, convType))