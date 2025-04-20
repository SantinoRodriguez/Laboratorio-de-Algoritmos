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
FUENTE = pygame.font.Font("Letras/space_invaders.ttf", int(20 * config.SCALE_FACTOR))
FUENTE_NEGRITA = pygame.font.Font("Letras/space_invaders.ttf", int(20 * config.SCALE_FACTOR))
FUENTE_NEGRITA.set_bold(True)

# =============== PRIMERA PANTALLA - IMAGEN INICIAL =============
INICIO_WIDTH = config.get_inicio_width()
INICIO_HEIGHT = config.get_inicio_height()
PANTALLA = pygame.display.set_mode((INICIO_WIDTH, INICIO_HEIGHT))
pygame.display.set_caption("Space Invaders - Inicio")

imagen_inicio = pygame.image.load("Images/image_init.jpeg")
imagen_inicio = pygame.transform.scale(imagen_inicio, (INICIO_WIDTH, INICIO_HEIGHT))

def pantalla_inicio():
    # ========== Crear los textos ==========
    texto_original = FUENTE.render("The Original Game".title(), True, (255, 238, 0))
    texto_produced = FUENTE_NEGRITA.render("Produced By Fuchs".title(), True, (255, 255, 255))
    texto_licencia = FUENTE_NEGRITA.render("Licenced By Huergo Inst.".title(), True, (255, 255, 255))
    texto_presionar = FUENTE.render("Push Start Button".title(), True, (255, 238, 0))

    # ========== Posicionar los textos ==========
    # Usamos las funciones de escala para adaptar las posiciones
    rect_original = texto_original.get_rect(center=(scale_value(INICIO_WIDTH // 2), scale_value(222)))
    rect_produced = texto_produced.get_rect(center=(scale_value(INICIO_WIDTH // 2), scale_value(685)))
    rect_licencia = texto_licencia.get_rect(center=(scale_value(INICIO_WIDTH // 2), scale_value(715)))
    rect_presionar = texto_presionar.get_rect(center=(scale_value(INICIO_WIDTH // 2), scale_value(300)))

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
ANCHO_MENU = config.get_menu_width()
ALTO_MENU = config.get_menu_height()

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
    # Escalar las posiciones y dimensiones
    x = scale_value(x)
    y = scale_value(y)
    ancho = scale_value(ancho)
    alto = scale_value(alto)
    
    rect = pygame.Rect(x, y, ancho, alto)
    color = color_hover if rect.collidepoint(pos_mouse) else color_base
    pygame.draw.rect(PANTALLA, color, rect, border_radius=10)
    
    texto_render = FUENTE.render(texto, True, BLANCO)
    texto_rect = texto_render.get_rect(center=rect.center)
    PANTALLA.blit(texto_render, texto_rect)
    
    return rect

def abrir_menu_settings():
    corriendo = True
    cambiando_izquierda = False
    cambiando_derecha = False

    while corriendo:
        PANTALLA.fill((30, 30, 30))
        pos_mouse = pygame.mouse.get_pos()

        fuente = pygame.font.SysFont(None, 36)
        mute_texto = f"Mute: {'ON' if config.get_muteado() else 'OFF'}"
        tecla_izq = pygame.key.name(config.get_izquierda()).upper()
        tecla_der = pygame.key.name(config.get_derecha()).upper()

        # Escalar las posiciones y tamaños de los botones
        mute_rect = pygame.Rect(scale_value(300), scale_value(200), scale_value(200), scale_value(40))
        izquierda_rect = pygame.Rect(scale_value(300), scale_value(260), scale_value(200), scale_value(40))
        derecha_rect = pygame.Rect(scale_value(300), scale_value(320), scale_value(200), scale_value(40))
        volver_rect = pygame.Rect(scale_value(300), scale_value(380), scale_value(200), scale_value(40))

        # Colores al pasar el ratón
        mute_color = (200, 0, 0) if mute_rect.collidepoint(pos_mouse) else (150, 0, 0)
        izq_color = (0, 200, 0) if izquierda_rect.collidepoint(pos_mouse) else (0, 150, 0)
        der_color = (0, 200, 0) if derecha_rect.collidepoint(pos_mouse) else (0, 150, 0)
        volver_color = (150, 150, 255) if volver_rect.collidepoint(pos_mouse) else (100, 100, 255)

        if cambiando_izquierda:
            izq_color = (255, 255, 0)
        if cambiando_derecha:
            der_color = (255, 255, 0)

        # Dibujar rectángulos y textos escalados
        pygame.draw.rect(PANTALLA, mute_color, mute_rect)
        PANTALLA.blit(fuente.render(mute_texto, True, (255, 255, 255)), (mute_rect.x + scale_value(10), mute_rect.y + scale_value(5)))

        pygame.draw.rect(PANTALLA, izq_color, izquierda_rect)
        PANTALLA.blit(fuente.render(f"Tecla Izquierda: {tecla_izq}", True, (255, 255, 255)), (izquierda_rect.x + scale_value(10), izquierda_rect.y + scale_value(5)))

        pygame.draw.rect(PANTALLA, der_color, derecha_rect)
        PANTALLA.blit(fuente.render(f"Tecla Derecha: {tecla_der}", True, (255, 255, 255)), (derecha_rect.x + scale_value(10), derecha_rect.y + scale_value(5)))

        pygame.draw.rect(PANTALLA, volver_color, volver_rect)
        PANTALLA.blit(fuente.render("Volver", True, (255, 255, 255)), (volver_rect.x + scale_value(60), volver_rect.y + scale_value(5)))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if mute_rect.collidepoint(event.pos):
                    config.toggle_muteado()  # Ya alterna internamente
                elif izquierda_rect.collidepoint(event.pos):
                    cambiando_izquierda = True
                    cambiando_derecha = False
                elif derecha_rect.collidepoint(event.pos):
                    cambiando_derecha = True
                    cambiando_izquierda = False
                elif volver_rect.collidepoint(event.pos):
                    corriendo = False
            elif event.type == pygame.KEYDOWN:
                if cambiando_izquierda:
                    config.set_izquierda(event.key)
                    cambiando_izquierda = False
                elif cambiando_derecha:
                    config.set_derecha(event.key)
                    cambiando_derecha = False
                elif event.key == pygame.K_ESCAPE:
                    corriendo = False

def menu_principal():
    global PANTALLA
    PANTALLA = pygame.display.set_mode((ANCHO_MENU, ALTO_MENU))
    pygame.display.set_caption("Space Invaders - Menú Principal")
    
    ejecutando = True
    # Variable para controlar si se muestra el submenú de multijugador
    mostrar_submenu_multi = False
    
    while ejecutando:
        pos_mouse = pygame.mouse.get_pos()
        
        # Dibujar fondo escalado
        PANTALLA.blit(imagen_menu, (0, 0))
        
        # Dibujar botón de configuración escalado
        settings_button_rect = pygame.Rect(scale_value(650), scale_value(30), scale_value(125), scale_value(35))
        settings_color = (150, 150, 255) if settings_button_rect.collidepoint(pos_mouse) else (100, 100, 255)
        pygame.draw.rect(PANTALLA, settings_color, settings_button_rect)
        texto = FUENTE.render("Settings", True, (255, 255, 255))
        PANTALLA.blit(texto, (settings_button_rect.x + scale_value(5), settings_button_rect.y + scale_value(5)))
        
        # Si no estamos en el submenú, mostrar los botones principales
        if not mostrar_submenu_multi:
            y_botones = ALTO_MENU - scale_value(100)
            boton_1_jugador = dibujar_boton("1 Jugador", ANCHO_MENU // 2 - scale_value(260), y_botones, scale_value(200), scale_value(60), AZUL, VERDE, pos_mouse)
            boton_multijugador = dibujar_boton("Multijugador", ANCHO_MENU // 2 + scale_value(60), y_botones, scale_value(200), scale_value(60), AZUL, VERDE, pos_mouse)
        else:
            # Mostrar los botones del submenu multijugador
            y_botones = ALTO_MENU - scale_value(100)
            boton_1vs1 = dibujar_boton("1 vs 1", ANCHO_MENU // 2 - scale_value(260), y_botones, scale_value(200), scale_value(60), AZUL, VERDE, pos_mouse)
            boton_2vsCpu = dibujar_boton("2 vs Cpu", ANCHO_MENU // 2 + scale_value(60), y_botones, scale_value(200), scale_value(60), AZUL, VERDE, pos_mouse)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Manejar el clic en botones
            if evento.type == pygame.MOUSEBUTTONDOWN:
                # Verificar si se hizo clic en el botón de configuración
                if settings_button_rect.collidepoint(evento.pos):
                    abrir_menu_settings()
                
                if not mostrar_submenu_multi:
                    # Interacción con los botones del menú principal
                    if boton_1_jugador.collidepoint(evento.pos):
                        return '1player'  # Devolver el modo seleccionado
                    if boton_multijugador.collidepoint(evento.pos):
                        mostrar_submenu_multi = True
                else:
                    # Interacción con los botones del submenú multijugador
                    if boton_1vs1.collidepoint(evento.pos):
                        return '1vs1'  # Devolver el modo seleccionado
                    if boton_2vsCpu.collidepoint(evento.pos):
                        return '2vsCpu'  # Devolver el modo seleccionado
            
            # Manejo de tecla Escape
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                if mostrar_submenu_multi:
                    # Si estamos en el submenú, volver al menú principal
                    mostrar_submenu_multi = False
                else:
                    # Si estamos en el menú principal, salir del juego
                    return 'salir'  # Devolver salir para terminar el programa

        pygame.display.flip()

# =============== EJECUCIÓN GENERAL ===========================
if __name__ == "__main__":
    pantalla_inicio()
    menu_principal()