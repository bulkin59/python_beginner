# 리스트 list를 배워보자

"""
indexing
index는 한 변수에 여러 데이터를 저장할 때 사용한다.
"""

#
colors = ["red", "blue", "green"]

# colors변수에서 첫번째 값을 출력해라
print(colors[0])

# colors변수에서 세번째 값을 출력해라
print(colors[2])

# colors 변수의 길이를 출력해라
print(len(colors))


"""
slicing
list의 값들을 잘라서 쓰는 것
주소값을 기반으로 부분값을 반환한다.
"""

# cities 변수에 도시 이름을 넣음
cities = ["서울", "부산", "대구", "인천", "대전", "광주", "울산", "수원"]

# 리스트의 길이를 출력
print(len(cities))

# 0부터 6까지 출력
print(cities[0:6])

# 전체범위 출력
print(cities[:])

# 지정범위를 넘어버리면 전체를 출력함
print(cities[-50:50])

# 두칸씩 뛰어넘어 출력해라. 역순으로 출력해라
print(cities[::2], "AND", cities[::-1])


"""
다양한 활용
"""

color1 = ["red", "blue", "green"]
color2 = ["orange", "black", "white"]

print(color1+color2)

print(len(color1))
print(len(color1+color2))

print(color1[0])
print(color1 * 2)

print("blue" in color2)

total_color = color1 + color2

print(total_color)


"""
리스트의 추가와 삭제
"""

# append 새로운 값을 추가하는 것
color1.append("white")
print(color1)

# extend 합치는 것
color1.extend(["black","purple"])
print(color1)

# insert 지정한 위치에 새로운 값을 추가하는 것
color1.insert(1,"orange")
print(color1)

# remove 값을 지우는 것
color1.remove("white")
print(color1)

# del 특정 위치의 값을 지우는 것
del color1[1]
print(color1)


"""
패킹과 언패킹
"""

# 패킹
t = [1, 2, 3]

# 언패킹
a, b, c = t

print(a)
print(b)
print(c)


"""
이차원 리스트 만들기 = 행렬 Matrix
"""

score0 = [43, 23, 12, 16, 17]
score1 = [13, 69, 70, 39, 20]
score2 = [16, 59, 30, 20]

midterm_score = [score0, score1, score2]
print(score0[2])

# 0과 2를 출력
print(midterm_score[0][2])


