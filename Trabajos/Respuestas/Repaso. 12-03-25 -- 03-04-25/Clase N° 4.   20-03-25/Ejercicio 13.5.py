Frutas = ["Manzana", "Banana", "Naranja", "Uva", "Pera","Sandía", "Melón", "Mango", "Piña", "Fresa","Cereza", "Durazno", "Ciruela", "Kiwi"]
Fruta = input("¿Cual Fruta Te Gusta?: ")
if Fruta.capitalize() in Frutas:
    print("Esa Fruta Tambien Me Gutas")
else:
    print("Esa Fruta No Me Gusta")
FrutasFav = ["Manzana, Melon, Kiwi"]
Fruta = input("¿Cual Es Tu Fruta Favorita?: ")
if Fruta.capitalize() in Frutas:
    print("Esa Fruta Es Una de Mis 3 Favoritas")
else:
    print("Esa Fruta No Es de Mi Favoritas")