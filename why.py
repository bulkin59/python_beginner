
'''
[loop 응용]

숫자찾기 게임

1부터 100까지의 난수 발생할 때
사용자가 입력한 값이 맞을때까지 반복
맞추면 종료


왜 판별 문구가 제대로 작동하지 않지????
'''


# 난수 발생 함수 호출
import random
# 1부터 100 사이의 정수 난수 발생
guess_number = random.randint(1, 100)


print("")
print(guess_number)
print("숫자를 맞춰보세요 (1 ~ 100)")

user_input = int(input())
while (user_input != guess_number) :
    if user_input > guess_number :
        print("숫자가 정답보다 큽니다.")
    else :
        print("숫자가 정답보다 작습니다.")
    user_input = int(input())
else :
    print("정답입니다.",
          "입력한 숫자는 ", user_input, "입니다.")

