import os
os.system("cls")

def raiz(n,m = 1):
    try: 
        if not isinstance(n, int) or n < 0:
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        if n == 1 or n == 0:
            return n
        if m ** 2 == n:
            return m
        else:
            return raiz(n, m + 1)
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(raiz(25))