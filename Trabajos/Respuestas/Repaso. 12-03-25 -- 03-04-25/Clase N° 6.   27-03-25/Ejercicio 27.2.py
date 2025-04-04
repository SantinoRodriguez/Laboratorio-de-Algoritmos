class Restaurante:
    def __init__(self, NombreRestaurante, TipoCocina):
        self.NombreRestaurante = NombreRestaurante
        self.TipoCocina = TipoCocina

    def DescribirRestaurante(self):
        print(f"El Restaurante {self.NombreRestaurante} Sirve {self.TipoCocina}.")

    def AbrirRestaurante(self):
        print(f"El Restaurante {self.NombreRestaurante} Está Abierto.")

Restaurante1 = Restaurante("La Parrilla De Juan", "Cocina Argentina")
Restaurante2 = Restaurante("Sushi Sensei", "Cocina Japonesa")
Restaurante3 = Restaurante("Pasta Fresca", "Cocina Italiana")

Restaurante1.DescribirRestaurante()
Restaurante2.DescribirRestaurante()
Restaurante3.DescribirRestaurante()
