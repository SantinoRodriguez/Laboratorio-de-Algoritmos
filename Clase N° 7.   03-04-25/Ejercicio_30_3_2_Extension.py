from Ejercicio_30_3_1_Extension import Usuario


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
