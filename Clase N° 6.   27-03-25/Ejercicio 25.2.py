def ConstruirPerfil(Nombre, Apellido, **InfoUsuario):
    Perfil = {}
    Perfil["Nombre"] = Nombre
    Perfil["Apellido"] = Apellido
    for Clave, Valor in InfoUsuario.items():
        Perfil[Clave] = Valor
    return Perfil

PerfilSantino = ConstruirPerfil("Santino", "Rodriguez", Edad="16", Ciudad="Buenos Aires", Profesion="Estudiante")
print(PerfilSantino)
