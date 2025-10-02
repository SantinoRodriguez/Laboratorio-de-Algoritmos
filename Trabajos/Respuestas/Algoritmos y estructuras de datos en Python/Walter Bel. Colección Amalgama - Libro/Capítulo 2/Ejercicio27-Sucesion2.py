import os
os.system("cls")

def sucesion(n):
    try:  
        if not isinstance(n, (int, float)) or n < 0:
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        if n < 21:
            print(n)
            return
        print(n, end=" -> ")
        sucesion(n / 4)
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

sucesion(1376256)