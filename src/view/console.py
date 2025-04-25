import sys
sys.path.append('src')
from model.reproductor import Reproductor
from model.barra import barra_progreso


class Console:
    def __init__(self):
        self.reproductor = Reproductor()
        self.opcion: int = 0
        self.aleatorio: bool = False
        self.porcentaje_adelantado: int = 0

    def crear_datos(self):
        self.reproductor.agregar('Bohemian Rhapsody', 'Queen', 12)
        self.reproductor.agregar('Another One Bites The Dust', 'Queen', 12)
        self.reproductor.agregar('Hotel California', 'Eagles', 11)
        self.reproductor.agregar('Smells Like Teen Spirit', 'Nirvana ', 14)
        self.reproductor.agregar('Something In The Way', 'Nirvana ', 14)
        self.reproductor.agregar('Soy Peor', 'Bad Bunny', 10)
        self.reproductor.agregar('Moscow Mule', 'Bad Bunny', 10)
        #self.reproductor.agregar('Dame tu cosita', 'El Chombo', 15)

    def imprimir(self):
        self.crear_datos()
        while self.opcion != 10:
            print('--------------------------------------------')
            print('📝 Menú Principal')
            print('🎸 Bienvenido a tu Playlist Interactiva 🎸')
            print('')
            print('1️⃣  Agregar canción')
            print('2️⃣  Avanzar a la siguiente canción')
            print('3️⃣  Retroceder a la canción anterior')
            print('4️⃣  Eliminar una canción')
            print('5️⃣  Mostrar canción en reproducción')
            print('6️⃣  Mostrar toda la playlist')
            print('7️⃣  Activar modo aleatorio')
            print('8️⃣  Adelantar una canción')
            print('9️⃣  Generar una subplaylist')
            print('🔟 Salir')
            print('11 Borrar artista con menos reproducciones')
            print('--------------------------------------------')
            self.opcion = input('Seleccione una opción: ')
            if self.opcion == '':
                self.opcion = 0
            else:
                self.opcion = int(self.opcion)

                if self.opcion == 1:
                    print('')
                    print('➕ Agregar una Canción')
                    titulo = input('Ingrese el título: ')
                    artista = input('Ingrese el artista: ')
                    duracion = int(input('Ingrese la duración (10-15 seg): '))
                    resultado = self.reproductor.agregar(titulo, artista, duracion)
                    print(resultado)

                if self.opcion == 2:
                    print('')
                    resultado = self.reproductor.avanzar()
                    print(resultado)

                if self.opcion == 3:
                    print('')
                    resultado = self.reproductor.retroceder()
                    print(resultado)

                if self.opcion == 4:
                    print('')
                    print('❌ Eliminar una Canción')
                    titulo = input('Ingrese el título de la canción a eliminar: ')
                    resultado = self.reproductor.eliminar(titulo)
                    print(resultado)

                if self.opcion == 5:
                    while True:
                        print('')
                        cancion_actual = self.reproductor.reproducir()
                        print('🎵 Ahora reproduciendo:')
                        print(f'{cancion_actual}                   ')
                        #barra_progreso(100, 1, self.porcentaje_adelantado)
                        barra_progreso(100, cancion_actual.duracion, self.porcentaje_adelantado)
                        self.porcentaje_adelantado = 0
                        if self.aleatorio is False:
                            self.reproductor.avanzar()
                        else:
                            resultado = self.reproductor.avanzar_aleatorio()
                            if resultado is True:
                                break
                        print('')
                        respuesta = input('Enter para seguir reproduciendo o "s" para salir: ')
                        if respuesta == 's':
                            break
                        print("\033[F\033[F\033[F\033[F\033[F\033[F", end="")

                if self.opcion == 6:
                    print('')
                    print(self.reproductor)

                if self.opcion == 7:
                    if self.aleatorio is False:
                        self.aleatorio = True
                        print('')
                        print('🔀 Modo aleatorio activado. ')
                    else:
                        self.aleatorio = False
                        print('')
                        print('🔀 Modo aleatorio desactivado. ')

                if self.opcion == 8:
                    cancion_actual = self.reproductor.reproducir()
                    print('')
                    respuesta = int(input('⏩ Ingrese el porcentaje de adelanto: '))
                    porcentaje = respuesta / 100
                    if porcentaje > 1:
                        self.reproductor.avanzar()
                        cancion_actual = self.reproductor.reproducir()
                        print(f'Avanzando a la siguiente cancion: {cancion_actual.titulo}')
                    else:
                        self.porcentaje_adelantado = porcentaje
                        print(f'⌛ Adelantando {int(cancion_actual.duracion * porcentaje)}s... de {cancion_actual.titulo}')

                if self.opcion == 9:
                    print('')
                    print('📑 Generar una Subplaylist')
                    titulos = input('Ingrese los títulos de las canciones a incluir en la subplaylist (separados por comas): ')
                    resultado = self.reproductor.crear_subplaylist(titulos)
                    print(resultado)
                    respuesta = input('1️⃣  Quiere reproducir esta nueva subplaylist? (si, no): ')
                    if respuesta == 'si':
                        self.reproductor.cambiar_playlist()

                if self.opcion == 11:
                    print('')
                    respuesta = self.reproductor.borrar_artista()
                    print(respuesta)

                
c = Console()
c.imprimir()