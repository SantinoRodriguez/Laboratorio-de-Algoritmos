import random

elementos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
ganadores = random.sample(elementos, 4)

print(
    f"¡Cualquier boleto que tenga estos 4 números o letras gana un premio: {ganadores}!")
