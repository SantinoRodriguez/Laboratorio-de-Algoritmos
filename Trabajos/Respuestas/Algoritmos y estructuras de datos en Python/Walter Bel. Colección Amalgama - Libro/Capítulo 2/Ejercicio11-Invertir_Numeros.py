import os
os.system("cls")

def invertir(n, invertido = 0):
    try:    
        if not isinstance(n, int) or n < 0:
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        if n == 0:
            return invertido
        else:
            return invertir(n // 10, invertido * 10 + n % 10)
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(invertir(743))