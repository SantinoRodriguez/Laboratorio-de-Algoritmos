Lenguajes = {'Juan': 'python', 'Sara': 'c', 'Eduardo': 'rust', 'Agustina': 'c#'}
Personas = ["Mateo", "Carlos", "Luis", "Sofía", "Pedro", "Julia", "Juan"]
for Persona in Personas:
    if Persona in Lenguajes:
        print(f"{Persona} Gracias Por Participar en la Encuesta")
    else:
        print(f"{Persona} Le invitamos a Participar")