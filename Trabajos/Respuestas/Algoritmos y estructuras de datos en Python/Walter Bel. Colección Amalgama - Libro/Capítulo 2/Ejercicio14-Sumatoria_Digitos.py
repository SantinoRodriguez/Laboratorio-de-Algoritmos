import os
os.system("cls")

def sumatoria(n):
    try:    
        if not isinstance(n, int) or n < 0:
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        if n < 10:
            return n
        else:
            return (n % 10) + sumatoria(n // 10)
        
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(sumatoria(186))