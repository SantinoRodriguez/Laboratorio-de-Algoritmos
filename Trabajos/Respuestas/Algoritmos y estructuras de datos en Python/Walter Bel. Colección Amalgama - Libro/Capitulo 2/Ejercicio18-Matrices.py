import os
os.system("cls")

def matrices(n,x = 0,y = 0):
    try:  
        if not isinstance(n, list):
                raise ValueError("El valor de n debe ser una matriz.")
        if x == len(n):
            return
        if y == len(n[0]):
            matrices(n, x + 1, 0)
        else:
            print(n[x][y], end=' ')
            matrices(n, x, y + 1)
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print("Ejercicio 18, Lector de matrices:")
matrices([[1, 2, 3],[4, 5, 6],[7, 8, 9]])