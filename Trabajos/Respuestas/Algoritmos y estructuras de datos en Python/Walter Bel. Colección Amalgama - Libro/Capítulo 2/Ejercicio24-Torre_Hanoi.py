import os
os.system("cls")

def torre(n, x, y, z):
    try:  
        if not isinstance(n, int) or n < 0:
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        if n == 1:
            return [f"Mover disco 1 de {x} a {y}"] 

        else:
            return (
                torre(n - 1, x, z, y) +
                [f"Mover disco {n} de {x} a {y}"] +
                torre(n - 1, z, y, x))
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

probar = torre(3, "Aguja 1", "Aguja 3", "Aguja 2")
for t in probar:
    print(t)