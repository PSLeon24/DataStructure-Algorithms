from enum import Enum

class Status(Enum):
    OCCUPIED = 0
    EMPTY = 1
    DELETED = 2

class Bucket:
    def __init__(self, key = None, value = None, stat = Status.EMPTY):
        ''' Constructor '''
        self.key = key
        self.value = value
        self.stat = stat

    def set(self, key, value, stat):
        self.key = key
        self.value = value
        self.stat =stat

    def set_status(self, stat):
        self.stat = stat

class OpenHash:
    def __init__(self, capacity):
        self.capactiy = capacity
        self.table = [Bucket()] * self.capactiy

    def hash_value(self, key):
        if isinstance(key, int):
            return key % self.capactiy
        
    def rehash_value(self, key):
        return (self.hash_value(key) + 1) % self.capactiy
    
    def search_node(self, key):
        hash = self.hash_value(key)
        p = self.table[hash]

        for i in range(13):
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            hash = self.rehash_value(hash)
            p = self.table[hash]
        return None
    
    def search(self, key):
        p = self.search_node(key)
        if p is not None:
            return p.value
        else:
            return None

    def add(self, key, value):
        if self.search(key) is not None:
            return False
        
        hash = self.hash_value(key)
        p = self.table[hash]
        for i in range(self.capactiy):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(hash)
            p = self.table[hash]
        return False
    
    def remove(self, key):
        p = self.search_node(key)
        if p is None:
            return False
        p.set_status(Status.DELETED)
        return True
    
    def dump(self):
        for i in range(13):
            print(f'{i:2} ', end='')
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value})')
            elif self.table[i].stat == Status.EMPTY:
                print('--- 미등록 ----')
            elif self.table[i].stat == Status.DELETED:
                print('--- 삭제 완료 ---')

Menu = ['추가', '삭제', '검색', '덤프', '종료']

def select_menu():
    s = [m for m in Menu]
    while True:
        print(*s)
        n = input('명령어를 입력하세요: ')
        if n != '종료':
            return n
        
hash = OpenHash(13)

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

    elif menu == '검색':
        key = int(input('검색할 키를 입력하세요.: '))
        t = hash.search(key)
        if t is not None:
            print(f'검색한 키를 값는 값은 {t}입니다.')
        else:
            print('Not found')

    elif menu == '덤프':
        hash.dump()
    
    else:
        break