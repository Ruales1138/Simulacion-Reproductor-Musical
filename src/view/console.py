import sys
sys.path.append('src')
from model.reproductor import Reproductor
from model.barra import barra_progreso


reproductor = Reproductor()
reproductor.agregar('Bohemian Rhapsody', 'Queen', 12)
reproductor.agregar('Hotel California', 'Eagles', 11)
reproductor.agregar('Smells Like Teen Spirit', 'Nirvana ', 14)
reproductor.agregar('Soy Peor', 'Bad Bunny', 10)
reproductor.agregar('Soy Peor', 'Bad Bunny', 10)

# print(r.eliminar_cancion('Bohemian Rhapsody'))
# print(r)

opcion = 0

while opcion != 10:
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
    print('--------------------------------------------')
    opcion = input('Seleccione una opción: ')
    if opcion == '':
        opcion = 0
    else:
        opcion = int(opcion)
        if opcion == 1:
            print('')
            print('➕ Agregar una Canción')
            titulo = input('Ingrese el título: ')
            artista = input('Ingrese el artista: ')
            duracion = int(input('Ingrese la duración (10-15 seg): '))
            resultado = reproductor.agregar(titulo, artista, duracion)
            print(resultado)
        if opcion == 2:
            print('')
            resultado = reproductor.avanzar()
            print(resultado)
        if opcion == 3:
            print('')
            resultado = reproductor.retroceder()
            print(resultado)
        if opcion == 4:
            print('')
            print('❌ Eliminar una Canción')
            titulo = input('Ingrese el título de la canción a eliminar: ')
            resultado = reproductor.eliminar(titulo)
            print(resultado)
        if opcion == 5:
            print('')
            cancion_actual = reproductor.reproducir()
            print('🎵 Ahora reproduciendo:')
            print(cancion_actual)
            #barra_progreso(100, cancion_actual.duracion)
            barra_progreso(100, 1)
        if opcion == 6:
            print('')
            print(reproductor)
