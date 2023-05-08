from DS.list.listNode import ListNode


class LinkedListBasic:
    def __init__(self):
        self.__head = ListNode('dummy', None)
        self.__numItems = 0

    def insert(self, i, newItem):
        if i >= 0 and i <= self.__numItems:
            prev = self.__getNode(i - 1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            self.__numItems += 1
        else:
            print(f'index {i}: out of bound in insert()')

    def append(self, newItem):
        prev = self.__getNode(self.__numItems - 1)
        newNode = ListNode(newItem, prev.next)
        prev.next = newNode
        self.__numItems += 1

    def pop(self, i):

    def remove(self, x):

    def __findNode(self, x) -> (ListNode, ListNode):

    def __getNode(self, i: int) -> ListNode:

    def get(self, i: int):

    def index(self, x) -> int:

    def isEmpty(self) -> bool:

    def size(self) -> int:

    def clear(self):

    def extend(self, a):

    def copy(self):

    def reverse(self):

    def sort(self) -> None:
