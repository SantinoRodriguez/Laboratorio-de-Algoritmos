def logaritmo(n,m):
    try:
        if not isinstance(n, int) or not isinstance(m, int) or n < 0:
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        if n == 0:
            return 1
        if n == 1:
            return 0
        else:
            return logaritmo(n / m, m) + 1
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(logaritmo(32,2))