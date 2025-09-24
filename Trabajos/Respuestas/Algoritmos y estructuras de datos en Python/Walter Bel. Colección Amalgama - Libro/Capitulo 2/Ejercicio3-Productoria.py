def productoria(n,m):
    try:
        if not isinstance(n, int) or n < 0:
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        
        if m == 0 or n == 0:
            return 0
        elif m == 1:
            return n
        elif n == 1:
            return m
        else:
            return n + productoria(n, m - 1)
        
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(productoria(5,3))