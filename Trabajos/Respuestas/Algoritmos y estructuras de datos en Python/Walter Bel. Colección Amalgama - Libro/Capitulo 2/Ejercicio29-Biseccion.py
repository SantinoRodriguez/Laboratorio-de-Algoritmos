def biseccion(f, n, m):
    try:
        if not isinstance(n, (int, float)) or not isinstance(m, (int, float)):
            raise ValueError("n y m deben ser números")
        if (f(n) * f(m)) > 0:
            raise ValueError("f(n) y f(m) deben tener signos opuestos")
        x = (n + m) / 2
        if abs(f(x)) < 1e-6:
            return x
        else:
            if (f(n) * f(x)) < 0:
                return biseccion(f, n, x)
            else:
                return biseccion(f, x, m)
            
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

f = lambda x: x * 2/4 + 20
print(int(biseccion(f,-100,5)))