try:
    Numero1 = int(input("Ingresá el primer número: "))
    Numero2 = int(input("Ingresá el segundo número: "))

    Resultado = Numero1 + Numero2
    print(f"La suma de los dos números es: {Resultado}")

except ValueError:
    print("Por favor, asegurate de ingresar solo números. No se permiten letras ni símbolos.")
