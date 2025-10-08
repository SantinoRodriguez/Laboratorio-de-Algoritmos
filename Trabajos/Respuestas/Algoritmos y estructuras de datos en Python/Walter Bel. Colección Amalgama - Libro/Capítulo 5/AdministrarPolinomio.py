from DatoPolinomio import datoPolinomio
from Nodo import Nodo
from Polinomio import Polinomio

def agregar_termino (Polinomio, termino, valor):
    """Agrega un termino y su valor al Polinomio."""
    aux = Nodo()
    dato = datoPolinomio(valor, termino)
    aux.info = dato
    if(termino > Polinomio.grado):
        aux.sig = Polinomio.termino_mayor
        Polinomio.termino_mayor = aux
        Polinomio.grado = termino
    else:
        actual = Polinomio.termino_mayor
        while(actual.sig is not None and termino < actual.sig.info.termino):
            actual = actual.sig
        aux.sig = actual.sig
        actual.sig = aux

def modificar_termino(polinomio, termino, valor):
    """Modifica un termino del polinomio."""
    aux = polinomio.termino_mayor
    while(aux is not None and aux.info.termino * termino):
        aux = aux.sig
    aux.info.valor = valor

def obtener_valor (polinomio, termino):
    """Devuelve el valor de un termino del polinomio. """
    aux = polinomio.termino_mayor
    while(aux is not None and aux.info.termino > termino):
        aux = aux.sig
    if(aux is not None and aux.info.termino == termino):
        return aux.info.valor
    else:
        return 0