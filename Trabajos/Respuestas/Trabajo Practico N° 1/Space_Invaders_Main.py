import pygame
import sys
import os
import config
from Space_Invaders import *  # Asegúrate de que este archivo esté en la misma carpeta
import Space_Invaders_2 as nm

# =============== CONFIGURAR VENTANA CENTRADA ==================
os.environ['SDL_VIDEO_CENTERED'] = '1'

# =============== INICIALIZAR PYGAME ============================
pygame.init()

# Cargar fuente personalizada desde la carpeta Letras
FUENTE = pygame.font.Font("Letras/space_invaders.ttf", 20)
FUENTE_NEGRITA = pygame.font.Font("Letras/space_invaders.ttf", 20)
FUENTE_NEGRITA.set_bold(True)

# =============== PRIMERA PANTALLA - IMAGEN INICIAL =============
ANCHO_INICIO = 532
ALTO_INICIO = 800
PANTALLA = pygame.display.set_mode((ANCHO_INICIO, ALTO_INICIO))
pygame.display.set_caption("Space Invaders - Inicio")

imagen_inicio = pygame.image.load("Images/image_init.jpeg")
imagen_inicio = pygame.transform.scale(imagen_inicio, (ANCHO_INICIO, ALTO_INICIO))

def pantalla_inicio():
    # ========== Crear los textos ==========
    texto_original = FUENTE.render("The Original Game".title(), True, (255, 238, 0))
    texto_produced = FUENTE_NEGRITA.render("Produced By Fuchs".title(), True, (255, 255, 255))
    texto_licencia = FUENTE_NEGRITA.render("Licenced By Huergo Inst.".title(), True, (255, 255, 255))
    texto_presionar = FUENTE.render("Push Start Button".title(), True, (255, 238, 0))

    # ========== Posicionar los textos ==========
    rect_original = texto_original.get_rect(center=(ANCHO_INICIO // 2,  222))
    rect_produced = texto_produced.get_rect(center=(ANCHO_INICIO // 2, 685))
    rect_licencia = texto_licencia.get_rect(center=(ANCHO_INICIO // 2, 715))
    rect_presionar = texto_presionar.get_rect(center=(ANCHO_INICIO // 2, 300))

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                esperando = False

        PANTALLA.blit(imagen_inicio, (0, 0))
        PANTALLA.blit(texto_original, rect_original)
        PANTALLA.blit(texto_presionar, rect_presionar)
        PANTALLA.blit(texto_produced, rect_produced)
        PANTALLA.blit(texto_licencia, rect_licencia)
        pygame.display.flip()

# =============== MENÚ PRINCIPAL ===============================
ANCHO_MENU = 800
ALTO_MENU = 600

# Colores
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
AMARILLO = (255, 255, 0)

# Fondo de la segunda pantalla
imagen_menu = pygame.image.load("Images/image_second.webp")
imagen_menu = pygame.transform.scale(imagen_menu, (ANCHO_MENU, ALTO_MENU))

def dibujar_boton(texto, x, y, ancho, alto, color_base, color_hover, pos_mouse):
    rect = pygame.Rect(x, y, ancho, alto)
    color = color_hover if rect.collidepoint(pos_mouse) else color_base
    pygame.draw.rect(PANTALLA, color, rect, border_radius=10)
    texto_render = FUENTE.render(texto, True, BLANCO)
    texto_rect = texto_render.get_rect(center=rect.center)
    PANTALLA.blit(texto_render, texto_rect)
    return rect

def menu_principal():
    global PANTALLA
    PANTALLA = pygame.display.set_mode((ANCHO_MENU, ALTO_MENU))
    
    ejecutando = True
    # Variable para controlar si se muestra el submenú de multijugador
    mostrar_submenu_multi = False
    
    while ejecutando:
        pos_mouse = pygame.mouse.get_pos()

        # Dibujar fondo
        PANTALLA.blit(imagen_menu, (0, 0))

        # Botón de mute en esquina superior derecha
        texto_mute = "Audio ON" if not config.MUTEADO else "Audio OFF"
        boton_mute = dibujar_boton(texto_mute, ANCHO_MENU - 150, 20, 130, 40, VERDE, ROJO, pos_mouse)

        # Si no estamos en el submenú, mostrar los botones principales
        if not mostrar_submenu_multi:
            y_botones = ALTO_MENU - 100
            boton_1_jugador = dibujar_boton("1 Jugador", ANCHO_MENU // 2 - 260, y_botones, 200, 60, AZUL, VERDE, pos_mouse)
            boton_multijugador = dibujar_boton("Multijugador", ANCHO_MENU // 2 + 60, y_botones, 200, 60, AZUL, VERDE, pos_mouse)
        else:
            # Mostrar los botones del submenu multijugador
            y_botones = ALTO_MENU - 100
            boton_1vs1 = dibujar_boton("1 vs 1", ANCHO_MENU // 2 - 260, y_botones, 200, 60, AZUL, VERDE, pos_mouse)
            boton_2vsCpu = dibujar_boton("2 vs Cpu", ANCHO_MENU // 2 + 60, y_botones, 200, 60, AZUL, VERDE, pos_mouse)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Manejo de tecla Escape
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                if mostrar_submenu_multi:
                    # Si estamos en el submenú, volver al menú principal
                    mostrar_submenu_multi = False
                elif ejecutando == False:
                    # Si estamos en el menú principal, salir del juego
                    pygame.quit()
                    sys.exit()
                    
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if not mostrar_submenu_multi:
                    # Interacción con los botones del menú principal
                    if boton_1_jugador.collidepoint(evento.pos):
                        ejecutando = False
                        game = SpaceInvaders()
                        game.main()
                    if boton_multijugador.collidepoint(evento.pos):
                        mostrar_submenu_multi = True
                else:
                    # Interacción con los botones del submenú multijugador
                    if boton_1vs1.collidepoint(evento.pos):
                        pass  # Aquí va la función para el modo 1vs1
                    if boton_2vsCpu.collidepoint(evento.pos):
                        ejecutando = False
                        SCREEN = pygame.display.set_mode((1000, 800))
                        game2 = nm.SpaceInvaders2()
                        game2.main2()
                
                # El botón de mute funciona en ambos menús
                if boton_mute.collidepoint(evento.pos):
                    config.MUTEADO = not config.MUTEADO  # Alterna entre mute y unmute

        pygame.display.flip()

# =============== EJECUCIÓN GENERAL ===========================
pantalla_inicio()
menu_principal()