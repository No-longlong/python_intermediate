import area_01 # 모듈을 불러오는 방법

print(area_01.circle(2)) # 함수 1
print(area_01.square(3)) # 함수 2
print(area_01.PI) # 지정된 변수를 호출 출력

from area_01 import circle, square # 모듈을 불러오는 방법 2

print("직접 가져온 경우의 반지름 5의 넓이", circle(5))
print("직접 가져온 경우의 정사각형 7의 넓이", square(7))

import area_01 as ar # 모듈을 불러오는 방법 3 - 모듈 이름에 alias지정

print('alias 지정', ar.circle(2))

from area_01 import square as sq # 모듈을 불러오는 방법 4 - 모듈 내 함수에 alias 지정

print(sq(7))

from area_01 import * # 모듈을 불러오는 방법 5 - 모듈 내 함수를 전체 불러오기

print(circle(2)) # 함수 1
print(square(3)) # 함수 2
print(PI) # 지정된 변수를 호출 출력