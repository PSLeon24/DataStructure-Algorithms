arr = [5, 2, 3, 7, 4, 1]
key = int(input("검색할 값을 입력하세요:"))

arr.append(key) #보초값 추가
i = 0
while True:
	if arr[i] == key:
		break
	i += 1
if i == len(arr)-1:
	print("not found")
else:
	print(f"검색값은 {arr[i]}에 있습니다.")
