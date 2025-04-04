import random
Edad = (random.randint(0,100))
print(f"La Edad Es: {Edad}")
if Edad < 2:
    print("La Persona Es un Bebe")
elif Edad > 2 and Edad < 4:
    print("La Persona Es un Nene/a Chiquito/a")
elif Edad > 2 and Edad < 13:
    print("La Persona Es un Nene/a")
elif Edad > 13 and Edad < 20:
    print("La Persona Es un Adolecente")
elif Edad > 20 and Edad < 65:
    print("La Persona Es un Adulto")
elif Edad > 65:
    print("La Persona Es un Adulto Mayor")