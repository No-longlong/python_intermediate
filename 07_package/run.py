# import shapes.volume as vol
# print(vol.cube(3))

# from shapes.area import square
# print(square(3))

# from shapes import volume 이름이 volume 그 자체
# import shapes.volume 이름이 shapes.volume

# import shapes
# print(shapes.area.circle(2))
# print(shapes.volume.cube(2))
# packages 디렉토리만 호출할 때에는 안에 있는 것은 import 되지 않음.
# 이것을 __init__으로 해결 가능.

########################
# # init 파일 테스트
# import shapes.volume

import shapes # 원래 안되었던 패키지 불러오기
print(shapes.circle(2))
print(shapes.square(2))
# 패키지만 불러오면
# 먼저 __init__.py을 호출한다.
# __init__.py 내부에서 import 하는 방식을
# from shapes.area import circle 을 통해서
# 바로 함수에 접근할 수 있도록 사용 가능
# 이러한 방식은 상황에 따라 유용하게 사용 가능

from shapes import PI # init 파일 안에 있는 PI변수 가져오기 1

import shapes
PI = shapes.PI # init 파일 안에 있는 PI변수 가져오기 1