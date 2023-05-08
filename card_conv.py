def card_conv(x: int, r: int) -> str:
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x > 0:
        d += dchar[x % r]
        x //= r
    
    return d[::-1]

if __name__ == "__main__":
    while True:
        while True:
            no = int(input('input N: '))
            if no > 0:
                break
        
        while True:
            cd = int(input('input R: '))
            if 2 <= cd <= 36:
                break
        
        print(f'{cd}진수로는 {card_conv(no, cd)}입니다.')

        retry = input("한 번 더 변환할까요?(Y...Yes / N...No): ")
        if retry in {'N', 'n'}:
            break