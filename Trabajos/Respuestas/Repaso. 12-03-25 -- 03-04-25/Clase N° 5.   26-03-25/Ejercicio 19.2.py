while True:
    Edad = int(input("¿Cuantos Años Tenes?: "))
    if Edad < 3:
        print("La Entrada Es Gratis") 
    elif Edad >= 3 and Edad < 12:
        print("La Entrada Cuesta $10")
    else:
        print("La Entrada Cuesta $15")