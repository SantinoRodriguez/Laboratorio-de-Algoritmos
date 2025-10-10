def Chico(head):
    minValue = head.data
    contador = 1
    currentNode = head.next
    while currentNode:
        if currentNode.data < minValue:
            minValue = currentNode.data
        currentNode = currentNode.next
        contador += 1
    return f"El Valor mas Chico es: {minValue}, Nodo: {contador}"