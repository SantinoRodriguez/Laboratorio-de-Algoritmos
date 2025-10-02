import os
os.system("cls")

def f(n):
    try:  
        if not isinstance(n, int) or n < 0:
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        if n == 1:
            return 2
        else:
            return n + 1 / f(n - 1)
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(f(2))