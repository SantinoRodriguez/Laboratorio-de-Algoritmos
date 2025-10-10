import os
from Clases.Nodo import Nodo
from Clases.Traversal import Traversal
from Clases.MasChico import Chico
from Clases.Remover import remover
from Clases.Insertar import insertar
os.system('cls')

nodo1 = Nodo(3)
nodo2 = Nodo(5)
nodo3 = Nodo(13)
nodo4 = Nodo(2)
nuevonodo = Nodo(97)

nodo1.next = nodo2
nodo2.next = nodo3
nodo3.next = nodo4

Traversal(nodo1)
print(Chico(nodo1))
nodo1 = remover(nodo1, nodo3)
print(f"Traversal tras haber eliminado el nodo 3: {Traversal(nodo1)}")
nodo1 = insertar(nodo1, nuevonodo, 3)
print(f"Traversal tras haber agregado el nodo 3: {Traversal(nodo1)}")