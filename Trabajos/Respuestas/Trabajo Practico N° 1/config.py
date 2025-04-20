import pygame
import json
import os

# Archivo de configuración
CONFIG_FILE = "config.json"

# Resolución base de referencia (16:9)
BASE_WIDTH = 1920
BASE_HEIGHT = 1080

# Detectar resolución actual de la pantalla
pygame.init()
info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h

# Calcular la proporción de escala
SCALE_X = SCREEN_WIDTH / BASE_WIDTH
SCALE_Y = SCREEN_HEIGHT / BASE_HEIGHT
SCALE_FACTOR = min(SCALE_X, SCALE_Y)  # Usamos el menor para evitar distorsión

# Adaptar resoluciones y posiciones
def scale_value(value):
    """Escala un valor basado en la resolución actual"""
    return int(value * SCALE_FACTOR)

# Dimensiones globales para Space Invaders
GAME_WIDTH = scale_value(800)
GAME_HEIGHT = scale_value(600)
GAME2_WIDTH = scale_value(1000)
GAME2_HEIGHT = scale_value(800)
MENU_WIDTH = scale_value(800)
MENU_HEIGHT = scale_value(600)
INICIO_WIDTH = scale_value(532)
INICIO_HEIGHT = scale_value(800)

# Posiciones y tamaños escalados
BLOCKERS_POSITION = scale_value(450)
ENEMY_DEFAULT_POSITION = scale_value(65)
ENEMY_MOVE_DOWN = scale_value(35)

# Valores por defecto
DEFAULT_CONFIG = {
    "izquierda": pygame.K_LEFT,
    "derecha": pygame.K_RIGHT,
    "muteado": False,
    "screen_width": SCREEN_WIDTH,
    "screen_height": SCREEN_HEIGHT
}

# Variables en memoria
Izquierda1 = DEFAULT_CONFIG["izquierda"]
Derecha1 = DEFAULT_CONFIG["derecha"]
MUTEADO = DEFAULT_CONFIG["muteado"]

def guardar_configuracion():
    """Guarda los valores actuales en el archivo JSON"""
    try:
        config_data = {
            "izquierda": Izquierda1,
            "derecha": Derecha1,
            "muteado": MUTEADO,
            "screen_width": SCREEN_WIDTH,
            "screen_height": SCREEN_HEIGHT
        }
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config_data, f)
        print("✔ Configuración guardada")
    except Exception as e:
        print(f"❌ Error al guardar configuración: {e}")

def cargar_configuracion():
    """Carga la configuración desde el archivo JSON si existe"""
    global Izquierda1, Derecha1, MUTEADO
    try:
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                config_data = json.load(f)
            Izquierda1 = config_data.get("izquierda", DEFAULT_CONFIG["izquierda"])
            Derecha1 = config_data.get("derecha", DEFAULT_CONFIG["derecha"])
            MUTEADO = config_data.get("muteado", DEFAULT_CONFIG["muteado"])
            print("✔ Configuración cargada")
        else:
            print("ℹ No se encontró config.json, usando valores por defecto")
    except Exception as e:
        print(f"❌ Error al cargar configuración: {e}")

# Getters - Configuración
def get_izquierda():
    return Izquierda1

def get_derecha():
    return Derecha1

def get_muteado():
    return MUTEADO

# Getters - Resolución
def get_game_width():
    return GAME_WIDTH

def get_game_height():
    return GAME_HEIGHT

def get_game2_width():
    return GAME2_WIDTH

def get_game2_height():
    return GAME2_HEIGHT

def get_menu_width():
    return MENU_WIDTH

def get_menu_height():
    return MENU_HEIGHT

def get_inicio_width():
    return INICIO_WIDTH

def get_inicio_height():
    return INICIO_HEIGHT

def get_blockers_position():
    return BLOCKERS_POSITION

def get_enemy_default_position():
    return ENEMY_DEFAULT_POSITION

def get_enemy_move_down():
    return ENEMY_MOVE_DOWN

def get_scale_factor():
    return SCALE_FACTOR

# Setters
def set_izquierda(tecla):
    global Izquierda1
    Izquierda1 = tecla
    guardar_configuracion()

def set_derecha(tecla):
    global Derecha1
    Derecha1 = tecla
    guardar_configuracion()

def set_muteado(valor):
    global MUTEADO
    MUTEADO = valor
    guardar_configuracion()

def toggle_muteado():
    """Cambia el estado de muteado y lo guarda"""
    global MUTEADO
    MUTEADO = not MUTEADO
    guardar_configuracion()
    return MUTEADO

def scale_size(width, height):
    """Escala un par (ancho, alto) con el SCALE_FACTOR."""
    return (int(width * SCALE_FACTOR), int(height * SCALE_FACTOR))

def get_scaled_rect(x, y, width, height):
    # Escalar las posiciones (x, y) y el tamaño (width, height)
    sx = scale_value(x)
    sy = scale_value(y)
    sw, sh = scale_size(width, height)  # Escalar el tamaño

    # Crear el rectángulo escalado con las posiciones escaladas y tamaño escalado
    return pygame.Rect(sx, sy, sw, sh)

# Cargar al inicio
cargar_configuracion()