def secuencia2(lista, buscado):
    """Método de búsqueda secuencial con centinela"""
    """Descripción:
    Este algoritmo utiliza la fuerza bruta para buscar un elemtento
    que puede estar o no estar dentro de una lista al igual que
    su forma elemental, sin embargo, posee una condicion que lo
    detiene en caso de alcanzar el objeto buscado. Esto es util 
    cuando se tiene gran cantidad de elementos para ahorrar tiempo"""
    posicion = -1 # Si no se encuentra devuelve un elemento que no es parte de la lista
    # Bucle principal, todos los elementos de la lista
    for i in range(0, len(lista)):
        if (lista[i] == buscado):
            posicion = i
            break
    return posicion