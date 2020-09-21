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

# import shapes # 원래 안되었던 패키지 불러오기
# print(shapes.circle(2))
# print(shapes.square(2))
# 패키지만 불러오면
# 먼저 __init__.py을 호출한다.
# __init__.py 내부에서 import 하는 방식을
# from shapes.area import circle 을 통해서
# 바로 함수에 접근할 수 있도록 사용 가능
# 이러한 방식은 상황에 따라 유용하게 사용 가능

from shapes import PI # init 파일 안에 있는 PI변수 가져오기 1

# import shapes
# PI = shapes.PI # init 파일 안에 있는 PI변수 가져오기 1

##################### __all__
# 모듈을 임포트할 때 from <module> import *를 하면 모듈의 모든 내용이 임포트됩니다.
# 하지만 모듈 대신 패키지에 from <package> import *를 하면 패키지 안에 있는 게 아무것도 임포트되지 않습니다.

# from shapes import * # 특수변수 PI를 제외하면 가져오지 않는다.
# print(dir()) # 이는 __init__ 파일을 수정해줘야 한다.

from shapes.area import * # area.py에 __all__을 직접 지정해줘도 된다.
print(dir())