# print(f'run file 이름: {__name__}')

# import area
# 원래는 True값이 출력되어야 하지만,
# area.py 내에 __name__값이 __main__인 경우에만
# (즉 직접 실행 되는 경우에만)
# 실행되도록 조건을 만들었으므로, 불러오는 run.py에서는
# 해당 print문이 보이지 않는다.


# print('run 파일 실행됨')

# 직접 실행할 때는 __name__의 이름이 __main__으로 바뀌고,
# 다른 곳에서 불러와서 사용될 때는 __name__이 해당 모듈의 이름으로 된다.
# 즉 __name__이 __main__인 경우에는 직접 실행했다는 의미이다.

############################################

# script는 프로그램 실행용 코드
# module은 임포트 하는 용도의 코드

############################

import area

def main():
    x = float(input('원의 지름을 입력해 주세요: '))
    print('지름이 {}인 원의 면적은 {}입니다.\n'.format(x, area.circle(x)))

    y = float(input('정사각형의 변의 길이를 입력해 주세요: '))
    print('변의 길이가 {}인 정사각형의 면적은 {}입니다.'.format(y, area.square(y)))

if __name__ == '__main__'
    main()

# 굳이 이렇게 두번 나누는 이유
# 가독성(main이 어딨는지 쉽게 알 수 있음)