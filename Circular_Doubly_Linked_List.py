class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev or self
        self.next = next or self
        
class DoubleLinkedList:
    def __init__(self):
        self.no = 0
        self.head = self.current = Node() # Create a dummy node
        
    def __len__(self):
        return self.no

    def is_empty(self):
        return self.head.next is self.head

    def search(self, data):
        cnt = 0
        ptr = self.head.next
        while ptr is not self.head:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1
        
    def __contains__(self, data):
        return self.search(data) >= 0
    
    def print_current_node(self):
        if self.is_empty():
            print('주목 노드는 없습니다.')
        else:
            print(self.current.data)

    def print(self):
        ptr = self.head.next
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.next

    def print_reverse(self):
        ptr = self.head.prev
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.prev

    def next(self):
        if self.is_empty() or self.current.next is self.head:
            return False
        self.current = self.current.next
        return True
    
    def prev(self):
        if self.is_empty() or self.current.prev is self.head:
            return False
        self.current = self.current.prev
        return True
    
    def add(self, data):
        node = Node(data, self.current, self.current.next)
        self.current.next.prev = node
        self.current.next = node
        self.current = node
        self.no += 1

    def add_first(self, data):
        self.current = self.head
        self.add(data)

    def add_last(self, data):
        self.current = self.head.prev
        self.add(data)

    def remove_current_node(self):
        if not self.is_empty():
            self.current.prev.next = self.current.next
            self.current.next.prev = self.current.prev
            self.current = self.current.prev
            self.no -= 1
            if self.current is self.head:
                self.current = self.head.next

    def remove(self, p):
        ptr = self.head.next

        while ptr is not self.head:
            if ptr is p:
                self.current = p
                self.remove_current_node()
                break
            ptr = ptr.next

    def remove_first(self):
        self.current = self.head.next
        self.remove_current_node()

    def remove_last(self):
        self.current = self.head.prev
        self.remove_current_node()

    def clear(self):
        while not self.is_empty():
            self.remove_first()
        self.no = 0

    def __iter__(self):
        return DoubleLinkedListIterator(self.head)
    
    def __reversed__(self):
        return DoubleLinkedListReverseIterator(self.head)

class DoubleLinkedListIterator:
    def __init__(self, head):
        self.head = head
        self.current = head.next

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data

class DoubleLinkedListReverseIterator:
    def __init__(self, head):
        self.head = head
        self.current = head.prev

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.prev
            return data

lst = DoubleLinkedList()
lst.add_first(5)
lst.add_first(4)
lst.add_first(3)
lst.add_first(2)
lst.print()

pos = lst.search(3)
if pos >= 0:
    print(f'{pos + 1}번째')
else:
    print('X')

lst.remove_current_node()
lst.print_current_node()
lst.prev()
lst.print_current_node()
lst.next()