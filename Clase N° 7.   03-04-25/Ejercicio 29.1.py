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


class PuestoDeHelados(Restaurante):
    def __init__(self, NombreRestaurante, TipoCocina, Sabores):
        super().__init__(NombreRestaurante, TipoCocina)
        self.Sabores = Sabores

    def MostrarSabores(self):
        print("Sabores de helado disponibles:")
        for sabor in self.Sabores:
            print(f"- {sabor}")


Puesto = PuestoDeHelados("Helados de la Abuela", "Heladería", [
                         "Vainilla", "Chocolate", "Fresa", "Menta", "Café"])
Puesto.MostrarSabores()
