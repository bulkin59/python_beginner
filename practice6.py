"""

반복문 loop을 배워보자

정해진 동작을 반복적으로 수행하게 하는 명령문
'''

'''
for문
    반복 실행횟수를 정확히 할때 사용

for 변수명 in 시작조건, 종료 조건 :
    수행 명령
"""
# 리스트로 반복하기
for loop in [1,2,3,4,5]:
    print("hello")

for loop in [1,2,3,4,5]:
    print(loop)

# 범위로 반복하기 (0부터 맨끝값 -1까지 반복)
for loop in range(0,2) :
    print("hello")

# 문자열로 반복하기
for i in "abcdef" :
    print(i)

# 리스트 문자열로 반복하기
for j in ["apple", "berry", "banana"] :
    print(j)

# 간격을 두고 세기
# 1부터 10-1까지 2 간격으로 반복
for k in range(1, 10, 2) :
    print(k)

# 역순으로 반복문 수행
# 10부터 1+1까지 -1 간격으로 반복
for m in range(10, 1, -1) :
    print(m)



print("====")

"""
while문
    반복 실행횟수가 명확하지 않을 때 사용
    
while 조건의 판단 기준
    수행 명령
    
"""

i = 1
while i < 10 :
     print (i)
     i += 1


print("====")

'''
반복의 제어
brak
continue
else
'''

# break
# 0부터 10-1까지인데 5에서 멈춰라
for i in range(10) :
    if i == 5:
        break
    print(i)
print("End of Program")


# continue
# 0부터 10-1까지인데 5 값에서 건너뛰어라
for j in range(10) :
    if j == 5 :
        continue
    print(j)
print("End of Program")



# else
for k in range(10) :
    print (o)
else :
    print("End of Program")




