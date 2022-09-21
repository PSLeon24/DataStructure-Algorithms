# Thinking
'''
1 3 4 이 땐, 3
1 2 2 이 땐, 2
1 1 2 이 땐, 1

a >= b >= c ; b
a >= c >= b ; c
c >= b >= a ; b
c >= a >= b ; a
b >= a >= c ; a
b >= c >= a ; c
'''


def median(a, b, c):
    if a >= b:
        if b >= c:
            return b
        elif c >= a:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b


print('세 정수의 중앙값을 구합니다. 세 정수를 입력하세요 : ')
a, b, c = map(int, input().split())
print(f'중앙값은 {median(a, b, c)}입니다.')
