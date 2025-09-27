import os
os.system("cls")

def MCD(n,m):
    try:    
        if not isinstance(n, int) or not isinstance(m, int) or n < 0 or m < 0:
            raise ValueError("los valores de n y m deben ser un número entero no negativo.")
        if m == 0:
            return n
        else:
            return MCD(m, n % m) 
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(MCD(270,192))