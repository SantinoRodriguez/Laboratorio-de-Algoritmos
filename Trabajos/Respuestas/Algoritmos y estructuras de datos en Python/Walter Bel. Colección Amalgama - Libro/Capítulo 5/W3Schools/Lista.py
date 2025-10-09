from Clases.Nodo import Nodo
from Clases.Traversal import Traversal
from Clases.MasChico import Chico

nodo1 = Nodo(3)
nodo2 = Nodo(5)
nodo3 = Nodo(13)
nodo4 = Nodo(2)

nodo1.next = nodo2
nodo2.next = nodo3
nodo3.next = nodo4

Traversal(nodo1)
print(Chico(nodo1))