import random
import time
import os
from AlgoritmosOrdenamiento.Countsort import *
os.system('cls')

def StarWars(personajes):
    # Crea un abecedario segun su valor de ASCII
    abecedario = {chr(letra): (letra - 65) for letra in range(ord("A"), ord("Z") + 1)}
    maximo = personajes[0][0]
    iniciales = []
    # Consigue la inicial de palabra con el valor más alto para el counting sort
    for nombre in personajes:
        iniciales.append(nombre)
        if (abecedario[nombre[0]] > abecedario[maximo]):
            maximo = nombre[0]
    countsort(abecedario[iniciales], abecedario[maximo])
    return countsort


personajes = [
    "Luke Skywalker",
    "Leia Organa",
    "Han Solo",
    "Darth Vader",
    "Obi-Wan Kenobi",
    "Yoda",
    "Anakin Skywalker",
    "Padmé Amidala",
    "Mace Windu",
    "Darth Maul",
    "Qui-Gon Jinn",
    "Rey",
    "Kylo Ren",
    "Finn",
    "Poe Dameron",
    "Hera Syndulla",
    "Ezra Bridger",
    "Ahsoka Tano",
    "Lando Calrissian",
    "Jabba the Hutt",
    "Chewbacca",
    "C-3PO",
    "R2-D2",
    "BB-8",
    "Boba Fett",
    "Grogu",
    "Bo-Katan Kryze",
    "Cad Bane",
    "Luminara Unduli",
    "Kit Fisto"
]

print(StarWars(personajes))