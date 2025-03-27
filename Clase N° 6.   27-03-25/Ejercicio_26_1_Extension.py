def ImprimirModelos(DiseñosNoImpresos, ModelosCompletados):
    while DiseñosNoImpresos:
        DiseñoActual = DiseñosNoImpresos.pop()
        print(f"Imprimiendo Modelo: {DiseñoActual}")
        ModelosCompletados.append(DiseñoActual)

def MostrarModelosCompletados(ModelosCompletados):
    print("\nLos siguientes modelos han sido impresos:")
    for ModeloCompletado in ModelosCompletados:
        print(ModeloCompletado)
