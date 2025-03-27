def HacerSandwich(*Ingredientes):
    print("Estás Pidiendo Un Sándwich Con Los Siguientes Ingredientes:")
    for Ingrediente in Ingredientes:
        print(f"- {Ingrediente}")
    print()

HacerSandwich("Pastrón", "Lechuga", "Tomate")
HacerSandwich("Pollo", "Aguacate", "Queso", "Mayonesa")
HacerSandwich("Jamon", "Queso")