Invitados = []
for i in range(0,3):
    Persona = input(f"A Quien Queres Invitar a Cenar? {i + 1}: ")
    Invitados.append(Persona)
for i in range(0,3):
    print(f"Hola, {Invitados[i].capitalize()}, Queres Venir a Cenar Mañana?")

print(f"Hay {len(Invitados)} Invitados")