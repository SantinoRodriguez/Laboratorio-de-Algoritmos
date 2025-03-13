nombre = input("Ingresa un nombre: ")

nombre_minuscula = nombre.lower()
print(nombre_minuscula)
print("Códigos ASCII de los caracteres:")
for caracter in nombre_minuscula:
    print(f"'{caracter}': {ord(caracter)}")

# Convierte el codigo a minuscula
# Muestra los caracteres en ASCCI con ord
