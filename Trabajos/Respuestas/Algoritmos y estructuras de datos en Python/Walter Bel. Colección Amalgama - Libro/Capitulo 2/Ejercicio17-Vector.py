import os
os.system("cls")

def vector(n):
    try:  
        if not isinstance(n, list):
            raise ValueError("El valor de n debe ser una lista.")
        if not n:
            return []
        else:
            return [n[-1]] + vector(n[:-1])
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(vector([7, 3, 4, 2]))