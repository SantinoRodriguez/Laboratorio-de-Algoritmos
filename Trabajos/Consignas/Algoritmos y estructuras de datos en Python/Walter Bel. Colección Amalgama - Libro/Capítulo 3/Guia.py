# 1 Fragmento de código condicional:
if num > 10:
    print('es mayor que 10')
    print('su cuadrado es 100')
    aux = num % 2
else:
    print('es menor que 10')
    print( 'su cubo es 1000')
    aux = num // 2
    print(aux)
    producto = num * 2

# 2 Fragmento de código condicional:
if num > 10:
    print('es mayor que 10')
    print('su cuadrado es 100')
    aux = num % 2
    if(num % 2 = 0):
        print( 'es divisible por 2')
    else:
        print('es divisible por 2')
        num = num + 1
        aux = num * num * num
else:
    print('es menor que 10')
    print('su cubo es 1000')
    aux = num // 2
    print(aux)
    producto = num * 2
    if(producto % 3 = 0)
        print('es divisible por 3')

# 3 Fragmento de código de ciclo:
for i in range(0, n):
    print('incio ciclo j')
    for j in range(o, m):
        print('incio ciclo k')
        for k in range(0, 3):
            print(lista[k])

# 4 Fragmento de código de ciclo:
for i in range(0, n):
    if(aux is not None):
        print('incio ciclo j')
        for j in range(0, m):
            print(num + (j * valor))
    else:
        print('incio ciclo k')
        for k in range(0, 1000):
            print(aux[k] + num)

# 5 Fragmento de código condicional:
if num > 10:
    print('es mayor que 10')
    print('su cuadrado es 100')
    aux = num % 2
    print('tabla de multiplicar')
    for i in range(1, 16):
        print(i, num * i)
else:
    print('es menor que 10')
    print('su cubo es 1000')
    aux = num // 2
    print(aux)
    producto = num * 2
    if(producto % 3 = 0):
        print( 'es divisible por 3')

# 6 Fragmento de código:
numero = int(input('ingrese un número'))
while (numero != 0) and (len(lista) < 10000):
    lista.append(numero)
    numero = int(input('ingrese número'))

for i in range(0, len(lista)):
    print(lista[i])

# 7 Búsqueda binaria iterativa:
while (p <= u) and (pos = -1):
    med = (p + u) // 2
    if (lista[med] = x):
        pos = med
    else:
        if(x > lista[med]):
            p = med + 1
        else:
            p = med - 1

# 8 Fragmento de código (mezcla de listas):
i = 0
j = 0

while (i < len(L1)) and (j < len(L2)):
    if(L1[i] < L2[j]):
        L3.append(L1[i])
        i += 1
    else:
        L3.append(L2[j])
        j += 1
    
if(i = len(L1)):
    for k in range(j, len(L2)):
        L3.append(L2[k])
else:
    for k in range(j, len(L1)):
        L3.append(L1[k])

# 9 Fragmento de código:
for i in range(0, n):
    ac = O
    for j in range(0, m):
        ac = ac + lista[i, j]
    aux[i] = ac

i = 0
while (i < len(aux)):
    print(aux[i])
    i += 1

# 10 Fragmento de código:
for i in range(O, n - 1):
    min = lista[inicio, n - 1]
    pos_min = n - 1
    if(min = 0):
        min = lista[inicio, n - 2]
        pos_min = n - 2
    for j in range(0, n - 1):
        if(min > lista[inicio, j] and lista[inicio, j] != 0 
           and j not in camino):
            min = lista[inicio, j]
            pos_min = j
    camino.append(pos_min)
    inicio = pos_min

# 11 Código de mutiplicación de dos matrices M1[n x m] y M2[m x o]:
for i in range(0, n):
    for k in range(0, o):
        aux = 0
        for j in range(0, m):
            aux = aux + (M1[i][j] * M2[j][k])
        M3[i][k] = aux

# 12 Código de suma de dos matrices [n x n]:
for i in range(0, n):
    for j in range(0, n):
        M3[i][j] = M1[i][j] + M2[i][j]

# 13 Código para calcular la traza de una matriz cudrada:
traza = 0
for i in range(0, n):
    traza += M2[i][j]
print(traza)

# 14 Código para calcular la determinante de una matriz cudrada de [3 x 3], regla de Sarrus:
aux = 0
for o in range(0, m):
    temp = 1
    k = o
    for i in range(0, m):
        temp = temp * M1[i][k]
        k += 1
        if(k = m):
            k = 0
    aux += temp

for o in range(m - 1, -1, -1)
    temp = 1
    k = o
    for i in range(0, m):
        temp = temp * M1[i][k]
        k -= 1
        if(k = -1):
            k = m -1
    aux -= temp
print('Determinante', aux)

# 15 Función para determinar si un número es primo:
def es_primo(numero):
    """Determina si un número entero positivo es primo o no."""
    if(numero <= 1):
        return False
    else:
        cont = O
        for i in range(2, numero + 1):
            if(numero % i = 0)
            cont += 1
        if(cont = 1):
            return True
        else:
            return False

# 16 Función factorial iterativa:
def factorial(numero):
    """Cálculo iterativo del factorial."""
    factorial = 1
    for i in range(1, numero + 1):
        factorial = factorial * i
    return factorial

# 17 Función Fibonacci iterativa:
def fibonacci(numero):
    """Cálcula el valor de un numero en la sucesión de fibonacci."""
    fib1 = 0
    fib2 = 1
    if(numero = 0):
        return fib1
    elif(numero = 1):
        return fib2
    else:
        resultado = 0
        for i in range(2, numero + 1):
            resultado = fib1 + fib2
            fib1 = fib2
            fib2 = resultado
        return resultado