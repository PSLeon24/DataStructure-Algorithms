class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.no = 0
        self.head = None
        self.current = None # 주목 노드

    def __len__(self):
        """연결 리스트의 노드 개수를 반환"""
        return self.no

    def search(self, data):
        cnt = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1
        
    def __contains__(self, data):
        return self.search(data) >= 0
    
    def add_first(self, data):
        ptr = self.head
        self.head = self.current = Node(data, ptr)
        self.no += 1

    def print_current_node(self):
        if self.current is None:
            print('주목 노드가 존재하지 않습니다.')
        else:
            print(self.current.data)

    def remove_first(self):
        if self.head is not None:
            self.head = self.current = self.head.next
        self.no -= 1

    def remove(self, p):
        if self.head is not None:
            if p is self.head:
                self.remove_first()
            else:
                ptr = self.head

                while ptr.next is not p:
                    ptr = ptr.next
                    if ptr is None:
                        return
                ptr.next = p.next
                self.current = ptr
                self.no -= 1

    def remove_current(self):
        self.remove(self.current)

    def next(self):
        """주목 노드를 한 칸 뒤로 진행"""
        if self.current is None or self.current.next is None:
            return False # 진행할 수 없음
        self.current = self.current.next
        return True


    def __iter__(self):
        return LinkedListIterator(self.head)

class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data

lst = LinkedList()
lst.add_first(5)
lst.add_first(4)
lst.add_first(3)
lst.add_first(2)

pos = lst.search(3)
if pos >= 0:
    print(f'{pos + 1}번째')
else:
    print('X')

lst.remove_current()
lst.print_current_node()
lst.next()