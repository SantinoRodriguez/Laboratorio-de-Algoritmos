def burbuja_mejorado(lista):
    """Método de ordenamiento burbuja mejorado."""
    """Descripción general:
    Este algoritmo ordena una lista de elementos de menor a mayor, similar
    al burbuja tradicional, pero incorpora un control para detectar si la
    lista ya está ordenada y evitar pasadas innecesarias. Esto mejora la
    eficiencia en listas que ya están parcialmente ordenadas."""
    i = 0                 
    control = True         # Variable que indica si se realizaron intercambios
    # Bucle principal: continúa mientras queden elementos por revisar y se hayan realizado cambios
    while (i <= len(lista) - 2) and control:
        control = False    # Se asume que no habrá intercambios en esta pasada
        for j in range(0, len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                control = True   # Marca que hubo un intercambio en esta pasada
        i += 1
