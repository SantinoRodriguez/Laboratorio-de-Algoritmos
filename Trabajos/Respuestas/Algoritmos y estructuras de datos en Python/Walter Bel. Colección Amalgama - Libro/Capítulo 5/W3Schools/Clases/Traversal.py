def Traversal(head):
    currentNodo = head
    while currentNodo:
        print(currentNodo.data, end=" -> ")
        currentNodo = currentNodo.next
    print("null")