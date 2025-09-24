import csv

def leer_ventas(nombre_archivo):
    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            ventas = []
            for fila in lector:
                fila['precio'] = float(fila['precio'])
                fila['cantidad'] = int(fila['cantidad'])
                ventas.append(fila)
            return ventas
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no fue encontrado.")
        return []
    except Exception as e:
        print(f"Error inesperado: {e}")
        return []

def ingresos_por_genero(ventas):
    ingresos = {}
    ingreso_total = 0
    for venta in ventas:
        genero = venta['genero'] 
        ingreso = venta['precio'] * venta['cantidad'] 
        ingreso = round(ingreso, 2)
        ingreso_total += ingreso
        ingreso_total = round(ingreso_total, 2)
        if genero in ingresos:
            ingresos[genero] += ingreso
        else:
            ingresos[genero] = ingreso
    return ingresos, ingreso_total

def generar_informe(nombre_archivo):
    ventas = leer_ventas(nombre_archivo)
    if not ventas:
        return
    ingresos, ingreso_total = ingresos_por_genero(ventas)
    print("Ingresos por género:")
    for genero, ingreso in ingresos.items():
        print(f"{genero}: ${ingreso}")
    print(f"\nIngreso total: ${ingreso_total}")

if __name__ == '__main__':
    generar_informe('ventas.csv')
