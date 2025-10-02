def convercion(n):
    try:
        if not isinstance(n, str):
            raise ValueError("El valor de n debe ser un número entero.")
        m = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        if len(n) == 1:
            return m[n]
        else:
            if m[n[0]] < m[n[1]]:
                return -m[n[0]] + convercion(n[1:])
            else:
                return m[n[0]] + convercion(n[1:])
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(convercion("MCMXCIV"))