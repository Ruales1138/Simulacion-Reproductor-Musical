import random

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
                deleted_node = current_node.value
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
                return deleted_node
            current_node = current_node.next
        return False
    
    def search(self, value: str):
        current_node = self.__head
        while current_node is not None:
            if (current_node.value.titulo).lower() == value.lower():
                return current_node
            current_node = current_node.next
        return False
    
    def search_by_artist(self, name: str):
        current_node = self.__head
        count = 0
        songs = []
        while current_node is not None:
            if (current_node.value.artista).lower() == name.lower():
                count += 1
                songs.append(current_node.value.titulo)
            current_node = current_node.next
        return count, songs
    
    def return_firs(self):
        return self.__head
    
    def return_last(self):
        return self.__tail
    
    def return_size(self):
        return self.__size

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
        self.__queue = DoubleLinkedList()

    def enqueue(self, value):
        self.__queue.append(value)

    def dequeue(self):
        self.__queue.delete_first()

    def dequeue_by_name(self, value):
        return self.__queue.delete_by_name(value)

    def first(self):
        return self.__queue.return_firs()
    
    def last(self):
        return self.__queue.return_last()
    
    def size(self):
        return self.__queue.return_size()
    
    def search(self, value):
        return self.__queue.search(value)
    
    def search_by_artist(self, name):
        return self.__queue.search_by_artist(name)
    
    def __repr__(self):
        return str(self.__queue)
    

class Reproductor:
    def __init__(self):
        self.playlist = Queue()
        self.subplaylist = Queue()
        self.aux_playlist = Queue()
        self.cancion_actual = None
        self.artists = {}
        
    def agregar(self, titulo: str, artista: str, duracion: int):
        if self.playlist.search(titulo) is not False:
            return '🚫 Cancion repetida'
        else:
            count, songs = self.playlist.search_by_artist(artista)
            if count == 0:
                self.artists[artista] = 1
            else:
                num = self.artists[artista]
                num += 1
                self.artists[artista] = num

            cancion = Cancion(titulo, artista, duracion)
            self.playlist.enqueue(cancion)
            print(self.artists)
            return '✅ Canción agregada exitosamente. '
        
    def eliminar(self, titulo: str):
        resultado = self.playlist.dequeue_by_name(titulo)
        if resultado is not False:
            num = self.artists[resultado.artista]
            num -= 1
            self.artists[resultado.artista] = num
            return '✅ Canción eliminada exitosamente.'
        else:
            return '🚫 No se encontro la cancion'
        
    def avanzar(self):
        if self.cancion_actual is not None:
            self.cancion_actual = self.cancion_actual.next
            if self.cancion_actual is not None:
                return f'Siguiente cancion: {self.cancion_actual}'
            else:
                self.cancion_actual = self.playlist.first()
                return f'Siguiente cancion: {self.cancion_actual}'
        else:
            self.cancion_actual = self.playlist.first().next
            return f'Siguiente cancion: {self.cancion_actual}'
    
    def avanzar_aleatorio(self):
        cantidad_de_canciones = self.playlist.size()
        if cantidad_de_canciones == 1:
            titulo = self.cancion_actual.value.titulo
            cancion_eliminada = self.playlist.dequeue_by_name(titulo)
            cancion = Cancion(cancion_eliminada.titulo, cancion_eliminada.artista, cancion_eliminada.duracion)
            self.aux_playlist.enqueue(cancion)
            self.playlist = self.aux_playlist
            return True
        if cantidad_de_canciones > 1:
            numero_aleatorio = random.randint(1, cantidad_de_canciones-1)
            titulo = self.cancion_actual.value.titulo
            for i in range(numero_aleatorio):
                self.avanzar()
            cancion_eliminada = self.playlist.dequeue_by_name(titulo)
            cancion = Cancion(cancion_eliminada.titulo, cancion_eliminada.artista, cancion_eliminada.duracion)
            self.aux_playlist.enqueue(cancion)

    def retroceder(self):
        if self.cancion_actual is not None:
            self.cancion_actual = self.cancion_actual.prev
            if self.cancion_actual is not None:
                return f'Anterior cancion: {self.cancion_actual}'
            else:
                self.cancion_actual = self.playlist.last()
                return f'Anterior cancion: {self.cancion_actual}'
        else:
            self.cancion_actual = self.playlist.last()
            return f'Anterior cancion: {self.cancion_actual}'
        
    def reproducir(self):
        if self.cancion_actual is None:
            self.cancion_actual = self.playlist.first()
        return self.cancion_actual.value
    
    def crear_subplaylist(self, titulos):
        lista_de_titulos = titulos.split(',')
        contador = 0
        for titulo in lista_de_titulos:
            titulo = titulo.strip()
            if self.playlist.search(titulo) is not False:
                cancion = self.playlist.search(titulo)
                nueva_cancion = Cancion(cancion.value.titulo, cancion.value.artista, cancion.value.duracion)
                self.subplaylist.enqueue(nueva_cancion)
                contador += 1
        return f'✅ Subplaylist creada con {contador} canciones'
    
    def cambiar_playlist(self):
        copia = self.playlist
        self.playlist = self.subplaylist
        self.subplaylist = copia

    def borrar_artista(self):
        artista_menor = ''
        numero_menor = 100
        for clave, valor in self.artists.items():
            if valor < numero_menor:
                numero_menor = valor
                artista_menor = clave
        count, songs = self.playlist.search_by_artist(artista_menor)
        for titulo in songs:
            self.eliminar(titulo)
        return artista_menor, songs

    def tamaño(self):
        return self.playlist.size()

    def __repr__(self):
        return str(self.playlist)