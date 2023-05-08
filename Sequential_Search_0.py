def search_list(array, target):
    n = len(array)
    for i in range(n):
        if target == array[i]:
            return f'{i+1}번째에 있는 {target}을 찾았습니다.'
    return -1

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 900))