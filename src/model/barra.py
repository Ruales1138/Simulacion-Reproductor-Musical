import time   # Módulo para trabajar con tiempo (pausas, medir duración, etc.)
import sys    # Módulo para escribir directamente en la consola sin saltos de línea

def barra_progreso(total, tiempo_total):
    # Calculamos cuánto debe durar cada iteración para que la barra tome el tiempo total
    tiempo_por_iteracion = tiempo_total / total

    # Guardamos el tiempo en que comienza la ejecución de la barra
    inicio = time.time()

    # Bucle que va desde 0 hasta 'total', para simular el avance
    for i in range(total + 1):
        # Calculamos cuántos segundos han pasado desde que empezó
        tiempo_actual = int(time.time() - inicio)  # Solo segundos enteros

        # Formateamos el tiempo transcurrido y el total como "Xs" (ej. 3s, 5s)
        tiempo_actual_fmt = f"{tiempo_actual:2d}s"
        tiempo_total_fmt = f"{int(tiempo_total):2d}s"

        # Calculamos cuántos caracteres de la barra deben estar llenos
        # 50 es el ancho total de la barra visual
        barra = '#' * int((i / total) * 50) + '-' * (50 - int((i / total) * 50))

        # Construimos la línea para mostrar: tiempo transcurrido | barra | tiempo total
        # '\r' hace que se sobreescriba la línea anterior (sin saltos)
        sys.stdout.write(f'\r{tiempo_actual_fmt} |[{barra}]| {tiempo_total_fmt}')
        sys.stdout.flush()  # Forzamos a que se actualice en pantalla

        # Esperamos el tiempo correspondiente antes de pasar al siguiente paso
        time.sleep(tiempo_por_iteracion)

    # Al final, hacemos un salto de línea para que el prompt quede bien posicionado
    print()

# Llamamos a la función con 100 pasos y duración total de 5 segundos
# barra_progreso(100, 5)



