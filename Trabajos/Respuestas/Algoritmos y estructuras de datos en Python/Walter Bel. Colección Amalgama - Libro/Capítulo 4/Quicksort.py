def quicksort(lista, primero, ultimo):
    """Método de ordenamiento quicksort."""
    """Descripción general:
    Quicksort es un algoritmo de ordenamiento recursivo muy eficiente.
    Funciona dividiendo la lista en dos sublistas alrededor de un pivote:
    - Todos los elementos menores que el pivote quedan a su izquierda.
    - Todos los elementos mayores que el pivote quedan a su derecha.
    
    Luego, el algoritmo se llama recursivamente sobre cada sublista hasta
    que toda la lista queda ordenada.
    Su complejidad promedio es O(n log n), pero en el peor caso es O(n^2)."""

    izquierda = primero              # Límite izquierdo
    derecha = ultimo - 1             # Límite derecho
    pivote = ultimo                  # Elegimos el pivote como el último elemento

    # Proceso de partición
    while (izquierda < derecha):
        # Avanza la izquierda hasta encontrar un valor mayor que el pivote
        while (izquierda <= derecha) and (lista[izquierda] < lista[pivote]):
            izquierda += 1
        # Retrocede la derecha hasta encontrar un valor menor o igual al pivote
        while (derecha >= izquierda) and (lista[derecha] >= lista[pivote]):
            derecha -= 1
        # Si aún no se cruzaron, intercambia
        if izquierda < derecha:
            lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]

    # Finalmente, coloca el pivote en su posición correcta
    if lista[izquierda] > lista[pivote]:
        lista[izquierda], lista[pivote] = lista[pivote], lista[izquierda]

    # Llamadas recursivas sobre las sublistas
    if primero < izquierda - 1:
        quicksort(lista, primero, izquierda - 1)
    if ultimo > izquierda + 1:
        quicksort(lista, izquierda + 1, ultimo)
