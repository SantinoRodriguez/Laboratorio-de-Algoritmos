import time
PedidosSandwiches = ["Pastron","Atún", "Jamón y Queso","Pastron", "Pollo", "Vegetariano", "Roast Beef", "Pastron"]
SandwichesTerminados = []
print("No Queda Ningun Sandwich de Pastron")
while "Pastron" in PedidosSandwiches:
    PedidosSandwiches.remove("Pastron")

while PedidosSandwiches:
    time.sleep(1)
    Sandwich = PedidosSandwiches.pop(0)
    print(f"Preparé Tu Sándwich de {Sandwich}.")  
    SandwichesTerminados.append(Sandwich) 

print("\nTodos Los Sándwiches Están Listos:")
for Sandwich in SandwichesTerminados:
    print(f"- Sándwich de {Sandwich}")
