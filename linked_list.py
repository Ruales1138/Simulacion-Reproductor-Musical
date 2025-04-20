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

    def return_firs(self):
        return self.__head.value

    def __repr__(self):
        string = ''
        current_node = self.__head
        while current_node is not None:
            #string += '(' + str(current_node.prev) + '<-' + str(current_node) + '->' + str(current_node.next) + ')'
            string += '(' + str(current_node) + ')'
            current_node = current_node.next
        return string
    

class Queue:
    def __init__(self):
        self.queue = DoubleLinkedList()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        self.queue.delete_first()

    def first(self):
        return self.queue.return_firs()
    
    def __repr__(self):
        return str(self.queue)
    

class Reproductor:
    def __init__(self):
        self.playlist = Queue()
        
    def agregar_cancion(self, titulo: str, artista: str, duracion: int):
        cancion = Cancion(titulo, artista, duracion)
        self.playlist.enqueue(cancion)

    def __repr__(self):
        return str(self.playlist)

r = Reproductor()
r.agregar_cancion('Bohemian Rhapsody', 'Queen', 12)
print(r)
r.agregar_cancion('Hotel California', 'Eagles', 11)
print(r)
r.agregar_cancion('Smells Like Teen Spirit', 'Nirvana ', 14)
print(r)
r.agregar_cancion('Soy Peor', 'Bad Bunny', 10)
print(r)