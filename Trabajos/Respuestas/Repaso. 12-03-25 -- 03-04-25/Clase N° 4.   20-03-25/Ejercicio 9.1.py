Lugares = []
LugaresSorted = []
LugaresReversed = []
for i in range(0,5):
    Lugar = input("Pensa en un Lugar al que te Gustaria Ir: ")
    Lugares.append(Lugar.capitalize())
print(f"Lista Original: {Lugares}")
LugaresSorted = sorted(Lugares)
print(f"Lista Ordenada: {LugaresSorted}")
print(f"Lista Original: {Lugares}")
LugaresReversed = Lugares[::-1]
print(f"Lista a la Inversa: {LugaresReversed}")
print(f"Lista Original: {Lugares}")
Lugares.sort()
print(f"Lista Original Ordenada: {Lugares}")
print(f"Lista Original a la Inversa Ordenada: {Lugares[::-1]}")