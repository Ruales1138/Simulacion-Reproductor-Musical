# 📀 Práctica: Implementación de una Lista de Reproducción de Música con Listas Enlazadas 🎵
## Objetivo
El objetivo de esta práctica es desarrollar una aplicación en consola que simule una lista de reproducción de música, utilizando estructuras de datos enlazadas. Los estudiantes deberán analizar y justificar qué tipo de estructura es la más adecuada para implementar cada funcionalidad.

Se espera que el programa permita agregar canciones, avanzar y retroceder entre ellas, eliminarlas, reproducir en modo aleatorio, adelantar la reproducción y generar subplaylists.

Se otorgarán puntos adicionales a los estudiantes que usen buenas prácticas de programación y diseño y que implementen una interfaz más amigable y organizada.

# 📌 Requisitos de la Implementación
## 📂 1. Estructura de la Lista de Reproducción
- Implementar una estructura de datos enlazada para gestionar la lista de canciones.
- Cada canción debe tener:
  - Título
  - Artista
  - Duración (entre 10 y 15 segundos).
- El estudiante debe analizar qué tipo de estructura es la más adecuada:
  - Lista enlazada simple
  - Lista doblemente enlazada
  - Lista enlazada circular
  - Pila implementada con listas enlazadas
  - Cola implementada con listas enlazadas
## 🎶 2. Funcionalidades Obligatorias
### ✅ Agregar una canción a la playlist
- Permitir al usuario ingresar una canción con su título, artista y duración.
- Agregar la canción a la lista.
- No se permiten canciones con el mismo título repetido.
### ✅ Avanzar a la siguiente canción
- Si la lista no está vacía, la reproducción avanza a la siguiente canción.
- Si se llega al final de la lista, debe volver al inicio (si se eligió una estructura circular).
### ✅ Retroceder a la canción anterior
- Si la lista no está vacía, la reproducción retrocede a la canción anterior.
- Si se está en la primera canción, debe regresar a la última.
### ✅ Eliminar una canción
- Se debe permitir eliminar una canción por su título.
- Si la canción eliminada estaba en reproducción, se debe reproducir la siguiente automáticamente.
- Si solo queda una canción y se elimina, la lista debe quedar vacía.




