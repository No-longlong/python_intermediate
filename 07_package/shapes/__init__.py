# init은 initialize라는 '초기화'라는 뜻
# 가장 먼저 init 파일에 있는 코드가 실행된다는 뜻

# print('__init__.py 파일 실행')

# from shapes import area, volume
# run.py에서 파이썬 패키지를 임포트할때 원래는 안되던게
# init에서 임포트를 해줌으로써 해결.
# 그러니 init 파일은 패키지를 임포트할 때
# 같이 임포트 하고자 하는 모듈을 적어주면 된다.

#from shapes.area import circle, square

########################################

PI = 3.14 # 모듈별로 PI를 지정하는 것은 의미가 없다.

__all__ = ['area', 'volume'] # 특수변수 all은 import * 를 할 때 가져오는 것을 정의