import os
os.system("cls")

def sumatoria(n):
    try:
        if not isinstance(n, int) or n < 0:
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        
        if n == 0 or n == 1:
            return n
        else:
            return n + sumatoria(n - 1)
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None
    
print(sumatoria(5))