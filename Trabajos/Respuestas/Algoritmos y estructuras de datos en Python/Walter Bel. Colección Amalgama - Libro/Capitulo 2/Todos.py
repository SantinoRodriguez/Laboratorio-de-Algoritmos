import numpy as np
import random
import os
os.system("cls")

# Ejercicio 1
def fibonacci(n):
    try:
        if not isinstance(n, int) or n < 0:
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        
        if n == 0 or n == 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(f"Ejercicio 1, Valor de Secuencia de Fibonacci:\n{fibonacci(7)}\n")

# Ejercicio 2
def sumatoria(n):
    try:
        if not isinstance(n, int) or n < 0:
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        
        if n == 0 or n == 1:
            return n
        else:
            return n + sumatoria(n - 1)
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(f"Ejercicio 2, Sumador de valores de n hasta 0:\n{sumatoria(5)}\n")

# Ejercicio 3
def productoria(n,m):
    try:
        if not isinstance(n, int) or n < 0:
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        
        if m == 0 or n == 0:
            return 0
        elif m == 1:
            return n
        elif n == 1:
            return m
        else:
            return n + productoria(n, m - 1)
        
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(f"Ejercicio 3, Multiplicador recursivo:\n{productoria(6,3)}\n")

# Ejercicio 4
def potenciacion(n,m):
    try:
        if not isinstance(n, int) or not isinstance(m, int):
            raise ValueError("El valor de n debe ser un número entero.")
        
        if n == 0:
            return 0
        elif m == 0 or n == 1:
            return 1
        elif m == 1:
            return n
        elif m < 0:
            return 1 / n * potenciacion(n, m + 1)
        else:
            return n * potenciacion(n, m - 1)
        
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(f"Ejercicio 4, Potenciador recursivo:\n{potenciacion(2,-3)}\n")

# Ejercicio 5
def convercion(n):
    try:
        if not isinstance(n, str):
            raise ValueError("El valor de n debe ser un número entero.")
        m = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        if len(n) == 1:
            return m[n]
        else:
            if m[n[0]] < m[n[1]]:
                return -m[n[0]] + convercion(n[1:])
            else:
                return m[n[0]] + convercion(n[1:])
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(f"Ejercicio 5, Conversion de Romano a Decimal:\n{convercion("MCMXCIV")}\n")

# Ejercicio 6
def inversion(palabra):
    try:
        if not isinstance(palabra, str):
            raise ValueError("Debe introducir un string como parametro.")
        
        if len(palabra) == 1:
            return palabra
        else:
            # Uno saca la primera letra y el otro deja a parte la primera letra (Funciones con string investigadas)
            return inversion(palabra[1:]) + palabra[0]
        
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(f"Ejercicio 6, Inversor de palabras:\n{inversion("TOMATE")}\n")

# Ejercicio 7
def sumatoria(n):
    try:
        if not isinstance(n, int) or n < 0:
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        
        if n == 1:
            return n
        else:
            return 1 / n + sumatoria(n - 1)
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None
    
print(f"Ejercicio 7, Secuencia Fraccionaria - Σ(1 / n):\n{sumatoria(7)}\n")

# Ejercicio 8
def conversion(n):
    try:
        if not isinstance(n, int) or n < 0:
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        if n == 0:
            return "0"
        elif n == 1:
            return "1"
        else:
            return conversion(n//2) + str(n % 2)
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(f"Ejercicio 8, Conversion de Decimal a Binario:\n{conversion(10)}\n")

# Ejercicio 9
def logaritmo(n,m):
    try:
        if not isinstance(n, (int,float)) or not isinstance(m, int) or n < 0:
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        if n == 0:
            return 1
        if n == 1:
            return 0
        else:
            return logaritmo(n / m, m) + 1
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(f"Ejercicio 9, Logaritmo recursivo:\n{logaritmo(32,2)}\n")

# Ejercicio 10
def contador(n):
    try:    
        if not isinstance(n, int):
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        
        if n < 10:
            return 1
        else:
            return 1 + contador(n // 10)

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(f"Ejercicio 10, Contador de digitos:\n{contador(123)}\n")

# Ejercicio 11
def invertir(n, invertido = 0):
    try:    
        if not isinstance(n, int) or n < 0:
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        if n == 0:
            return invertido
        else:
            return invertir(n // 10, invertido * 10 + n % 10)
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(f"Ejercicio 11, Inversor de numeros:\n{invertir(743)}\n")

# Ejercicio 12
def MCD(n,m):
    try:    
        if not isinstance(n, int) or not isinstance(m, int) or n < 0 or m < 0:
            raise ValueError("los valores de n y m deben ser un número entero no negativo.")
        if m == 0:
            return n
        else:
            return MCD(m, n % m) 
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(f"Ejercicio 12, Maximo Comun Divisor:\n{MCD(270,192)}\n")

# Ejercicio 13
def MCM (n,m,x = 1):
    try:    
        if not isinstance(n, int) or not isinstance(m, int) or n < 0 or m < 0:
            raise ValueError("los valores de n y m deben ser un número entero no negativo.")
        if (n * x) % m == 0:
            return n * x
        else:
            return MCM(n,m,x + 1)
        
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(f"Ejercicio 13, Minimo Comun Multiplo:\n{MCM(24,36)}\n")

# Ejercicio 14
def sumatoria(n):
    try:    
        if not isinstance(n, int) or n < 0:
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        if n < 10:
            return n
        else:
            return (n % 10) + sumatoria(n // 10)
        
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(f"Ejercicio 14, Sumador de digitos:\n{sumatoria(186)}\n")

# Ejercicio 15
def raiz(n,m = 1):
    try: 
        if not isinstance(n, int) or n < 0:
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        if n == 1 or n == 0:
            return n
        if m ** 2 == n:
            return m
        else:
            return raiz(n, m + 1)
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(f"Ejercicio 15, Raiz cuadrada recursiva:\n{raiz(25)}\n")

# Ejercicio 16
def sucesion(n,m = 0):
    try:  
        if not isinstance(n, int) or n < 0:
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        if n == (m + 1):
            return 2 - (3 * m)
        else:
            return sucesion(n,m + 1)
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(f"Ejercicio 16, Sucesion de 2 a razon de -3:\n{sucesion(5)}\n")

# Ejercicio 17
def vector(n):
    try:  
        if not isinstance(n, list):
            raise ValueError("El valor de n debe ser una lista.")
        if not n:
            return []
        else:
            return [n[-1]] + vector(n[:-1])
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(f"Ejercicio 17, Inversor de alementos de una lista:\n{vector([7, 3, 4, 2])}\n")

# Ejercicio 18
def matrices(n,x = 0,y = 0):
    try:  
        if not isinstance(n, list):
                raise ValueError("El valor de n debe ser una matriz.")
        if x == len(n):
            return
        if y == len(n[0]):
            matrices(n, x + 1, 0)
        else:
            print(n[x][y], end=' ')
            matrices(n, x, y + 1)
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print("Ejercicio 18, Lector de matrices:")
matrices([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

# Ejercicio 19
def f(n):
    try:  
        if not isinstance(n, int) or n < 0:
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        if n == 1:
            return 2
        else:
            return n + 1 / f(n - 1)
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(f"\n\nEjercicio 19, Secuencia de valor 2 cuando n es igual a 1 y Σ(n + 1 / f(n - 1)) el resto de las veces:\n{f(2)}\n")

# Ejercicio 20
def centinela(lista,n,m = 0):
    try:  
        if not isinstance(lista, list):
            raise ValueError("El valor de n debe ser una lista.")
        if m == 0:
            lista.append(n)
        if n == lista[m]:
            if m == len(lista) - 1:
                return f"{n} No se encuentra en la lista"
            else:
                return f"El numero {n} se encuentra en la lista en la posicion {m + 1}"
        else:
            return centinela(lista, n, m + 1)
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

lista = [7, 3, 4, 2]
print(f"Ejercicio 20, Lector de lista en busca del valor de n - Metodo Centinela:")
print(f"Ejemplo verdadero: {centinela(lista,4)}")
print(f"Excepcion: {centinela(lista,50)}\n")

# Ejercicio 21
def binaria(lista, n, m = 0):
    try:  
        if not isinstance(lista, list):
            raise ValueError("El valor de n debe ser una lista.")
        if not lista:
            return f"{n} No se encuentra en la lista"
        medio = len(lista) // 2
        if lista[medio] == n:
            return f"{n} Se encuentra en la posicion {m + medio + 1}"
        elif n < lista[medio]:
            return binaria(lista[:medio], n, m)
        else:
            return binaria(lista[medio + 1:], n, m + medio + 1)
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

lista = [1,2,3,4,5,6,7,8,9,10]
print(f"Ejercicio 21, Lector de lista en busca del valor de n - Metodo Binario:")
print(f"Ejemplo Primera midtad: {binaria(lista, 4)}")
print(f"Ejemplo Segunda midtad: {binaria(lista, 7)}")
print(f"Excepcion: {binaria(lista, 11)}\n")

# Ejercicio 22
def usar_la_fuerza(mochila, m = 0):
    try:  
        if not isinstance(mochila, list):
            raise ValueError("El valor de n debe ser una lista.")
        if m == (len(mochila) - 1):
            return "No se ha encontrado el sable de luz", f"Objetos encontrados: {mochila}"
        if mochila[m] == "Sable":
            return "Se encontro el sable de luz", f"Fue necesario retirar otros {m} objetos"
        else:
            return usar_la_fuerza(mochila, m + 1)
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

mochila = ["Agua", "Comida", "Mapa", "Sable", "comunicador"]
mochila2 = ["Agua", "Comida", "Mapa", "comunicador"]
print(f"Ejercicio 22, Lector de lista en busca del valor de n - Con Strings:")
print(f"Ejemplo con sable de luz: {usar_la_fuerza(mochila)}")
print(f"Excepcion: {usar_la_fuerza(mochila2)}\n")

# Ejercicio 23
# Generación del laberinto por ChatGPT
def creacion(n):
    try:  
        if not isinstance(n, int) or n < 0:
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        laberinto = np.ones((n, n), dtype=int)
        x, y = 0, 0
        laberinto[x, y] = 0
        while x < n-1 or y < n-1:
            if x == n-1:
                y += 1
            elif y == n-1:
                x += 1
            else:
                if random.choice([True, False]):
                    x += 1
                else:
                    y += 1
            laberinto[x, y] = 0

        for i in range(n):
            for j in range(n):
                if laberinto[i, j] != 0:
                    laberinto[i, j] = random.choice([0, 1])

        return laberinto

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

def laberinto(n, x = 0, y = 0, salida = None, visitados = None):
    if salida is None:
        salida = []
    if visitados is None:
        visitados = set()
    if x == len(n) - 1 and y == len(n[0]) - 1:
        salida.append([x, y])
        return salida
    if x < 0 or x >= len(n) or y < 0 or y >= len(n[0]) or n[x][y] == 1:
        return None
    if (x, y) in visitados:
        return None
    visitados.add((x, y))
    salida.append([x, y])
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        camino = laberinto(n, x + dx, y + dy, salida.copy(), visitados.copy())
        if camino is not None:
            return camino
    return None

Esquema = creacion(10)
print(f"Ejercicio 23, Resolvedor de laberintos:")
print("Laberinto generado:\n", Esquema, "\n")
print("Camino encontrado:\n", laberinto(Esquema),"\n")

# Ejercicio 24
def torre(n, x, y, z):
    try:  
        if not isinstance(n, int) or n < 0:
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        if n == 1:
            return [f"Mover disco 1 de {x} a {y}"] 

        else:
            return (
                torre(n - 1, x, z, y) +
                [f"Mover disco {n} de {x} a {y}"] +
                torre(n - 1, z, y, x))
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

probar = torre(3, "Aguja 1", "Aguja 3", "Aguja 2")
print(f"Ejercicio 24, Torre de Hanoi con n platos:")
for t in probar:
    print(t)

# Ejercicio 25
def triangulo(n, m = 2, lista = [[1],[1,1]]):
    try:  
        if not isinstance(n, int) or n < 0:
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        if len(lista) == n:
            for fila in lista:
                print(* fila)
            return lista
        fila = [1]
        for i in range(1, len(lista[-1])):
            fila.append(lista[-1][i - 1] + lista[-1][i])
        fila.append(1)
        lista.append(fila)
        return triangulo(n, m + 1, lista)

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(f"\nEjercicio 25, Piramide de Pascal con n pisos:")
triangulo(11)

# Ejercicio 26
def ajedrez(n, fila = 0, tablero = None, amenazas = None):
    if tablero is None:
        tablero = []
    if amenazas is None:
        amenazas = set()
    if fila == n:
        return tablero
    for col in range(n):
        if (fila, col) not in amenazas:
            nuevo_tablero = tablero.copy()
            nuevo_tablero.append((fila + 1, col + 1))
            nuevas_amenazas = amenazas.copy()
            for i in range(n):
                nuevas_amenazas.add((fila, i))     
                nuevas_amenazas.add((i, col))   
                if fila + i < n and col + i < n: nuevas_amenazas.add((fila + i, col + i))
                if fila + i < n and col - i >= 0: nuevas_amenazas.add((fila + i, col - i))
                if fila - i >= 0 and col + i < n: nuevas_amenazas.add((fila - i, col + i))
                if fila - i >= 0 and col - i >= 0: nuevas_amenazas.add((fila - i, col - i))

            resultado = ajedrez(n, fila + 1, nuevo_tablero, nuevas_amenazas)
            if resultado is not None:
                return resultado
    return None

print(f"\nEjercicio 26, Problema de las 8 reinas de Max Bezzel:\n{ajedrez(8)}\n")

# Ejercicio 27
def sucesion(n):
    try:  
        if not isinstance(n, (int, float)) or n < 0:
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        if n < 21:
            print(n)
            return
        print(n, end=" -> ")
        sucesion(n / 4)
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(f"\nEjercicio 27, Sucesion de 5.25 a razon de 4:")
sucesion(1376256)

# Ejercicio 28
def f(n):
    try:  
        if not isinstance(n, int) or n < 0:
            raise ValueError("El valor de n debe ser un número entero no negativo.")
        if n == 1:
            return 3
        else:
            return 2 * n + f(n - 1)
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

print(f"\nEjercicio 28, Secuencia de valor 3 cuando n es igual a 1 y Σ(2 * n + f(n - 1)) el resto de las veces:\n{f(3)}\n")

# Ejercicio 29
def biseccion(f, n, m):
    try:
        if not isinstance(n, (int, float)) or not isinstance(m, (int, float)):
            raise ValueError("n y m deben ser números")
        if (f(n) * f(m)) > 0:
            raise ValueError("f(n) y f(m) deben tener signos opuestos")
        x = (n + m) / 2
        if abs(f(x)) < 1e-6:
            return x
        else:
            if (f(n) * f(x)) < 0:
                return biseccion(f, n, x)
            else:
                return biseccion(f, x, m)
            
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

f = lambda x: x * 2/4 + 20
print(f"\nEjercicio 29, Buscador de Raices - Metodo de la Biseccion:\n{int(biseccion(f,-100,5))}\n")