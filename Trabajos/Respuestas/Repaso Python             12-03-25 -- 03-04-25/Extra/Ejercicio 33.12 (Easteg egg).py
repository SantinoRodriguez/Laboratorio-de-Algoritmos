import random

# Generar una lista de cumpleaño aleatorio
def GenerarCumpleaños(CantidadPersonas):
    ListaCumpleaños = []
    for _ in range(CantidadPersonas): # Se usa "_" cuando es irrelevante, al igual que con "i" solo que no aparece dentro del bucle
        Cumpleaños = random.randint(1, 365)
        ListaCumpleaños.append(Cumpleaños)
    return ListaCumpleaños

# Función para verificar si hay al menos un cumpleaños repetido
def HayCumpleañosRepetidos(ListaCumpleaños):
    return len(ListaCumpleaños) != len(set(ListaCumpleaños))

# Experimento principal para probar la paradoja del cumpleaños
def ProbarParadoja():
    Intentos = 5000

    for CantidadPersonas in range(5, 101, 5):
        CasosConCoincidencia = 0

        for _ in range(Intentos):
            ListaCumpleaños = GenerarCumpleaños(CantidadPersonas)
            if HayCumpleañosRepetidos(ListaCumpleaños):
                CasosConCoincidencia += 1

        Probabilidad = (CasosConCoincidencia / Intentos) * 100
        print(f"Para {CantidadPersonas} personas, la probabilidad de al menos un cumpleaños repetido es aproximadamente {Probabilidad:.2f}%")
        # ":", es el comienzo del formato del print; ".2", es la cantidad de decimales; "f", significa es de tipo Float

ProbarParadoja()