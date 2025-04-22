class Cancion:
    def __init__(self, titulo: str, artista: str, duracion: int):
        self.titulo: str = titulo
        self.artista: str = artista
        self.duracion: int = duracion

    def __repr__(self):
        return f'🎧 {self.titulo} - {self.artista} ({self.duracion}s)'


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
        else:
            nodo_anterior = self.__tail
            self.__tail.next = nuevo_nodo
            self.__tail = nuevo_nodo
            self.__tail.prev = nodo_anterior
        self.__size += 1
    
    def delete_first(self):
        if self.__size == 0:
            return
        if self.__size == 1:
            self.__head = None
            self.__tail = None
        else:
            current_node = self.__head.next
            current_node.prev = None
            self.__head = current_node
        self.__size -= 1

    def delete_end(self):
        if self.__size == 0:
            return
        if self.__size == 1:
            self.__head = None
            self.__tail = None
        else:
            current_node = self.__tail.prev
            current_node.next = None
            self.__tail = current_node
        self.__size -= 1

    def delete_by_name(self, value: str):
        current_node = self.__head
        while current_node is not None:
            if (current_node.value.titulo).lower() == value.lower():
                prev_node = current_node.prev
                next_node = current_node.next
                if current_node == self.__head:
                    self.__head = next_node
                if current_node == self.__tail:
                    self.__tail = prev_node
                if prev_node is not None:
                    prev_node.next = next_node
                if next_node is not None:
                    next_node.prev = prev_node
                self.__size -= 1
                return 'Cancion eliminada'
            current_node = current_node.next
        return 'Cancion no encotrada'

    def return_firs(self):
        return self.__head.value
    
    def search(self, value: str):
        current_node = self.__head
        while current_node is not None:
            if (current_node.value.titulo).lower() == value.lower():
                return True
            current_node = current_node.next
        return False

    def __repr__(self):
        string = ''
        current_node = self.__head
        while current_node is not None:
            #string += '(' + str(current_node.prev) + '<-' + str(current_node) + '->' + str(current_node.next) + ')'
            string += str(current_node) + '\n'
            current_node = current_node.next
        return string
    

class Queue:
    def __init__(self):
        self.queue = DoubleLinkedList()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        self.queue.delete_first()

    def dequeue_by_name(self, value):
        return self.queue.delete_by_name(value)

    def first(self):
        return self.queue.return_firs()
    
    def search(self, value):
        return self.queue.search(value)
    
    def __repr__(self):
        return str(self.queue)
    

class Reproductor:
    def __init__(self):
        self.playlist = Queue()
        
    def agregar_cancion(self, titulo: str, artista: str, duracion: int):
        if self.playlist.search(titulo) == True:
            return 'Cancion repetida'
        else:
            cancion = Cancion(titulo, artista, duracion)
            self.playlist.enqueue(cancion)

    def eliminar_cancion(self, titulo: str):
        return self.playlist.dequeue_by_name(titulo)

    def __repr__(self):
        return str(self.playlist)
    

