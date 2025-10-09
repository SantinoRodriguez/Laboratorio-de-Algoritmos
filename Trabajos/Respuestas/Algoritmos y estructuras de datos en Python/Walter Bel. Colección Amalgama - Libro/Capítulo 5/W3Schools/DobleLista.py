from Clases.NodoDoble import NodoDoble

nodo1 = NodoDoble(3)
nodo2 = NodoDoble(5)
nodo3 = NodoDoble(13)
nodo4 = NodoDoble(2)

nodo1.next = nodo2

nodo2.prev = nodo1
nodo2.next = nodo3

nodo3.prev = nodo2
nodo3.next = nodo4

nodo4.prev = nodo3

print("\nTraversing forward:")
currentNodo = nodo1
while currentNodo:
    print(currentNodo.data, end=" -> ")
    currentNodo = currentNodo.next
print("null")

print("\nTraversing backward:")
currentNodo = nodo4
while currentNodo:
    print(currentNodo.data, end=" -> ")
    currentNodo = currentNodo.prev
print("null")