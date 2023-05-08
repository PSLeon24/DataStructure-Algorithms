class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def top(self):
        return self.items[-1]
    
    def isEmpty(self):
        return not self.items

'''
Stack Structure
   Top
[ ]
[ ]
[ ]
   Bottom

후입선출 LIFO(Last In First Out)
- 나중에 들어온게 먼저 나감

'''

stk = Stack()
print(f'Stack Object: {stk}')

print(stk.isEmpty()) # 처음에는 비어있으므로 True
stk.push(10) # Top - 가장 먼저 들어온 것
stk.push(7)
stk.push(3) # Bottom - 가장 마지막에 들어온 것
print(stk.items)
print(stk.top()) # 3 출력

print(stk.pop()) # 3 제거 후 출력

print(stk.items) # [10, 7]
print(stk.isEmpty()) # 객체가 비어있지 않으므로 False

print(stk.pop()) # 7 제거
print(stk.pop()) # 10 제거
print(stk.items)
print(stk.isEmpty()) # 객체가 비어있으므로 True