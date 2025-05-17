import random

Elementos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
MiTicekt = [7, 'B', 3, 'D']
Intentos = 0

while True:
    Ticket = random.sample(Elementos, 4)
    Intentos += 1
    if Ticket == MiTicekt:
        break

print(
    f"¡Ganaste! El boleto {MiTicekt} fue generado después de {Intentos} Intentos.")
