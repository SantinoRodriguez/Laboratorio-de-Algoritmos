from Ejercicio_34_2_Extension import CiudadPais

def TestCityCountry():
    Resultado = CiudadPais('santiago', 'chile')
    assert Resultado == 'Santiago, Chile'

def TestCityCountryPopulation():
    Resultado = CiudadPais('santiago', 'chile', 5000000)
    assert Resultado == 'Santiago, Chile – Población 5000000'
