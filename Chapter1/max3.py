# 세 정수 입력받아 최댓값 출력

print('세 정수를 입력하시오.(예: 1 3 5)')
'''
교재 코드
a = int(input('정수 a의 값을 입력하세요.: ))
b = int(input('정수 a의 값을 입력하세요.: ))
c = int(input('정수 a의 값을 입력하세요.: ))
'''
# 내 코드
a, b, c = map(int, input().split())

maximum = a
if maximum < b:
    maximum = b
if maximum < c:
    maximum = c

print(f'최댓값: {maximum}')
