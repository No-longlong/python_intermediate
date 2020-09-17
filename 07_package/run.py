# import shapes.volume as vol
# print(vol.cube(3))

# from shapes.area import square
# print(square(3))

# from shapes import volume 이름이 volume 그 자체
# import shapes.volume 이름이 shapes.volume

import shapes
print(shapes.area.circle(2))
print(shapes.volume.cube(2))
# packages 디렉토리만 호출할 때에는 안에 있는 것은 import 되지 않음.
# 이것을 __init__으로 해결 가능.