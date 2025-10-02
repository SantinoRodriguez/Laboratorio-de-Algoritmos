import os
os.system("cls")

def sucesion(n,m = 0):
    try:  
        if not isinstance(n, int) or n < 0:
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        if n == (m + 1):
            return 2 - (3 * m)
        else:
            return sucesion(n,m + 1)
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(sucesion(5))