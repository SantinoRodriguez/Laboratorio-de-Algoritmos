import os
os.system("cls")

def MCM (n,m,x = 1):
    try:    
        if not isinstance(n, int) or not isinstance(m, int) or n < 0 or m < 0:
            raise ValueError("los valores de n y m deben ser un número entero no negativo.")
        if (n * x) % m == 0:
            return n * x
        else:
            return MCM(n,m,x + 1)
        
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(MCM(24,36))