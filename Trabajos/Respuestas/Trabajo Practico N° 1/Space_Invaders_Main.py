import pygame
import sys
import os
from Space_Invaders import *  # Asegúrate de que este archivo esté en la misma carpeta
#import Space_Invaders_2 as nm

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
    texto_original = FUENTE.render("The Original Game".title(), True, (255, 238, 0))  # Amarillo Space Invaders
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

        PANTALLA.blit(imagen_inicio, (0, 0))                      # Fondo
        PANTALLA.blit(texto_original, rect_original)              # Texto superior
        PANTALLA.blit(texto_presionar, rect_presionar)
        PANTALLA.blit(texto_produced, rect_produced)              # Texto inferior
        PANTALLA.blit(texto_licencia, rect_licencia)              # Texto inferior
        pygame.display.flip() 

# =============== MENÚ PRINCIPAL ===============================
ANCHO_MENU = 800
ALTO_MENU = 600

# Colores
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Cargar fondo de la segunda pantalla
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
    while ejecutando:
        pos_mouse = pygame.mouse.get_pos()

        # Dibujar fondo y logo
        PANTALLA.blit(imagen_menu, (0, 0))

        # Botones uno al lado del otro en la parte inferior
        y_botones = ALTO_MENU - 100
        boton_1_jugador = dibujar_boton("1 Jugador", ANCHO_MENU // 2 - 260, y_botones, 200, 60, AZUL, VERDE, pos_mouse)
        boton_multijugador = dibujar_boton("Multijugador", ANCHO_MENU // 2 + 60, y_botones, 200, 60, AZUL, VERDE, pos_mouse)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or (evento.type == KEYUP and evento.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_1_jugador.collidepoint(evento.pos):
                    game = SpaceInvaders()
                    game.main()
                    ejecutando = False
                if boton_multijugador.collidepoint(evento.pos):
                    # game = nm.SpaceInvaders()
                    # game.main2()
                    ejecutando = False

        pygame.display.flip()

# =============== EJECUCIÓN GENERAL ===========================
pantalla_inicio()
menu_principal()
