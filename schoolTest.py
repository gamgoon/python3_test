print("당신이 태어난 년도를 입력하세요")
year = int(input())
age = 2016 - year + 1
school = "학생이 아닙니다."

if 20 <= age <= 26:
    school = "대학생"
elif 17 <= age < 20:
    school = "고등학생"
elif 14 <= age < 17:
    school = "중학생"
elif 8 <= age < 14:
    school = "초등학생"

print(school)