class Restaurante:
    def __init__(self, NombreRestaurante, TipoCocina):
        self.NombreRestaurante = NombreRestaurante
        self.TipoCocina = TipoCocina

    def DescribirRestaurante(self):
        print(f"El Restaurante {self.NombreRestaurante} Sirve {self.TipoCocina}.")

    def AbrirRestaurante(self):
        print(f"El Restaurante {self.NombreRestaurante} Está Abierto.")

Restaurante1 = Restaurante("La Parrilla De Juan", "Cocina Argentina")

print(Restaurante1.NombreRestaurante)
print(Restaurante1.TipoCocina)

Restaurante1.DescribirRestaurante()
Restaurante1.AbrirRestaurante()