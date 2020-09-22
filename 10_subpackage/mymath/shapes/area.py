__all__ = ['PI', 'circle'] # from ~~.area import *
# 서클을 실행할 때만 실행되는 특수변수나 함수.


#from shapes import PI
PI = 3.14 # 상수는 대문자로 지정

def circle(radius):
    return PI * radius * radius

def square(length):
    return length * length


# 상대경로
from ..stats.average import data_mean
# 복잡해보이는 경우 절대경로가 더욱 직관적