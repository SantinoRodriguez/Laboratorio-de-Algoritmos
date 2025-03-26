Personas = {"Nombre": "Mateo", "Apellido": "De Lucca", "Edad": "15", "Ciudad": "CABA"}
Teo = {"Nombre": "Teo", "Apellido": "Marcyniuk", "Edad": "16", "Ciudad": "CABA"}
Fuchs = {"Nombre": "Santino", "Apellido": "Rodriguez", "Edad": "16", "Ciudad": "CABA"}
Gente = [Personas,Teo,Fuchs]
for Personas in Gente:
    print(f"{Personas['Nombre']} {Personas['Apellido']}, Tiene {Personas['Edad']} y Vive en {Personas['Ciudad']}")