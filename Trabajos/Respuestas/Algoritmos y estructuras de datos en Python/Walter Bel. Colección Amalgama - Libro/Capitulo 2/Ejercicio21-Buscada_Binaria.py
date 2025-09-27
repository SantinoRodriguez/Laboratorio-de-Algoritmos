import os
os.system("cls")

def binaria(lista, n, m = 0):
    try:  
        if not isinstance(lista, list):
            raise ValueError("El valor de n debe ser una lista.")
        if not lista:
            return f"{n} no se encuentra en la lista"
        medio = len(lista) // 2
        if lista[medio] == n:
            return m + medio + 1
        elif n < lista[medio]:
            return binaria(lista[:medio], n, m)
        else:
            return binaria(lista[medio + 1:], n, m + medio + 1)
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

lista = [1,2,3,4,5,6,7,8,9,10]
print(binaria(lista, 4))
print(binaria(lista, 7))
print(binaria(lista, 11))