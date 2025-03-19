Invitados = []
for i in range(0,3):
    Persona = input(f"¿A Quien Queres Invitar a Cenar? {i + 1}: ")
    Invitados.append(Persona.capitalize())
for i in range(0,3):
    print(f"Hola, {Invitados[i]}, ¿Queres Venir a Cenar Mañana?")
print(f"{" - ".join(Invitados)}, Sepan Que Consegui Una Mesa Mas Grande")
Persona = input(f"¿A Quien Queres Invitar a Cenar?: ")
Invitados.insert(0,Persona.capitalize())
Persona = input(f"¿A Quien Queres Invitar a Cenar?: ")
Invitados.insert(len(Invitados)//2,Persona.capitalize())
Persona = input(f"¿A Quien Queres Invitar a Cenar?: ")
Invitados.append(Persona.capitalize())
for i in range(0,len(Invitados)):
    print(f"Hola, {Invitados[i]}, ¿Queres Venir a Cenar Mañana?")