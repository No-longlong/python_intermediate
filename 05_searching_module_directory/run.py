# 파이썬은 모듈을 어떻게 찾을까?
import sys

# sys.path에 경로를 추가 - 리스트와 동일하게 처리
sys.path.append('C:\\Users\\codeit\\Desktop')

# 해당 리스트에 있는 디렉토리를 순서대로 찾는다. 없으면 오류.
print(sys.path)
