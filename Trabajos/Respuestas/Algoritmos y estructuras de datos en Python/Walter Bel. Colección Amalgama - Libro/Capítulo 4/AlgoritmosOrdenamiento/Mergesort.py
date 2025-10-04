def mergesort(lista):
    """Método de ordenamiento mergesort."""
    """Descripción general:
    Mergesort es un algoritmo de ordenamiento basado en la técnica
    de "divide y vencerás":
    1. Divide la lista en dos mitades.
    2. Ordena cada mitad de forma recursiva.
    3. Combina (merge) las dos mitades ordenadas en una sola lista.

    Su principal ventaja es que garantiza un tiempo de ejecución
    O(n log n) tanto en el mejor como en el peor caso."""
    
    # Caso base: si la lista tiene 1 o 0 elementos, ya está ordenada
    if len(lista) <= 1:
        return lista
    
    else:
        medio = len(lista) // 2
        izquierda = []
        for i in range(0, medio):
            izquierda.append(lista[i])
        derecha = []
        for i in range(medio, len(lista)):
            derecha.append(lista[i])
        izquierda = mergesort(izquierda)
        derecha = mergesort(derecha)
        # Optimización: si el mayor de izquierda ya es menor o igual al menor de derecha
        # no hace falta mezclar, simplemente se concatenan
        if(izquierda[medio - 1] <= derecha[0]):
            izquierda += derecha
            return izquierda
        # En caso contrario, se mezclan ordenadamente con la función auxiliar merge
        resultado = merge(izquierda, derecha)
        return resultado


def merge(izquierda, derecha):
    """Función auxiliar para combinar dos listas ordenadas
    en una sola lista también ordenada."""
    lista_mezclada = []
    # Mientras ambas listas tengan elementos, se comparan los primeros
    while (len(izquierda) > 0) and (len(derecha) > 0):
        if (izquierda[0] < derecha[0]):
            # Si el primer elemento de izquierda es menor, se pasa a la lista final
            lista_mezclada.append(izquierda.pop(0))
        else:
            # Si el primer elemento de derecha es menor, se pasa a la lista final
            lista_mezclada.append(derecha.pop(0))
    # Si quedaron elementos en izquierda, se agregan al resultado
    if(len(izquierda) > 0):
        lista_mezclada += izquierda
    # Si quedaron elementos en derecha, se agregan al resultado
    if(len(derecha) > 0):
        lista_mezclada += derecha
    # Se retorna la lista ordenada
    return lista_mezclada
