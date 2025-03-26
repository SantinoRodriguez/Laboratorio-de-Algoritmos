Pizzas = []
for i in range(0,3):
    Cual = input("¿Cual Pizza te Gusta?: ")
    Pizzas.append(Cual.capitalize())
PizzasAmigo = Pizzas[:]
Amigazo = input("¿Cual Pizza le Gusta a Tu Amigo?: ")
PizzasAmigo.append(Amigazo.capitalize())
for i in Pizzas:
    print(f"Mis Pizzas Favoritas Son: {i}")
for i in PizzasAmigo:
    print(f"Las Pizzas Favoritas de Mi Amigo/a Son: {i}")