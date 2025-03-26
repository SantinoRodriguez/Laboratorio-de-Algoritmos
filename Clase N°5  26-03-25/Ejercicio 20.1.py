import time
PedidosSandwiches = ["Atún", "Jamón y Queso", "Pollo", "Vegetariano", "Roast Beef"]
SandwichesTerminados = []

while PedidosSandwiches:
    time.sleep(1)
    Sandwich = PedidosSandwiches.pop(0)
    print(f"Preparé Tu Sándwich de {Sandwich}.")  
    SandwichesTerminados.append(Sandwich) 

print("\nTodos Los Sándwiches Están Listos:")
for Sandwich in SandwichesTerminados:
    print(f"- Sándwich de {Sandwich}")
