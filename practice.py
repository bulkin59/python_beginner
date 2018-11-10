"""
데이터 타입을 변환해보자.
data conversion
""""

# int 정수형으로 바꿔보자 10.XX -> 10
a = 10.3
b = 10.7
a = int(a)
b = int(b)
print(a+b)

# float 소수형으로 바꿔보자 10 -> 10.X
a = 10.3
b = 10
a = float(a)
b = float(b)
print(a)
print(b)
print(a+b)

# str  문자열형으로 바꿔보자 "--"
a = float(76.3)
b = a
print(a+b)

a = str(a)
b = str(b)
print(a+b)

# find type 무슨 타입인지 알아보자
type(a)
type(b)



"""
데이터 타입 변화시키는 것을 응용해보자1
"""


# input -> string
print("Enter your name!", "Hello People~")
somebody = input()
print("Hi", somebody)

# input -> float
temperature = float(input("온도를 입력하세요 :"))
print(temperature)
print(type(temperature))


# 화씨변환기 프로그램
print("본 프로그램은 섭씨를 화씨로 변환해주는 프로그램입니다.")
print("변환하고 싶은 섭씨 온도를 입력해 주세요. : ")
c_temp=float(input())
f_temp=((9/5)*c_temp)+32
print("섭씨온도 : ", c_temp)
print("화씨온도 : ", f_temp)