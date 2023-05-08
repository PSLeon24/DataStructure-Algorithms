arr = list(range(1, 11111111))
print(arr)


def binarySearch(arr, targetNum):
    start = 0
    end = len(arr) - 1
    while start <= end:
        midIndex = (start + end) // 2
        if arr[midIndex] == targetNum:
            return f'Result index: {midIndex}'
        elif arr[midIndex] < targetNum:  # targetNum이 arr[midIndex]보다 큰 경우 / 오른쪽 확인
            start = midIndex + 1
        elif arr[midIndex] > targetNum:  # targetNum이 arr[midIndex]보다 작은 경우 / 왼쪽 확인
            end = midIndex - 1
        print(f'start: {start}, end: {end}')
    return -1


print(binarySearch(arr, 12))
