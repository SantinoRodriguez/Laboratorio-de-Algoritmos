def countsort(lista, maximo):
    """Método de ordenamiento CountSort."""
    """Descripción general:
    CountSort es un algoritmo de ordenamiento basado en contar la
    frecuencia de aparición de cada elemento. Funciona bien cuando
    los elementos de la lista son números enteros y están en un rango
    pequeño (por ejemplo de 0 a k).

    Complejidad:
    - Tiempo: O(n + k), donde n es el tamaño de la lista y k el valor máximo.
    - Espacio: O(n + k), ya que utiliza arreglos auxiliares."""
    lista_conteo = [0] * (maximo + 1)
    # Lista ordenada (resultado), inicialmente vacía con el mismo tamaño de la original
    lista_ordenada = [None] * len(lista)
    # Contar la frecuencia de cada número en la lista
    for i in lista:
        lista_conteo[i] += 1
    # Acumular las frecuencias para obtener las posiciones finales
    total = 0
    for i in range(len(lista_conteo)):
        # Sumar cada conteo con el conteo anterior
        lista_conteo[i], total = total, total + lista_conteo[i]
    # Ubicar cada número en su posición correspondiente dentro de la lista ordenada
    for indice in lista:
        # El valor 'indice' es un elemento de la lista original.
        # 'lista_conteo[indice]' nos indica en qué posición debe ir este valor
        # dentro de la lista ordenada.
        lista_ordenada[lista_conteo[indice]] = indice

        # Luego de colocar el valor, incrementamos en 1 la posición en lista_conteo[indice].
        # Esto asegura que, si el mismo número aparece varias veces,
        # se coloque en la siguiente posición libre (manteniendo la estabilidad del algoritmo).
        lista_conteo[indice] += 1

    # Finalmente, devolvemos la lista ya completamente ordenada
    return lista_ordenada
