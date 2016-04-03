import random

strike_count = 0
ball_count = 0
game_count = 0

while 1:

    # 랜덤 중복 없는 숫자 3자리
    number_pool = list(range(0, 10))
    # print(number_pool)
    random.shuffle(number_pool)
    # print(number_pool)
    target_num = str(number_pool.pop()) + str(number_pool.pop()) + str(number_pool.pop())
    print(target_num)

    while strike_count < 3:

        strike_count = 0
        ball_count = 0

        origin_number = input("input number: ")

        try:
            input_number = int(origin_number)
        except ValueError:
            print("숫자만 입력하삼")
            continue

        str_input_num = str(origin_number)

        if len(list(str_input_num)) != 3:
            print("3자리 숫자 입력하삼")
            continue

        # print(str_input_num)
        tmp = set(str_input_num)

        if len(tmp) != 3:
            print("중복된 숫자는 입력하지마삼")
            continue

        index = 0
        for i in str_input_num:
            # print("str_input_num ", i)
            sub_index = 0
            for j in target_num:
                # print("target_num ", j)
                if i == j:
                    if index == sub_index:
                        strike_count += 1
                    else:
                        ball_count += 1
                sub_index += 1
            index += 1

        print(strike_count, " Strike")
        print(ball_count, " Ball")
        game_count += 1
    else:
        if strike_count == 3:
            print("you win")
        print("you played ", game_count , " times")
        strike_count = 0
        ball_count = 0
        game_count = 0

    while 1:
        yes_no = input("한판 더? (yes/no) :")
        if yes_no.upper != 'YES' and yes_no.upper != 'NO':
            continue
        else:
            break

    if yes_no.upper() == 'NO':
        break


