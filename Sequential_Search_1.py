# 보초법
def search_list(array, target):
    i = 0
    array.append(target)
    while array[i] != target:
        i += 1
    
    return f'Found at index: {i}' if i != len(array) - 1 else 'Not found'

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 900))