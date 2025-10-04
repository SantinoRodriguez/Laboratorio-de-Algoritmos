def secuencia(lista, buscado):
    """Método de búsqueda secuencial"""
    """Descripción:
    Este algoritmo utiliza la fuerza bruta para buscar un elemtento
    que puede estar o no estar dentro de una lista. Se denomina el 
    algoritmo mas busqueda más basico por no necesitar de ninguna
    logica para su resolucion ya que simplemente se observa si el
    elemnto se ubica en alguna de las posiciones de la lista de
    manera secuencial - de ahí el nombre -"""
    posicion = -1 # Si no se encuentra devuelve un elemento que no es parte de la lista
    # Bucle principal, todos los elementos de la lista
    for i in range(0, len(lista)):
        if (lista[i] == buscado):
            posicion = i
    return posicion