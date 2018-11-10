'''
조건문 condition 을 배워보자

if 조건 판단의 기준 :
    수행 명령
elif 조건 판단의 기준 :
    수행 명령
else 조건 판단의 기준 :
    수행 명령

'''



print("Tell me your age")
myage = int(input("Age : "))

if myage < 30:
    print("당신은 구매 할 수 있습니다.")
else:
    print("당신은 구매 할 수 없습니다.")



print("===============================")


# 학점 계산하기

print("Tell me your score (1~100)")
score = float(input("score : "))

if score>=90 :
    print("학 점 : A")
elif score>=80 :
    print("학 점 : B")
elif score>=70 :
    print("학 점 : C")
else :
    print("학 점 : F")


'''
[연습문제]

결과물
당신이 태어난 연도를 입력하세요
1994
대학생

'''

print("당신이 태어난 연도를 입력하세요")
birth = int(input())

age = 2016 - birth + 1

if age <= 26 and age >= 20 :
    print("대학생")
elif age < 20 and age >= 17 :
    print("고등학생")
elif age < 17 and age >= 14 :
    print("중학생")
elif age < 14 and age >=8 :
    print("초등학생")
else :
    print("학생이 아닙니다")
