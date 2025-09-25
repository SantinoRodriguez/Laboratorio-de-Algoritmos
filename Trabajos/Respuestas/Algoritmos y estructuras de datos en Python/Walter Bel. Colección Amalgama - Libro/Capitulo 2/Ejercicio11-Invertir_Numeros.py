def invertir(n, invertido = 0):
    if n == 0:
        return invertido
    else:
        return invertir(n // 10, invertido * 10 + n % 10)

print(invertir(743))
