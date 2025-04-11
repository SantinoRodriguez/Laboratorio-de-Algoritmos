import pygame
from Space_Invaders_Main import menu_principal
from Space_Invaders import SpaceInvaders

pygame.init()

def main():
    estado = 'menu'

    while True:
        if estado == 'menu':
            resultado = menu_principal()
            if resultado == 'jugar':
                juego = SpaceInvaders()
                estado = juego.main()  # Devuelve 'menu' si se quiere volver
            elif resultado == 'multi':
                print("Modo multijugador no implementado")
                estado = 'menu'
        elif estado == 'salir':
            break

if __name__ == '__main__':
    main()