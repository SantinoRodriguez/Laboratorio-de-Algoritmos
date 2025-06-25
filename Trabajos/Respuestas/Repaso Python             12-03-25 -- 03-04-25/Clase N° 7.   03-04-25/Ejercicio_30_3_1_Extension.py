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
