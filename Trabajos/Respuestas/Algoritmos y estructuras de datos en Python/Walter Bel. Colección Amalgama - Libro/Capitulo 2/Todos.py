import os
os.system("cls")

# Ejercicio 1
def fibonacci(n):
    try:
        if not isinstance(n, int) or n < 0:
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        
        if n == 0 or n == 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(f"Ejercicio 1:\n{fibonacci(7)}\n\n")

# Ejercicio 2
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
    
print(f"Ejercicio 2:\n{sumatoria(5)}\n\n")