def max3(a, b, c):
    maximum = a
    if maximum < b:
        maximum = b
    if maximum < c:
        maximum = c
    return maximum


print(f'max3(3, 2, 1) = {max3(3, 2, 1)}')
print(f'max3(3, 2, 2) = {max3(3, 2, 2)}')
print(f'max3(3, 1, 2) = {max3(3, 1, 2)}')
print(f'max3(3, 2, 3) = {max3(3, 2, 3)}')
print(f'max3(2, 1, 3) = {max3(2, 1, 3)}')
print(f'max3(3, 3, 2) = {max3(3, 3, 2)}')
print(f'max3(3, 3, 3) = {max3(3, 3, 3)}')
print(f'max3(2, 2, 3) = {max3(2, 2, 3)}')
print(f'max3(2, 3, 1) = {max3(2, 3, 1)}')
print(f'max3(2, 3, 2) = {max3(2, 3, 2)}')
print(f'max3(1, 3, 2) = {max3(1, 3, 2)}')
print(f'max3(2, 3, 3) = {max3(2, 3, 3)}')
print(f'max3(1, 2, 3) = {max3(1, 2, 3)}')

# max3.py 처럼 코딩하는 것보다, 함수로 만들어 쓰는 것이 더 유용
