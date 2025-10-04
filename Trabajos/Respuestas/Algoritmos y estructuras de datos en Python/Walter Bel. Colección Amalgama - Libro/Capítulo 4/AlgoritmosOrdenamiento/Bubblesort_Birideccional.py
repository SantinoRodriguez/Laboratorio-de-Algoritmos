def coctel(lista):
    """Método de ordenamiento cóctel (burbuja bidireccional)."""
    """Descripción general:
    Este algoritmo es una variante del burbuja que ordena la lista
    en ambas direcciones en cada pasada. Primero "empuja" el mayor
    elemento hacia el final y luego "empuja" el menor elemento hacia
    el inicio, reduciendo así el número de pasadas necesarias.

    Es más eficiente que el burbuja clásico para listas que tienen
    elementos grandes o pequeños en posiciones lejanas al inicio o al final."""
    izquierda = 0               
    derecha = len(lista) - 1      
    control = True              
    while (izquierda < derecha) and control:
        control = False
        # Paso 1: recorrido de izquierda a derecha
        for i in range(izquierda, derecha):
            if lista[i] > lista[i + 1]:
                # Intercambia elementos desordenados
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                control = True
        derecha -= 1               # Reduce el límite derecho, el mayor elemento ya está en su lugar
        # Paso 2: recorrido de derecha a izquierda
        for j in range(derecha, izquierda, -1):
            if lista[j] < lista[j - 1]:
                # Intercambia elementos desordenados
                lista[j], lista[j - 1] = lista[j - 1], lista[j]
                control = True
        izquierda += 1             # Aumenta el límite izquierdo, el menor elemento ya está en su lugar
