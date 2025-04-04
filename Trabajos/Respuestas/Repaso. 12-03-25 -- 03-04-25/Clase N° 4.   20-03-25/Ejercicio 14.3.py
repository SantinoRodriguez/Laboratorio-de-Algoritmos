UsuariosActuales = ["Juan", "Maria", "Pedro", "Lucia", "Carlos"]
UsuariosNuevos = ["Ana", "JUAN", "Carlos", "MARTIN", "Sofia"]
UsuariosActualesLower = [Usuario.lower() for Usuario in UsuariosActuales]
for Usuario in UsuariosNuevos:
    if Usuario.lower() in UsuariosActualesLower:
        print(f"El nombre de usuario '{Usuario}' ya está en uso. Por favor, elegí otro.")
    else:
        print(f"El nombre de usuario '{Usuario}' está disponible.")
