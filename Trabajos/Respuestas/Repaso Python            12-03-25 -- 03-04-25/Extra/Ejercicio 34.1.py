from Ejercicio_34_1_Extension import CiudadPais

def TestCityCountry():
    Resultado = CiudadPais('santiago', 'chile')
    assert Resultado == 'Santiago, Chile'
