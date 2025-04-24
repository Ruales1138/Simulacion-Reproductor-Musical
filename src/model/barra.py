import time
import sys

def barra_progreso(total, tiempo_total, inicio_en=0.0):
    if not 0.0 <= inicio_en <= 1.0:
        raise ValueError("El parámetro 'inicio_en' debe estar entre 0.0 y 1.0")

    tiempo_por_iteracion = tiempo_total / total
    inicio = time.time()

    # Calculamos el punto de inicio en pasos
    inicio_contador = int(total * inicio_en)
    pasos_restantes = total - inicio_contador

    for i in range(pasos_restantes + 1):
        tiempo_actual = int(time.time() - inicio)
        tiempo_actual_fmt = f"{tiempo_actual:2d}s"
        tiempo_total_fmt = f"{int(tiempo_total):2d}s"

        # Total de pasos completados desde el inicio de la barra (inicial ya llenos + los nuevos)
        completados = inicio_contador + i
        progreso = completados / total

        # Generamos la barra visual
        barra = '#' * int(progreso * 50) + '-' * (50 - int(progreso * 50))

        sys.stdout.write(f'\r{tiempo_actual_fmt} |[{barra}]| {tiempo_total_fmt}')
        sys.stdout.flush()

        time.sleep(tiempo_por_iteracion)

    print()

# Ejemplo: empieza con la barra ya a la mitad
#barra_progreso(100, 5, 0.5)
