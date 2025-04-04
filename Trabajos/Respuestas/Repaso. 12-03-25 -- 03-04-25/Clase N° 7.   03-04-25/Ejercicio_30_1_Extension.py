class Restaurante:
    def __init__(self, NombreRestaurante, TipoCocina):
        self.NombreRestaurante = NombreRestaurante
        self.TipoCocina = TipoCocina
        self.ClientesAtendidos = 0

    def DescribirRestaurante(self):
        print(f"Restaurante: {self.NombreRestaurante}")
        print(f"Tipo de Cocina: {self.TipoCocina}")

    def AbrirRestaurante(self):
        print(f"El restaurante {self.NombreRestaurante} está abierto.")

    def EstablecerClientesAtendidos(self, NuevosClientes):
        self.ClientesAtendidos = NuevosClientes
        print(f"Clientes atendidos establecidos a: {self.ClientesAtendidos}")

    def IncrementarClientesAtendidos(self, ClientesAdicionales):
        self.ClientesAtendidos += ClientesAdicionales
        print(
            f"Clientes atendidos incrementados. Ahora son: {self.ClientesAtendidos}")
