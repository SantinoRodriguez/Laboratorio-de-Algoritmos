def insertar(head, newNode, position):
    if position == 1:
        newNode.next = head
        return newNode
    currentNode = head
    for _ in range(position - 2):
        if currentNode is None:
            break
        currentNode = currentNode.next
    newNode.next = currentNode.next
    currentNode.next = newNode
    return head