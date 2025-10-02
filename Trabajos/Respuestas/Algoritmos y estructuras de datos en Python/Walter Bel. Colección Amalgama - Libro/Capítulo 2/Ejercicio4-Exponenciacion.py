import os
os.system("cls")

def potenciacion(n,m):
    try:
        if not isinstance(n, int) or not isinstance(m, int):
            raise ValueError("El valor de n debe ser un número entero.")
        
        if n == 0:
            return 0
        elif m == 0 or n == 1:
            return 1
        elif m == 1:
            return n
        elif m < 0:
            return 1 / n * potenciacion(n, m + 1)
        else:
            return n * potenciacion(n, m - 1)
        
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(potenciacion(2,-3))