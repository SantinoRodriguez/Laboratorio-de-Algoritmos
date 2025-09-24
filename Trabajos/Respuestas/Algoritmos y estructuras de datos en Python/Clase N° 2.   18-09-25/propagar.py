lista = []
try:
    numeros = int(input("Cuantos fósforos querés?: "))
    if numeros <= 0:
        raise ValueError("El número de fósforos debe ser mayor que 0.")
except ValueError as e:
    print(f"Error: {e}")
    exit()
for i in range(0, numeros):
    while True:
        try:
            fosforo = int(input(f"{i + 1}, Colocá 1 para encendido, 0 para apagado y -1 para quemado: "))
            if fosforo not in [1, 0, -1]:
                raise ValueError("El valor ingresado debe ser 1, 0 o -1.")
            lista.append(fosforo)
            break
        except ValueError as e:
            print(f"Error: {e}. Intenta nuevamente.")
def propagar():
    print(f"{lista}, Lista Original")
    for y in range(0, numeros):
        for i in range(0, numeros):
            if lista[i] == 1:
                if i + 1 < len(lista):
                    if lista[i + 1] == 0:
                        lista[i + 1] = 1
                if i - 1 >= 0:
                    if lista[i - 1] == 0:
                        lista[i - 1] = 1
    print(lista)
propagar()
