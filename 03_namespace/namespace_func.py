#from area_01 import circle, square as sq
import area_01

def square(length):
    return 4 * length

print(dir())
print(square(7))
#print(sq(7))
print(area_01.square(7))

# 동일한 네임스페이스인 'square'로 정의되었을 때,
# 다른 모듈에서 불러온 square과, 현재 파이썬 내에 있는 def 중 "나중에 정의"된 square를 사용한다.
# print 바로 앞에 import를 붙이면 7 * 7 의 결과로 나온다. (모듈 불러오기가 더 최근에 네임스페이스(dir())에 올라갔기 때문)

#####################################################################
# 네임스페이스가 겹치지 않기 위해서는 두가지 방법이 있다.
# 1. from import를 할 때에 alias를 지정한다.
# 2. import로 모듈을 전체 불러온 뒤에, 모듈이름.함수 식으로 사용한다.

#####################################################################
# from 모듈 import * 가 권장되지 않는 이유
# namespace에 모든 함수가 다 올라가 버리기 때문.