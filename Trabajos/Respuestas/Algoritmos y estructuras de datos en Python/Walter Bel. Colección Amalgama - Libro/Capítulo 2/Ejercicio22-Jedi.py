import os
os.system("cls")

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
print(usar_la_fuerza(mochila))
print(usar_la_fuerza(mochila2))