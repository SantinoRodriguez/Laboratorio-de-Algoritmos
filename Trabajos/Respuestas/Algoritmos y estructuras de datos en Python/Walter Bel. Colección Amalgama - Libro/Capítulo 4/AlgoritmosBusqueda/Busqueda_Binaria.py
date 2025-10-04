def binaria(lista, buscado):
    """Método de búsqueda binaria."""
    """Descripción:
    Este metodo consiste en dividir una lista por la
    mitad en busca de un elemento especifico, si el
    elemento es mayor al valor medio se procede a 
    dividir de nuevo la lista, pero esta vez desde la
    parte derecha, sino al revez. Para que funcione este
    algoritmo debe de tener una lista ordenada"""
    posicion = -1 # Si no se encuentra devuelve un elemento que no es parte de la lista
    primero = 0
    ultimo = len(lista) - 1
    # Bucle principañ, mientras no se haya encontrado y la lista no se pueda dividir mas
    while (primero <= ultimo) and (posicion == -1):
        medio = (primero + ultimo) // 2
        if(lista[medio] == buscado):
            posicion = medio
        else:
            # Si es menor al buscado el ultimo valor pasa a ser el del medio, exclusive
            if(buscado < lista[medio]):
                ultimo = medio - 1
            # Si es mayor al buscado el primer valor pasa a ser el del medio, exclusive
            else:
                primero = medio + 1
    return posicion