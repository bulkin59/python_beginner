

# input -> string 값으로 인식된다.

print("Enter your name!", "Hello People~")
somebody = input()
print("Hi", somebody)


# input -> float 값으로 변환해본다.

temperature = float(input("온도를 입력하세요 :"))
print(temperature)
print(type(temperature))


# 응용해보자
# 화씨변환기 프로그램

print("본 프로그램은 섭씨를 화씨로 변환해주는 프로그램입니다.")
print("변환하고 싶은 섭씨 온도를 입력해 주세요. : ")
c_temp=float(input())
f_temp=((9/5)*c_temp)+32
print("섭씨온도 : ", c_temp)
print("화씨온도 : ", f_temp)
