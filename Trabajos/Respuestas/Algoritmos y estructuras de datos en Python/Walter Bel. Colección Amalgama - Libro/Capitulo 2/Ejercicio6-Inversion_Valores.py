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

print(inversion("TOMATE"))