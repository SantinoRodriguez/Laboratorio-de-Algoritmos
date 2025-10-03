def insercion(lista):
    """Método de ordenamiento inserción."""
    """Descripción general:
    Este algoritmo ordena la lista de forma similar a cómo una persona 
    ordena las cartas en su mano: toma cada nuevo elemento y lo inserta 
    en la posición correcta dentro de la parte ya ordenada.

    Es eficiente para listas pequeñas o casi ordenadas, con complejidad:
    - Mejor caso: O(n) (si la lista ya está ordenada).
    - Peor caso: O(n^2) (si la lista está en orden inverso)."""
    # Bucle externo: recorre la lista desde la segunda posición hasta el final
    for i in range(1, len(lista) + 1):
        k = i - 1  # Índice para comparar hacia atrás en la parte ordenada
        # Mientras no se haya llegado al inicio y el elemento esté desordenado
        while (k > 0) and (lista[k] < lista[k - 1]):
            # Intercambia el elemento actual con el anterior
            lista[k], lista[k - 1] = lista[k - 1], lista[k]
            k -= 1  # Retrocede una posición para seguir comparando
