class Node:
    def __init__(self, key, value, next):
        ''' Constructor '''
        self.key = key
        self.value = value
        self.next = next # refer to the back node

class ChainedHash:
    def __init__(self, capacity):
        self.capactiy = capacity
        self.table = [None] * self.capactiy

    def hash_value(self, key):
        if isinstance(key, int):
            return key % self.capactiy
        
    def add(self, key, value):
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return False
            p = p.next # focus on back node
        
        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True
    
    def remove(self, key):
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None # focus on front node

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True
            pp = p
            p = p.next
        return False
    
    def search(self, key, value):
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return p.value
            p = p.next
        return None

Menu = ['추가', '삭제', '검색', '덤프', '종료']

def select_menu():
    s = [m for m in Menu]
    while True:
        print(*s)
        n = input('명령어를 입력하세요: ')
        if n != '종료':
            return n
        
hash = ChainedHash(13)

while True:
    menu = select_menu()

    if menu == '추가':
        key = int(input('추가할 키를 입력하세요: '))
        val = input('추가할 값을 입력하세요: ')
        if not hash.add(key, val):
            print('추가를 실패하였습니다.')
        
    elif menu == '삭제':
        key = int(input('삭제할 키를 입력하세요.: '))
        if not hash.remove(key):
            print('삭제를 실패했습니다!')
    
    else:
        break