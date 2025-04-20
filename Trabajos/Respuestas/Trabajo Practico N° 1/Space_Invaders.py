from pygame import *
import sys
from os.path import abspath, dirname
from random import choice
from config import Izquierda1, Derecha1, MUTEADO, get_game_width, get_game_height, scale_size, scale_value

# Archivos
BASE_PATH = abspath(dirname(__file__))
FONT_PATH = BASE_PATH + '/Letras/'
IMAGE_PATH = BASE_PATH + '/Images/'
SOUND_PATH = BASE_PATH + '/Sounds/'

# Colores (R, G, B)
WHITE = (255, 255, 255)
GREEN = (78, 255, 87)
YELLOW = (241, 255, 0)
BLUE = (80, 255, 239)
PURPLE = (203, 0, 255)
RED = (237, 28, 36)

# Cargado de Imagenes y Pantalla
GAME_WIDTH = get_game_width()
GAME_HEIGTH = get_game_height()
SCREEN = display.set_mode((GAME_WIDTH, GAME_HEIGTH))
FONT = FONT_PATH + 'space_invaders.ttf'
IMG_NAMES = ['ship', 'mystery',
             'enemy1_1', 'enemy1_2',
             'enemy2_1', 'enemy2_2',
             'enemy3_1', 'enemy3_2',
             'explosionblue', 'explosiongreen', 'explosionpurple',
             'laser', 'enemylaser']
IMAGES = {name: image.load(IMAGE_PATH + '{}.png'.format(name)).convert_alpha()
          for name in IMG_NAMES} # Cargado Automatico de Imagenes en un diccionario

# Valores escalados de posiciones
ENEMY_DEFAULT_POSITION = scale_value(65)  # Originalmente 65
BLOCKERS_POSITION = scale_value(450)  # Originalmente 450
ENEMY_MOVE_DOWN = scale_value(35)  # Originalmente 35

class Ship(sprite.Sprite):  # Hereda la clase Sprite de Pygame (Util para objetos con hitbox)
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = IMAGES['ship']
        
        # Escalar la posición inicial de la nave
        self.rect = self.image.get_rect(topleft=(scale_value(375), scale_value(540)))  # Asigna la hitbox y la posición inicial de la nave escalada
        self.invulnerable = True  # Nueva nave es invulnerable al principio
        self.tiempoDeCreacion = time.get_ticks()  # Tiempo de creación
        self.speed = scale_value(5)  # Escalar la velocidad según la resolución

    def update(self, keys, currentTime, pantalla):  # Para reescribir la posición del objeto (Keys - Teclas, *Args - Agrupar argumentos)
        if self.invulnerable and (currentTime - self.tiempoDeCreacion > 1000):
            self.invulnerable = False
        
        # Limitar movimiento según los bordes de la pantalla escalados
        if keys[Izquierda1] and self.rect.x > scale_value(10):  # Escalar límite izquierdo
            self.rect.x -= self.speed  # Si se presiona la flecha izquierda y no está en el borde se mueve hacia allí
        
        if keys[Derecha1] and self.rect.x < scale_value(740):  # Escalar límite derecho
            self.rect.x += self.speed  # Si se presiona la flecha derecha y no está en el borde se mueve hacia allí
        
        pantalla.blit(self.image, self.rect)  # Dibuja el objeto

class Bullet(sprite.Sprite):  # Definiendo las balas
    def __init__(self, xpos, ypos, direction, speed, filename, side):
        sprite.Sprite.__init__(self)
        self.image = IMAGES[filename]
        
        # Escalar la posición inicial de la bala
        self.rect = self.image.get_rect(topleft=(scale_value(xpos), scale_value(ypos)))  # Cargar la imagen escalada
        self.speed = scale_value(speed)  # Escalar la velocidad de la bala
        self.direction = direction
        self.side = side  # Tirador
        self.filename = filename  # Nombre de la imagen

    def update(self, keys, *args):  # Para reescribir la posición del objeto (Keys - Teclas, *Args - Agrupar argumentos)
        if args and hasattr(args[-1], "blit"):  # Verifica que se haya pasado la pantalla y que tenga el método blit
            pantalla = args[-1]  # Extrae la pantalla desde los argumentos
            pantalla.blit(self.image, self.rect)  # Dibuja la imagen de la bala

        else:
            print("Advertencia: No se pasó pantalla correctamente a update()")
        
        self.rect.y += self.speed * self.direction  # Mueve la bala
        if self.rect.y < scale_value(15) or self.rect.y > scale_value(GAME_HEIGTH):
            self.kill()  # Eliminar la bala en caso que exceda los límites

class Enemy(sprite.Sprite):  # Definiendo a los enemigos
    def __init__(self, row, column):  # Para ubicar al enemigo dentro de una matriz de posiciones
        sprite.Sprite.__init__(self)
        self.row = row
        self.column = column
        self.images = []  # Una lista con las dos imágenes para alternar en la animación
        self.load_images()
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()  # Crea la hitbox

    def toggle_image(self):
        self.index += 1  # Agrega una imagen
        if self.index >= len(self.images):  # Si la cantidad de imágenes es igual o mayor a la cantidad de imágenes animables (2)
            self.index = 0  # Empezar con las imágenes de vuelta
        self.image = self.images[self.index]

    def update(self, *args):
        if args:  # Verifica que se haya pasado al menos un argumento
            pantalla = args[-1]  # Obtiene el último argumento como la pantalla
            pantalla.blit(self.image, self.rect)  # Solo lo dibuja

    def load_images(self):
        images = {0: ['1_2', '1_1'],
                  1: ['2_2', '2_1'],
                  2: ['2_2', '2_1'],
                  3: ['3_1', '3_2'],
                  4: ['3_1', '3_2'],
                  }  # Asigna un tipo de enemigo a cada fila

        img1, img2 = (IMAGES['enemy{}'.format(img_num)] for img_num in
                      images[self.row])  # Generador de imágenes
        escala = scale_size(40, 35)  # Usas la escala aquí una sola vez para las imágenes de los enemigos

        self.images.append(transform.scale(img1, escala))
        self.images.append(transform.scale(img2, escala))  # Asigna un tamaño a la imagen y la guarda dentro de la lista

class EnemiesGroup(sprite.Group):  # Extiende la clase Enemies para trabajar en conjunto con cada uno de ellos
    def __init__(self, columns, rows, enemyPosition):
        sprite.Group.__init__(self)
        self.enemies = [[None] * columns for _ in range(rows)]  # Crea una matriz vacía para la formación de enemigos
        self.columns = columns
        self.rows = rows
        self.leftAddMove = 0  # Agrega movimientos si los enemigos se mueren cerca del lado del límite
        self.rightAddMove = 0
        self.moveTime = 600  # Cuantos milisegundo tarda en moverse el grupo
        self.direction = 1  # 1 = Derecha - -1 = Izquierda
        self.rightMoves = 30
        self.leftMoves = 30  # Cantidad de paso para poder bajar a la siguiente columna
        self.moveNumber = 15
        self.timer = time.get_ticks()  # Último momento en el que se movieron
        self.bottom = scale_value(enemyPosition + ((rows - 1) * 45) + 35)  # Bottom = la hilera de abajo
        self._aliveColumns = list(range(columns))
        self._leftAliveColumn = 0
        self._rightAliveColumn = columns - 1

    def update(self, current_time):  # Actualizar al grupo
        if current_time - self.timer > self.moveTime:
            if self.direction == 1:  # ¿Cuántos movimientos horizontales quedan?
                max_move = self.rightMoves + self.rightAddMove
            else:
                max_move = self.leftMoves + self.leftAddMove

            if self.moveNumber >= max_move:  # Si se llega al límite
                self.leftMoves = 30 + self.rightAddMove  # Sumar movimientos
                self.rightMoves = 30 + self.leftAddMove
                self.direction *= -1  # Cambiar dirección
                self.moveNumber = 0  # Resetear valores
                self.bottom = 0
                for enemy in self:
                    enemy.rect.y += scale_value(ENEMY_MOVE_DOWN)  # Todos bajan una fila, escalar el movimiento
                    enemy.toggle_image()  # Alternar entre imágenes
                    if self.bottom < enemy.rect.y + scale_value(35): 
                        self.bottom = enemy.rect.y + scale_value(35)  # No pasarse
            else:  # Si no se llega al límite
                velocity = scale_value(10) if self.direction == 1 else -scale_value(10)  # Ajustar la velocidad para derecha o izquierda
                for enemy in self:
                    enemy.rect.x += velocity  # Los mueve de a un movimiento
                    enemy.toggle_image()  # Alterna entre imágenes
                self.moveNumber += 1  # Suma un movimiento

            self.timer += self.moveTime

    def add_internal(self, *sprites):  # Agrega el sprite a la matriz de enemigos
        super(EnemiesGroup, self).add_internal(*sprites)
        for s in sprites:
            self.enemies[s.row][s.column] = s

    def remove_internal(self, *sprites):  # Elimina de la matriz a los muertos y actualiza la velocidad
        super(EnemiesGroup, self).remove_internal(*sprites)
        for s in sprites:
            self.kill(s)
        self.update_speed()

    def is_column_dead(self, column):
        return not any(self.enemies[row][column] for row in range(self.rows))

    def random_bottom(self):
        col = choice(self._aliveColumns)  # Elige una de las columnas vivas al azar
        col_enemies = (self.enemies[row - 1][col]  # Devolvemos el enemigo de más abajo para poder disparar
                       for row in range(self.rows, 0, -1))
        return next((en for en in col_enemies if en is not None), None)

    def update_speed(self):
        if len(self) == 1:
            self.moveTime = 200  # Si solo queda un enemigo triplica la velocidad
        elif len(self) <= 10:
            self.moveTime = 400  # Si quedan entre 10 y 2 enemigos duplica la velocidad

    def kill(self, enemy):
        self.enemies[enemy.row][enemy.column] = None  # Elimina al enemigo de la matriz
        is_column_dead = self.is_column_dead(enemy.column)
        if is_column_dead:  # Verifica si la columna está vacía
            self._aliveColumns.remove(enemy.column)  # Lo elimina de la lista de los vivos

        if enemy.column == self._rightAliveColumn:  # Si era el borde derecho
            while self._rightAliveColumn > 0 and is_column_dead:
                self._rightAliveColumn -= 1  # Reduce el borde
                self.rightAddMove += 5  # Agrega movimientos en esa dirección
                is_column_dead = self.is_column_dead(self._rightAliveColumn)

        elif enemy.column == self._leftAliveColumn:  # Lo mismo pero con el lado izquierdo
            while self._leftAliveColumn < self.columns and is_column_dead:
                self._leftAliveColumn += 1
                self.leftAddMove += 5
                is_column_dead = self.is_column_dead(self._leftAliveColumn)

class Blocker(sprite.Sprite):  # Definir los bloques de protección
    def __init__(self, size, color, row, column):
        sprite.Sprite.__init__(self)
        self.height = scale_value(size)  # Escalar el tamaño
        self.width = scale_value(size)  # Escalar el tamaño
        self.color = color
        self.image = Surface((self.width, self.height))  # Crear el bloque escalado
        self.image.fill(self.color)  # Se le coloca el color
        self.rect = self.image.get_rect()  # Para manejar las colisiones
        self.row = row
        self.column = column

    def update(self, pantalla):
        pantalla.blit(self.image, self.rect)  # Dibujar el bloque

class Mystery(sprite.Sprite):  # Nave misteriosa
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = IMAGES['mystery']
        self.image = transform.scale(self.image, (scale_value(75), scale_value(35)))  # Escalar la imagen
        self.rect = self.image.get_rect(topleft=(-scale_value(80), scale_value(45)))  # Posición inicial ajustada a la escala
        self.row = 5
        self.moveTime = 25000  # Aparece cada 25 segundos
        self.direction = 1
        self.timer = time.get_ticks()
        
        # Cargar el sonido con volumen según esté muteado o no
        self.mysteryEntered = mixer.Sound(SOUND_PATH + 'mysteryentered.wav')
        self.mysteryEntered.set_volume(0.0 if MUTEADO else 0.3)
        
        self.playSound = True  # Controla si el sonido debe reproducirse nuevamente

    def update(self, keys, currentTime, *args):
        if args:  # Verifica que se haya pasado la pantalla
            pantalla = args[-1]  # Se extrae la pantalla desde los argumentos
            resetTimer = False
            passed = currentTime - self.timer

            if passed > self.moveTime:  # Solo si pasaron los milisegundos necesarios
                if (self.rect.x < 0 or self.rect.x > GAME_WIDTH) and self.playSound:
                    self.mysteryEntered.play()  # Reproduce el sonido de la nave
                    self.playSound = False  # Apaga el sonido de la nave
                if self.rect.x < 840 and self.direction == 1:
                    self.mysteryEntered.fadeout(4000)  # Reduce suavemente el sonido
                    self.rect.x += scale_value(2)  # Movimiento escalado
                    pantalla.blit(self.image, self.rect)  # Lo mueve para la derecha
                if self.rect.x > -100 and self.direction == -1:
                    self.mysteryEntered.fadeout(4000)  # Reduce suavemente el sonido
                    self.rect.x -= scale_value(2)  # Movimiento escalado
                    pantalla.blit(self.image, self.rect)  # Lo mueve para la izquierda

            if self.rect.x > 830:  # Si salió por la derecha
                self.playSound = True
                self.direction = -1  # Setea el movimiento para la izquierda
                resetTimer = True 
            if self.rect.x < -90:  # Si salió por la izquierda
                self.playSound = True
                self.direction = 1  # Setea el movimiento para la derecha
                resetTimer = True
            if passed > self.moveTime and resetTimer:
                self.timer = currentTime  # Resetea el reloj

class EnemyExplosion(sprite.Sprite):  # Definir la explosión de los enemigos tras su muerte
    def __init__(self, enemy, *groups):
        super(EnemyExplosion, self).__init__(*groups)
        self.image = transform.scale(self.get_image(enemy.row), (scale_value(40), scale_value(35)))  # Escalar imagen inicial
        self.image2 = transform.scale(self.get_image(enemy.row), (scale_value(50), scale_value(45)))  # Imagen más grande escalada
        self.rect = self.image.get_rect(topleft=(enemy.rect.x, enemy.rect.y))  # La coloca en la posición del enemigo
        self.timer = time.get_ticks()  # Guarda el momento de la explosión

    @staticmethod
    def get_image(row):
        img_colors = ['purple', 'blue', 'blue', 'green', 'green']
        return IMAGES['explosion{}'.format(img_colors[row])]  # Generador de imágenes

    def update(self, current_time, *args):
        if args:  # Solo si hay argumentos extra
            pantalla = args[-1]
            passed = current_time - self.timer
            if passed <= 100:
                pantalla.blit(self.image, self.rect)
            elif passed <= 200:
                pantalla.blit(self.image2, (self.rect.x - scale_value(6), self.rect.y - scale_value(6)))  # Explosión escalada
        if current_time - self.timer > 400:
            self.kill()

class MysteryExplosion(sprite.Sprite):  # Explosión de la nave misteriosa
    def __init__(self, mystery, score, *groups):
        super(MysteryExplosion, self).__init__(*groups)
        self.text = Text(FONT, scale_value(20), str(score), WHITE,  # Escalar el texto
                         mystery.rect.x + scale_value(20), mystery.rect.y + scale_value(6))
        self.timer = time.get_ticks()  # Guarda el tiempo de la explosión

    def update(self, current_time, *args):
        if args:  # Verifica si se pasó la pantalla
            pantalla = args[-1]  # Extrae la pantalla desde los argumentos
            passed = current_time - self.timer
            if passed <= 200 or 400 < passed <= 600:
                self.text.draw(pantalla)  # Muestra el texto en 2 intervalos; 0 - 200 , 400 - 600 milisegundos
            elif 600 < passed:
                self.kill()  # Luego de 600 milisegundos elimina el texto

class ShipExplosion(sprite.Sprite):  # Explosión de la nave propia
    def __init__(self, ship, *groups):
        super(ShipExplosion, self).__init__(*groups)
        self.image = IMAGES['ship']
        self.image = transform.scale(self.image, (scale_value(50), scale_value(50)))  # Escalar la imagen
        self.rect = self.image.get_rect(topleft=(ship.rect.x, ship.rect.y))
        self.timer = time.get_ticks()  # Guarda el tiempo de la explosión

    def update(self, current_time, *args):
        if args:
            pantalla = args[-1]  # Extrae la pantalla desde los argumentos si existe
            passed = current_time - self.timer
            if 300 < passed <= 600:
                pantalla.blit(self.image, self.rect)  # Durante 300 milisegundos dibuja de nuevo la nave
        if current_time - self.timer > 900:
            self.kill()  # Luego de 900 milisegundos la elimina

class Life(sprite.Sprite): 
    def __init__(self, xpos, ypos):
        sprite.Sprite.__init__(self)
        self.image = IMAGES['ship']
        self.image = transform.scale(self.image, (scale_value(23), scale_value(23)))  # Scales based on resolution
        self.rect = self.image.get_rect(topleft=(xpos, ypos))  # Define the initial position on screen

    def update(self, *args):
        if args and hasattr(args[-1], "blit"):  # Verifies if the last argument has a 'blit' method
            pantalla = args[-1]
            pantalla.blit(self.image, self.rect)

class Text(object):
    def __init__(self, textFont, size, message, color, xpos, ypos):
        self.font = font.Font(textFont, scale_value(size))  # Scale text size based on resolution
        self.surface = self.font.render(message, True, color)
        self.rect = self.surface.get_rect(topleft=(xpos, ypos))

    def draw(self, surface):
        surface.blit(self.surface, self.rect)  # Draws the text over the surface

class SpaceInvaders(object): # Codigo del Juego
    def __init__(self):
        mixer.pre_init(44100, -16, 1, 4096) # Es recomendado para las persona que usan Linux
        init()
        self.bullets = sprite.Group() # Inicializa el grupo de balas
        self.allSprites = sprite.Group() # También asegurate de tener este grupo para los .add()
        self.shipAlive = True
        self.score = 0
        self.player = Ship() 
        self.sounds = {
            'shoot': mixer.Sound('Sounds\shoot.wav'),
            'shoot2': mixer.Sound('Sounds\shoot2.wav')
        }
        self.allSprites.add(self.player)
        self.clock = time.Clock() # Timer
        self.caption = display.set_caption('Space Invaders') # Titulo
        self.screen = SCREEN # Pantalla
        self.menu = image.load(IMAGE_PATH + 'image_second.webp') # Cargar fondo
        self.menu = transform.scale(self.menu, (GAME_WIDTH, GAME_HEIGTH))
        self.background = image.load(IMAGE_PATH + 'background.jpg') # Cargar fondo
        self.startGame = False # Iniciar el juego
        self.mainScreen = True # El menu principal
        self.gameOver = False # Controla si el juego termino
        self.enemyPosition = ENEMY_DEFAULT_POSITION # Llama a la funcion para poder colocar a los enemigos
        # self.titleText = image.load(IMAGE_PATH + 'space_invaders_logo.png') # Titulo del fondo
        self.titleText2 = Text(FONT, 25, 'Press any key to continue', WHITE, 
                               201, 540) # Titulo de inicializacion
        self.gameOverText = Text(FONT, 50, 'Game Over', WHITE, 250, 270) # Texto al perder
        self.nextRoundText = Text(FONT, 50, 'Next Round', WHITE, 240, 270) # Texto para la proxima ronda
        """self.enemy1Text = Text(FONT, 25, '   =   10 pts', GREEN, 368, 400) 
        self.enemy2Text = Text(FONT, 25, '   =  20 pts', BLUE, 368, 450)
        self.enemy3Text = Text(FONT, 25, '   =  30 pts', PURPLE, 368, 500)
        self.enemy4Text = Text(FONT, 25, '   =  ?????', RED, 368, 550)"""
        self.scoreText = Text(FONT, 20, 'Score', WHITE, 5, 5)
        self.livesText = Text(FONT, 20, 'Lives ', WHITE, 640, 5)

        self.life1 = Life(715, 3) # Posicion de cada nave de vidas
        self.life2 = Life(742, 3)
        self.life3 = Life(769, 3)
        self.livesGroup = sprite.Group(self.life1, self.life2, self.life3)

    def reset(self, score): # Reinicia cada grupo (Para cuando termina o pasa de nivel)
        self.player = Ship()
        self.playerGroup = sprite.Group(self.player)
        self.explosionsGroup = sprite.Group()
        self.bullets = sprite.Group()
        self.mysteryShip = Mystery()
        self.mysteryGroup = sprite.Group(self.mysteryShip)
        self.enemyBullets = sprite.Group()
        self.make_enemies()
        self.allSprites = sprite.Group(self.player, self.enemies,
                                       self.livesGroup, self.mysteryShip)
        self.keys = key.get_pressed()

        self.timer = time.get_ticks()
        self.noteTimer = time.get_ticks()
        self.shipTimer = time.get_ticks()
        self.score = score
        self.create_audio()
        self.makeNewShip = False
        self.shipAlive = True

    def make_blockers(self, number): # Crea los bloques de defensa
        blockerGroup = sprite.Group()
        for row in range(4): # Los posiciona en diferentes lugares
            for column in range(9):
                blocker = Blocker(10, GREEN, row, column)
                blocker.rect.x = 50 + (200 * number) + (column * blocker.width)
                blocker.rect.y = BLOCKERS_POSITION + (row * blocker.height)
                blockerGroup.add(blocker)
        return blockerGroup

    def create_audio(self):  # Guarda los sonidos de cada actualización
        self.sounds = {}  # Diccionario para acceder a los sonidos fácilmente

        for SoundName in ['shoot', 'shoot2', 'invaderkilled', 'mysterykilled', 'shipexplosion']:
            self.sounds[SoundName] = mixer.Sound(SOUND_PATH + '{}.wav'.format(SoundName))
            # Si está muteado, volumen en 0; si no, en 0.2
            self.sounds[SoundName].set_volume(0.0 if MUTEADO else 0.2)

        self.musicNotes = [mixer.Sound(SOUND_PATH + '{}.wav'.format(i)) for i in range(4)]
        for Sound in self.musicNotes:
            # Si está muteado, volumen en 0; si no, en 0.5
            Sound.set_volume(0.0 if MUTEADO else 0.5)

        self.noteIndex = 0  # Índice de nota para la secuencia

    def play_main_music(self, currentTime): # Reproductor de musica
        if currentTime - self.noteTimer > self.enemies.moveTime: # Suena con el mismo intercalo que los enemigos se mueven
            self.note = self.musicNotes[self.noteIndex]
            if self.noteIndex < 3: # Si no excede el maximo de notas
                self.noteIndex += 1 # Pasa a la siguiente nota
            else: # Si lo excedio
                self.noteIndex = 0 # Se reinician las notas

            self.note.play() 
            self.noteTimer += self.enemies.moveTime # Actualiza el tiempo de ultimo tocado

    @staticmethod # Funcion estatica
    def should_exit(evt): # Evalua el evento
        return evt.type == QUIT or (evt.type == KEYUP and evt.key == K_ESCAPE)
        # Si es la accion de tocar la cruz o la tecla escape se cierra el juego

    def check_input(self): # Verifica los eventos del teclado y salida
        self.keys = key.get_pressed() # Detecta qué teclas están siendo presionadas

        for e in event.get(): # Recorre todos los eventos
            if self.should_exit(e): # Si el jugador cierra la ventana
                return True # Indica que se debe salir al menú

            # Iniciar el juego desde el menú presionando cualquier tecla
            if e.type == KEYUP and self.mainScreen:
                # Crea los bloques defensivos al iniciar
                self.allBlockers = sprite.Group(self.make_blockers(0),
                                                self.make_blockers(1),
                                                self.make_blockers(2),
                                                self.make_blockers(3))
                # Agrega las vidas a su grupo visual
                self.livesGroup.add(self.life1, self.life2, self.life3)
                self.reset(0) # Reinicia los valores del juego
                self.startGame = True # Marca que el juego ha comenzado
                self.mainScreen = False # Sale del menú

            # Detecta disparos cuando se está en el juego
            if e.type == KEYDOWN and self.startGame:
                if e.key == K_SPACE: # Si se presiona la barra espaciadora
                    if len(self.bullets) == 0 and self.shipAlive: # Solo dispara si no hay balas
                        if self.score < 1000: # Disparo normal
                            bullet = Bullet(self.player.rect.x + 23,
                                            self.player.rect.y + 5, -1,
                                            15, 'laser', 'center')
                            self.bullets.add(bullet)
                            self.allSprites.add(self.bullets)
                            self.sounds['shoot'].play()
                        else: # Disparo doble si el jugador tiene más de 1000 puntos
                            leftbullet = Bullet(self.player.rect.x + 8,
                                                self.player.rect.y + 5, -1,
                                                15, 'laser', 'left')
                            rightbullet = Bullet(self.player.rect.x + 38,
                                                self.player.rect.y + 5, -1,
                                                15, 'laser', 'right')
                            self.bullets.add(leftbullet)
                            self.bullets.add(rightbullet)
                            self.allSprites.add(self.bullets)
                            self.sounds['shoot2'].play()

        return False # No se salió, el juego continúa

    
    def make_enemies(self): # Crear los enemigos
        enemies = EnemiesGroup(10, 5, self.enemyPosition) # Se agregan los anemigos a los grupos de enemigos 
        for row in range(5):
            for column in range(10):
                enemy = Enemy(row, column)
                enemy.rect.x = 157 + (column * 50)
                enemy.rect.y = self.enemyPosition + (row * 45)
                enemies.add(enemy) # Se agrega al grupo de los enemigos existenes

        self.enemies = enemies

    def make_enemies_shoot(self): # Crea los disparos de los enemigos
        if (time.get_ticks() - self.timer) > 700 and self.enemies: # Solo si ya pasaron 700 milisegundos
            enemy = self.enemies.random_bottom()
            self.enemyBullets.add(
                Bullet(enemy.rect.x + 14, enemy.rect.y + 20, 1, 5,
                       'enemylaser', 'center')) # Se genera una bala para el enemigo elegido por el random
            self.allSprites.add(self.enemyBullets)
            self.timer = time.get_ticks() # Se guarda el tiempo de disparo

    def calculate_score(self, row): # Calcular el puntaje
        scores = {0: 30,
                  1: 20,
                  2: 20,
                  3: 10,
                  4: 10,
                  5: choice([50, 100, 150, 300])
                  } # Asigna un valor a cada fila de enemigos

        score = scores[row] # Calcula la posicion del enemigo destruido para saber cuantos puntos asignar
        self.score += score
        return score

    def create_main_menu(self): # Crea el menu principal
        """self.enemy1 = IMAGES['enemy3_1'] # Coloca un enemigo en cada posicion asignada
        self.enemy1 = transform.scale(self.enemy1, (40, 40)) # Crea la escala de la imagen
        self.enemy2 = IMAGES['enemy2_2']
        self.enemy2 = transform.scale(self.enemy2, (40, 40))
        self.enemy3 = IMAGES['enemy1_2']
        self.enemy3 = transform.scale(self.enemy3, (40, 40))
        self.enemy4 = IMAGES['mystery']
        self.enemy4 = transform.scale(self.enemy4, (80, 40))
        self.screen.blit(self.enemy1, (318, 395))
        self.screen.blit(self.enemy2, (318, 445))
        self.screen.blit(self.enemy3, (318, 495))
        self.screen.blit(self.enemy4, (299, 545))"""

    def check_collisions(self): # Checkear las coliciones de hitbox's
        # Valores True para eliminaciones y False para no eliminados al contacto
        sprite.groupcollide(self.bullets, self.enemyBullets, True, True) # Considera ambos tipos de balas 

        for enemy in sprite.groupcollide(self.enemies, self.bullets,
                                         True, True).keys(): # Considera enemigos y balas propias
            self.sounds['invaderkilled'].play() # Suena el sonido de muerte
            self.calculate_score(enemy.row) # Calcula el puntaje
            EnemyExplosion(enemy, self.explosionsGroup) # Llama a la funcion de grafico de explosiones
            self.gameTimer = time.get_ticks() # Guarda el tiempo de la muerte

        for mystery in sprite.groupcollide(self.mysteryGroup, self.bullets,
                                           True, True).keys(): # Para las naves misteriosas y balas propias
            mystery.mysteryEntered.stop() # Se detiene el sonido de la nave recorriendo el juego
            self.sounds['mysterykilled'].play() # Se inserta el sonido de la nave destruida
            score = self.calculate_score(mystery.row) # Se calcula el puntaje
            MysteryExplosion(mystery, score, self.explosionsGroup) 
            newShip = Mystery() # Se crea una nueva nave
            self.allSprites.add(newShip) # Se agrega al grupo
            self.mysteryGroup.add(newShip)

        for player in sprite.groupcollide(self.playerGroup, self.enemyBullets,
                                          True, True).keys(): # Considera balas enemigas y la nave
            if not player.invulnerable: # Solo si la nave NO es invulnerable
                if self.life3.alive(): 
                    self.life3.kill() # Elimina la tercera vida
                elif self.life2.alive():
                    self.life2.kill() # Elimina la segunda vida
                elif self.life1.alive():
                    self.life1.kill() # Elimina la primera vida
                else:
                    self.gameOver = True # Si no tiene mas vidas muestra la pantalla de perdida
                    self.startGame = False 
                self.sounds['shipexplosion'].play() # Reproduce el sonido de explosion de la nave
                ShipExplosion(player, self.explosionsGroup)
                self.makeNewShip = True # Se crean nuevas naves
                self.shipTimer = time.get_ticks() # Se guarda el tiempo de la muerte
                self.shipAlive = False # Se avisa que no existe mas

        if self.enemies.bottom >= 540: # Si los enemigos decendieron demasiado
            sprite.groupcollide(self.enemies, self.playerGroup, True, True) # Si el enemigo toca a la nave
            if not self.player.alive() or self.enemies.bottom >= GAME_HEIGTH: # Si llegan al final
                self.gameOver = True # Se peirde
                self.startGame = False

        sprite.groupcollide(self.bullets, self.allBlockers, True, True) # Considera balas aliadas y los bloques
        sprite.groupcollide(self.enemyBullets, self.allBlockers, True, True) # Considera balas enemigas y los bloques
        if self.enemies.bottom >= BLOCKERS_POSITION: # Si los enemigos se encuentran en la misma posicion que los bloques
            sprite.groupcollide(self.enemies, self.allBlockers, False, True) # Considera a los enemigos y los bloques

    def create_new_ship(self, createShip, currentTime):
        if createShip and (currentTime - self.shipTimer > 900): # Si se esta creando una nave nueva y pasaron 900 milisegundos desde la destruccion de la anterior
            self.player = Ship() # Nueva nave
            self.allSprites.add(self.player) # Se agrega al grupo
            self.playerGroup.add(self.player)
            self.makeNewShip = False # Se deja de querer crear naves
            self.shipAlive = True # Se activa la nave

    def create_game_over(self, currentTime): # Instancia de perdida
        self.screen.blit(self.background, (0, 0)) 
        passed = currentTime - self.timer
        if passed < 750: # Si pasaron 750 milisegundos
            self.gameOverText.draw(self.screen) # Se carga el texto de "Game Over" en bucle
        elif 750 < passed < 1500:
            self.screen.blit(self.background, (0, 0))
        elif 1500 < passed < 2250:
            self.gameOverText.draw(self.screen)
        elif 2250 < passed < 2750:
            self.screen.blit(self.background, (0, 0))
        elif passed > 3000:
            self.mainScreen = True # Luego de los 3 segundo se activa el menu de inicio

        for e in event.get(): # Dentro de los eventos
            if self.should_exit(e): # Si en de salida
                sys.exit() # Salir del progama

    def main(self): # Definiendo el bucle principal del juego
        self.screen = display.set_mode((GAME_WIDTH, GAME_HEIGTH)) # Define el tamaño de la pantalla

        while True:
            salir = self.check_input() # Verifica si se debe salir (al menú)
            if salir:
                return 'menu'
            
            if self.mainScreen: # Si se encuentra en la pantalla del menú principal
                self.screen.blit(self.background, (0, 0)) # Se grafica el fondo
                self.screen.blit(self.menu, (0, 0)) # Se grafica el fondo
                # self.screen.blit(self.titleText, (0, 0)) # Se dibuja el título
                self.titleText2.draw(self.screen) # Se dibuja el subtítulo
                """self.enemy1Text.draw(self.screen) # Imagen del primer enemigo
                self.enemy2Text.draw(self.screen) # Imagen del segundo enemigo
                self.enemy3Text.draw(self.screen) # Imagen del tercer enemigo
                self.enemy4Text.draw(self.screen) # Imagen del enemigo especial"""
                self.create_main_menu() # Dibuja los textos con puntajes

            elif self.startGame: # Si el juego ya ha comenzado
                currentTime = time.get_ticks() # Guarda el tiempo actual
                self.screen.blit(self.background, (0, 0)) # Se grafica el fondo

                if not self.enemies and not self.explosionsGroup: # Si no hay enemigos ni explosiones
                    if currentTime - self.gameTimer < 3000: # Si pasaron menos de 3 segundos
                        self.screen.blit(self.background, (0, 0)) # Fondo del juego
                        self.scoreText2 = Text(FONT, 20, str(self.score), GREEN, 85, 5) # Puntaje actualizado
                        self.scoreText.draw(self.screen)
                        self.scoreText2.draw(self.screen)
                        self.nextRoundText.draw(self.screen) # Mensaje "Siguiente ronda"
                        self.livesText.draw(self.screen) # Vidas
                        self.livesGroup.update() # Dibuja las vidas
                    elif currentTime - self.gameTimer > 3000: # Si pasaron más de 3 segundos
                        self.enemyPosition += ENEMY_MOVE_DOWN # Baja los enemigos
                        self.reset(self.score) # Resetea la ronda manteniendo el puntaje
                        self.gameTimer += 3000 # Actualiza el temporizador
                    self.allSprites.update(self.keys, currentTime, self.screen) # Actualiza los sprites

                else: # Si hay enemigos y el juego continúa
                    self.play_main_music(currentTime) # Ejecuta la música del juego
                    self.screen.blit(self.background, (0, 0)) # Fondo
                    self.allBlockers.update(self.screen) # Dibuja los bloques defensivos
                    self.scoreText2 = Text(FONT, 20, str(self.score), GREEN, 85, 5) # Puntaje
                    self.scoreText.draw(self.screen)
                    self.scoreText2.draw(self.screen)
                    self.livesText.draw(self.screen)
                    self.enemies.update(currentTime) # Mueve enemigos
                    self.allSprites.update(self.keys, currentTime, self.screen) # Mueve jugador, balas, etc.
                    self.explosionsGroup.update(currentTime) # Actualiza explosiones
                    self.check_collisions() # Verifica colisiones entre elementos
                    self.create_new_ship(self.makeNewShip, currentTime) # Crea nave nueva si fue destruida
                    self.make_enemies_shoot() # Los enemigos disparan

            elif self.gameOver: # Si el juego terminó
                currentTime = time.get_ticks()
                self.enemyPosition = ENEMY_DEFAULT_POSITION # Reinicia la posición de enemigos
                self.create_game_over(currentTime) # Muestra pantalla de Game Over

            display.update() # Actualiza la pantalla
            self.clock.tick(60) # Limita la velocidad de fotogramas a 60 FPS

if __name__ == "__main__":
    game = SpaceInvaders()
    game.main()