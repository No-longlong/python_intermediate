# 원의 면적을 구해주는 area

print(f'area 모듈 이름: {__name__}')
PI = 3.14 # 상수는 대문자로 지정

def circle(radius):
    return PI * radius * radius

def square(length):
    return length * length

# 모듈을 import 하면 밑에 코드가 출력된다.
# print(circle(2) == 12.56)
# print(circle(5) == 78.5)
#
# print(square(2) == 4)
# print(square(5) == 25)

# __name__ (DUNDER를 추가)
# __main__  # 파이썬 파일을 직접 실행할 때 area의 name은 __main__이 된다.

if __name__ == '__main__': # area.py를 직접 실행할때만 실행되도록
    print(circle(2) == 12.56)
    print(circle(5) == 78.5)

    print(square(2) == 4)
    print(square(5) == 25)

###############################################

# 함수들을 테스팅 하는 메인 함수
def main():
    print(circle(2) == 12.56)
    print(circle(5) == 78.5)

    print(square(2) == 4)
    print(square(5) == 25)

if __name__ == '__main__':
    main()