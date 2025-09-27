import os
os.system("cls")

def centinela(lista,n,m = 0):
    try:  
        if not isinstance(lista, list):
            raise ValueError("El valor de n debe ser una lista.")
        if m == 0:
            lista.append(n)
        if n == lista[m]:
            if m == len(lista) - 1:
                return False
            else:
                return True, m + 1
        else:
            return centinela(lista, n, m + 1)
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

lista = [7, 3, 4, 2]
print(centinela(lista,4))
print(centinela(lista,50))