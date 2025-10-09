from Clases.Nodo import Nodo

nodo1 = Nodo(3)
nodo2 = Nodo(5)
nodo3 = Nodo(13)
nodo4 = Nodo(2)

nodo1.next = nodo2
nodo2.next = nodo3
nodo3.next = nodo4
nodo4.next = nodo1

currentNodo = nodo1
startNodo = nodo1
print(currentNodo.data, end=" -> ") 
currentNodo = currentNodo.next 

while currentNodo != startNodo:
    print(currentNodo.data, end=" -> ")
    currentNodo = currentNodo.next

print("...")