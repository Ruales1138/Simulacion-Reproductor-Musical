class DoubleNode:
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f'{self.value}'


class DoubleLinkedList:
    def __init__(self):
        self.__head: DoubleNode = None
        self.__tail: DoubleNode = None
        self.__size: int = 0

    def append(self, value):
        nuevo_nodo = DoubleNode(value)
        if self.__size == 0:
            self.__head = nuevo_nodo
            self.__tail = nuevo_nodo
        self.__size += 1

    def __repr__(self):
        return f'{self.__tail}'

ll = DoubleLinkedList()
print(ll)
ll.append(5)
print(ll)
ll.append(8)
print(ll)