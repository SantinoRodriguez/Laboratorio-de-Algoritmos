Invitados = []
for i in range(0,3):
    Persona = input(f"¿A Quien Queres Invitar a Cenar? {i + 1}: ")
    Invitados.append(Persona.capitalize())
for i in range(0,3):
    print(f"Hola, {Invitados[i]}, ¿Queres Venir a Cenar Mañana?")
print(f"{Invitados[-1]} No Puede Asistir a La Cena")
Invitados.pop(-1)
Persona = input(f"¿A Quien Queres Invitar a Cenar?: ")
Invitados.append(Persona.capitalize())
for i in range(0,3):
    print(f"Hola, {Invitados[i]}, ¿Queres Venir a Cenar Mañana?")