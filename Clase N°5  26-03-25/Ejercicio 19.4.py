import time
try:
    while True:
        print("Presiona CTRL+C para detener el loop.")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nLoop Detenido Con CTRL+C. ¡Hasta luego!")
