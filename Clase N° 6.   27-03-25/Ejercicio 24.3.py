def EnviarMensajes(Mensajes):
    MensajesEnviados = []  
    while Mensajes:
        Mensaje = Mensajes.pop(0)  
        print(Mensaje)  
        MensajesEnviados.append(Mensaje)  
    return MensajesEnviados

Mensajes = [
    "¡Hola! ¿Cómo Estás?",
    "Espero Que Tengas Un Buen Día.",
    "Recuerda Tomar Agua.",
    "No Olvides Sonreír.",
    "Sigue Persiguiendo Tus Sueños."
]

MensajesCopia = Mensajes.copy()
MensajesEnviados = EnviarMensajes(MensajesCopia)

print("\nLista Original De Mensajes:", Mensajes)
print("Lista De Mensajes Enviados:", MensajesEnviados)
