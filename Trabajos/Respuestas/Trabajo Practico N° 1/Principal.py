import pygame
from Space_Invaders_Main import menu_principal
from Space_Invaders import SpaceInvaders
from Space_Invaders_2 import SpaceInvaders2

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
                juego2 = SpaceInvaders2()
                estado = juego2.main2()  # Devuelve 'menu' si se quiere volver
            elif resultado == 'salir':
                break
        elif estado == 'salir':
            break

if __name__ == '__main__':
    main()
