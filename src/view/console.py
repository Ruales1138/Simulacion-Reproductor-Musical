import sys
sys.path.append('src')
from model.reproductor import Reproductor


r = Reproductor()
r.agregar_cancion('Bohemian Rhapsody', 'Queen', 12)
r.agregar_cancion('Hotel California', 'Eagles', 11)
r.agregar_cancion('Smells Like Teen Spirit', 'Nirvana ', 14)
r.agregar_cancion('Soy Peor', 'Bad Bunny', 10)
r.agregar_cancion('Soy Peor', 'Bad Bunny', 10)

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
            pass
        if opcion == 6:
            print('')
            print(r)
