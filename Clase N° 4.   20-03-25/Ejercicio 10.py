Pizzas = []
for i in range(0,3):
    Cual = input("¿Cual Pizza te Gusta?: ")
    Pizzas.append(Cual.capitalize())
for i in Pizzas:
    print(f"Me Gusta la Pizza {i}")
print("¡Me Encanta la Pizza!")