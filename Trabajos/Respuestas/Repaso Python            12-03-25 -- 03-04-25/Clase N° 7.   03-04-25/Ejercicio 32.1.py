with open("1MillonPI.txt", "r") as file:
    Digitos = file.read()

Fecha = input(
    "Ingresa Tu Cumpleaños En La Forma ddmmaa: ")

if Fecha in Digitos:
    print(
        f"¡Sí! La secuencia {Fecha} aparece en los primeros un millón de dígitos de Pi.")
else:
    print(
        f"No, la secuencia {Fecha} no aparece en los primeros un millón de dígitos de Pi.")
