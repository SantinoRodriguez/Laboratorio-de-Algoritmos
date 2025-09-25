def contador(n):
    try:    
        if not isinstance(n, int):
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        
        if n < 10:
            return 1
        else:
            return 1 + contador(n // 10)

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(contador(123))