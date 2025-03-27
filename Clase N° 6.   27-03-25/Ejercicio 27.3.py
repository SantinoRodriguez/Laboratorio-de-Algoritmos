class Usuario:
    def __init__(self, Nombre, Apellido, Edad, CorreoElectronico, Ciudad):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Edad = Edad
        self.CorreoElectronico = CorreoElectronico
        self.Ciudad = Ciudad

    def DescribirUsuario(self):
        print(f"Nombre: {self.Nombre} {self.Apellido}")
        print(f"Edad: {self.Edad}")
        print(f"Correo Electrónico: {self.CorreoElectronico}")
        print(f"Ciudad: {self.Ciudad}")

    def SaludarUsuario(self):
        print(f"¡Hola, {self.Nombre}! Bienvenido a tu perfil.")

Usuario1 = Usuario("Juan", "Perez", 35, "juan@email.com", "Lima")
Usuario2 = Usuario("Carlos", "Gomez", 30, "carlos@email.com", "Madrid")
Usuario3 = Usuario("Maria", "Lopez", 28, "maria@email.com", "Barcelona")

Usuario1.DescribirUsuario()
Usuario1.SaludarUsuario()

Usuario2.DescribirUsuario()
Usuario2.SaludarUsuario()

Usuario3.DescribirUsuario()
Usuario3.SaludarUsuario()
