class Usuario:
    def __init__(self, Nombre, Apellido, Edad, CorreoElectronico, Ciudad):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Edad = Edad
        self.CorreoElectronico = CorreoElectronico
        self.Ciudad = Ciudad
        self.IntentosLogin = 0

    def DescribirUsuario(self):
        print(f"Nombre: {self.Nombre} {self.Apellido}")
        print(f"Edad: {self.Edad}")
        print(f"Correo Electrónico: {self.CorreoElectronico}")
        print(f"Ciudad: {self.Ciudad}")

    def SaludarUsuario(self):
        print(f"¡Hola, {self.Nombre}! Bienvenido a tu perfil.")

    def IncrementarIntentosLogin(self):
        self.IntentosLogin += 1
        print(
            f"Intentos de login incrementados. Ahora son: {self.IntentosLogin}")

    def ReiniciarIntentosLogin(self):
        self.IntentosLogin = 0
        print(
            f"Intentos de login reiniciados. Ahora son: {self.IntentosLogin}")


class Privilegios:
    def __init__(self, privilegios):
        self.privilegios = privilegios

    def MostrarPrivilegios(self):
        print(f"Privilegios:")
        for privilegio in self.privilegios:
            print(f"- {privilegio}")


class Administrador(Usuario):
    def __init__(self, Nombre, Apellido, Edad, CorreoElectronico, Ciudad, Privilegios):
        super().__init__(Nombre, Apellido, Edad, CorreoElectronico, Ciudad)
        self.Privilegios = Privilegios

    def MostrarPrivilegios(self):
        self.Privilegios.MostrarPrivilegios()


privilegios_admin = Privilegios([
    "Puede Agregar Publicaciones",
    "Puede Eliminar Publicaciones",
    "Puede Bloquear Usuarios",
    "Puede Editar Publicaciones",
    "Puede Ver Estadísticas",
    "Puede Gestionar Comentarios",
    "Puede Agregar Imágenes",
    "Puede Modificar Perfil",
    "Puede Ver Perfil De Otros Usuarios",
    "Puede Enviar Mensajes Privados"
])

Admin = Administrador("Santino", "Rodriguez", 16,
                      "santinorofu@gmail.com", "CABA", privilegios_admin)

Admin.MostrarPrivilegios()
