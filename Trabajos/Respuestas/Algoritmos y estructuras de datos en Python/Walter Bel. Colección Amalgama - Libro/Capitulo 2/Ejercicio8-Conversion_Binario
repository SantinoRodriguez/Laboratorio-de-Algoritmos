def conversion(n):
    try:
        if not isinstance(n, int) or n < 0:
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        if n == 0:
            return "0"
        elif n == 1:
            return "1"
        else:
            return conversion(n//2) + str(n % 2)
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(conversion(10))