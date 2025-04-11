from pygame import *
import sys
from os.path import abspath, dirname
from random import choice

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
SCREEN = display.set_mode((1000, 800))
FONT = FONT_PATH + 'space_invaders.ttf'
IMG_NAMES = ['ship', 'mystery',
             'enemy1_1', 'enemy1_2',
             'enemy2_1', 'enemy2_2',
             'enemy3_1', 'enemy3_2',
             'explosionblue', 'explosiongreen', 'explosionpurple',
             'laser', 'enemylaser']
IMAGES = {name: image.load(IMAGE_PATH + '{}.png'.format(name)).convert_alpha()
          for name in IMG_NAMES} # Cargado Automatico de Imagenes en un diccionario

BLOCKERS_POSITION = 550
ENEMY_DEFAULT_POSITION = 65 
ENEMY_MOVE_DOWN = 35


class Ship(sprite.Sprite): # Hereda la clase Sprite de Pygame (Util para objetos con hitbox)
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = IMAGES['ship']
        self.rect = self.image.get_rect(topleft=(485, 735)) # Asigna la hitbox y la posicion inicial de la nave
        self.invulnerable = True # Nueva nave es invulnerable al principio
        self.tiempoDeCreacion = time.get_ticks() # Tiempo de creación
        self.speed = 5

    def update(self, keys, currentTime, *args): # Para reescribir la posicion del objeto (Keys - Teclas, *Args - Agrupar argumentos)
        if self.invulnerable and (currentTime - self.tiempoDeCreacion > 1000):
            self.invulnerable = False
        if keys[K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed # Si se presiona la flecha izquierda y no esta en el borde se mueve hacia allí
        if keys[K_RIGHT] and self.rect.x < 740:
            self.rect.x += self.speed # Si se presiona la flecha derecha y no esta en el borde se mueve hacia allí
        game.screen.blit(self.image, self.rect) # Dibuja el objeto

class Bullet(sprite.Sprite): # Definiendo las balas
    def __init__(self, xpos, ypos, direction, speed, filename, side):
        sprite.Sprite.__init__(self)
        self.image = IMAGES[filename]
        self.rect = self.image.get_rect(topleft=(xpos, ypos)) # Cargar la imagen
        self.speed = speed
        self.direction = direction
        self.side = side # Tirador
        self.filename = filename # Nombre de la imagen

    def update(self, keys, *args): # Para reescribir la posicion del objeto (Keys - Teclas, *Args - Agrupar argumentos)
        game.screen.blit(self.image, self.rect)
        self.rect.y += self.speed * self.direction
        if self.rect.y < 20 or self.rect.y > 987:
            self.kill() # Eliminar la bala en caso que exceda los limites

class Enemy(sprite.Sprite): # Definiendo a los enemigos
    def __init__(self, row, column): # Para ubicar al enemigo dentro de una matriz de posiciones
        sprite.Sprite.__init__(self)
        self.row = row
        self.column = column
        self.images = [] # Una lista con las dos imagenes para alternar en la animacion
        self.load_images()
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect() # Crea la hitbox

    def toggle_image(self):
        self.index += 1 # Agraga una imagen
        if self.index >= len(self.images): # Si la cantidad de imagenes es igual o mayor a la cantidad de imagenes animables (2)
            self.index = 0 # Empezar con las imagenes de vuelta
        self.image = self.images[self.index]

    def update(self, *args):
        game.screen.blit(self.image, self.rect) # Solo lo dibuja

    def load_images(self): 
        images = {0: ['1_2', '1_1'],
                  1: ['2_2', '2_1'],
                  2: ['2_2', '2_1'],
                  3: ['3_1', '3_2'],
                  4: ['3_1', '3_2'],
                  } # Asigna un tipo de enemigo a cada fila
        img1, img2 = (IMAGES['enemy{}'.format(img_num)] for img_num in
                      images[self.row]) # Generador de imagenes
        self.images.append(transform.scale(img1, (40, 35)))
        self.images.append(transform.scale(img2, (40, 35))) # Asigna un tamaño a la imagen y la guarda dentro de la lista

class EnemiesGroup(sprite.Group): # Extiende la clase Enemies para trabajar en conjunto con cada uno de ellos
    def __init__(self, columns, rows):
        sprite.Group.__init__(self)
        self.enemies = [[None] * columns for _ in range(rows)] # Crea una matriz vacia para la formacion de enemigos
        self.columns = columns
        self.rows = rows
        self.leftAddMove = 0 # Agregan movimientos si los enemigos se mueren cerca del lado del limite
        self.rightAddMove = 0
        self.moveTime = 600 # Cuantos milisegundo tarda en moverse el grupo
        self.direction = 1 # 1 = Derecha - -1 = Izquierda
        self.rightMoves = 28 
        self.leftMoves = 28 # Cantidad de paso para poder bajar a la siguiente columna
        self.moveNumber = 12
        self.timer = time.get_ticks() # Ultimo momento en el que se movieron
        self.bottom = game.enemyPosition + ((rows - 1) * 45) + 35 # Bottom = la ilera de abajo
        self._aliveColumns = list(range(columns))
        self._leftAliveColumn = 0
        self._rightAliveColumn = columns - 1

    def update(self, current_time): # Actualizar al grupo
        if current_time - self.timer > self.moveTime:
            velocidad = 10 if self.direction == 1 else -10
            anchoPantalla = 1000  # Ancho de tu pantalla
            margen = 15  # Margen para que no lleguen pegados al borde

            # Verificar si algún enemigo se pasa del borde
            seVaAPasar = any(
                (enemy.rect.right + velocidad >= anchoPantalla - margen and self.direction == 1) or
                (enemy.rect.left + velocidad < margen and self.direction == -1)
                for enemy in self
            )

            if seVaAPasar: # Si alguno se pasa, cambiar dirección y bajar
                self.direction *= -1
                self.moveNumber = 0
                self.leftMoves = 30 + self.rightAddMove
                self.rightMoves = 30 + self.leftAddMove
                self.bottom = 0
                for enemy in self:
                    enemy.rect.y += ENEMY_MOVE_DOWN
                    enemy.toggle_image()
                    if self.bottom < enemy.rect.y + 35:
                        self.bottom = enemy.rect.y + 35
            else: # Si no se pasa, seguir moviéndose
                for enemy in self:
                    enemy.rect.x += velocidad
                    enemy.toggle_image()
                self.moveNumber += 1

            self.timer += self.moveTime
            
    def add_internal(self, *sprites): # Agrega el sprite a la matriz de enemigos
        super(EnemiesGroup, self).add_internal(*sprites)
        for s in sprites:
            self.enemies[s.row][s.column] = s

    def remove_internal(self, *sprites): # Elimina de la matriz a los muertos y actualiza la velocidad
        super(EnemiesGroup, self).remove_internal(*sprites)
        for s in sprites:
            self.kill(s)
        self.update_speed()

    def is_column_dead(self, column):
        return not any(self.enemies[row][column]
                       for row in range(self.rows))

    def random_bottom(self):
        col = choice(self._aliveColumns) # Elige una de las columnas vivas al azar
        col_enemies = (self.enemies[row - 1][col] # De vuelve el enemigo de mas abajo para poder disparar
                       for row in range(self.rows, 0, -1))
        return next((en for en in col_enemies if en is not None), None)

    def update_speed(self):
        if len(self) == 1:
            self.moveTime = 200 # Si solo queda un enemigo triplica la velocidad
        elif len(self) <= 10:
            self.moveTime = 400 # Si quedan entre 10 y 2 enemigos duplica la velocidad

    def kill(self, enemy):
        self.enemies[enemy.row][enemy.column] = None # Elemina al enemigo de la matriz
        is_column_dead = self.is_column_dead(enemy.column) 
        if is_column_dead: # Verifica 
            self._aliveColumns.remove(enemy.column) # Lo elimina de la lista de los vivos

        if enemy.column == self._rightAliveColumn: # Si era el borde
            while self._rightAliveColumn > 0 and is_column_dead:
                self._rightAliveColumn -= 1 # Reduce el borde
                self.rightAddMove += 5 # Agrega movimientos en esa direccion
                is_column_dead = self.is_column_dead(self._rightAliveColumn)

        elif enemy.column == self._leftAliveColumn: # Lo mismo pero con el lado izquierdo
            while self._leftAliveColumn < self.columns and is_column_dead:
                self._leftAliveColumn += 1
                self.leftAddMove += 5
                is_column_dead = self.is_column_dead(self._leftAliveColumn)

class Blocker(sprite.Sprite): # Definir los bloques de proteccion
    def __init__(self, size, color, row, column):
        sprite.Sprite.__init__(self)
        self.height = size # Alto
        self.width = size # Ancho
        self.color = color
        self.image = Surface((self.width, self.height)) # Se crea un rectangulo
        self.image.fill(self.color) # Se le coloca el color
        self.rect = self.image.get_rect() # Para manejar las coliciones
        self.row = row
        self.column = column

    def update(self, keys, *args):
        game.screen.blit(self.image, self.rect) # Dibujar el objeto

class Mystery(sprite.Sprite): # Nave misteriosa
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = IMAGES['mystery']
        self.image = transform.scale(self.image, (75, 35))
        self.rect = self.image.get_rect(topleft=(-80, 45)) # Posicion incial (Fuera de la pantalla)
        self.row = 5
        self.moveTime = 25000 # Aparace cada 25 segundos
        self.direction = 1 
        self.timer = time.get_ticks()
        self.mysteryEntered = mixer.Sound(SOUND_PATH + 'mysteryentered.wav')
        self.mysteryEntered.set_volume(0.3)
        self.playSound = True # Controla si el sonido debe reproducirse nuevamente

    def update(self, keys, currentTime, *args):
        resetTimer = False
        passed = currentTime - self.timer
        if passed > self.moveTime: # Solo si pasarons 25 segundos
            if (self.rect.x < 0 or self.rect.x > 800) and self.playSound:
                self.mysteryEntered.play() # Reproduce el sonido de la nave
                self.playSound = False # apaga el sonido de la nave
            if self.rect.x < 840 and self.direction == 1:
                self.mysteryEntered.fadeout(4000) # Reduce suavemente el sonido
                self.rect.x += 2
                game.screen.blit(self.image, self.rect) # Lo mueve para la derecha
            if self.rect.x > -100 and self.direction == -1:
                self.mysteryEntered.fadeout(4000) # Reduce suavemente el sonido
                self.rect.x -= 2
                game.screen.blit(self.image, self.rect) # Lo mueve para la izquierda

        if self.rect.x > 830: # Si salio por la derecha
            self.playSound = True
            self.direction = -1 # Setea el movimiento para la izquierda
            resetTimer = True 
        if self.rect.x < -90: # Si salio por la izquierda
            self.playSound = True
            self.direction = 1 # Setea el movimiento para la derecha
            resetTimer = True
        if passed > self.moveTime and resetTimer:
            self.timer = currentTime # Resetea el reloj de 25 segundos

class EnemyExplosion(sprite.Sprite): # Definir la explosion de los enemigos tras su muerte
    def __init__(self, enemy, *groups):
        super(EnemyExplosion, self).__init__(*groups)
        self.image = transform.scale(self.get_image(enemy.row), (40, 35)) # Asigna un tamaño de imagen inicial
        self.image2 = transform.scale(self.get_image(enemy.row), (50, 45)) # Asigna un tamaño a la imagen mas grande
        self.rect = self.image.get_rect(topleft=(enemy.rect.x, enemy.rect.y)) # La coloca en la posicion del enemigo
        self.timer = time.get_ticks() # Guarda el momento de la explosion

    @staticmethod
    def get_image(row):
        img_colors = ['purple', 'blue', 'blue', 'green', 'green']
        return IMAGES['explosion{}'.format(img_colors[row])] # Generador de imagenes

    def update(self, current_time, *args):
        passed = current_time - self.timer
        if passed <= 100:
            game.screen.blit(self.image, self.rect) # Dibuja una imagen luego de 100 milisegundos
        elif passed <= 200:
            game.screen.blit(self.image2, (self.rect.x - 6, self.rect.y - 6)) # Dibuja la segunda luego de 200 milisegundos
        elif 400 < passed:
            self.kill() # Luego de 400 milisegundo las elimina

class MysteryExplosion(sprite.Sprite): # Explosion de la nave misteriosa
    def __init__(self, mystery, score, *groups):
        super(MysteryExplosion, self).__init__(*groups)
        self.text = Text(FONT, 20, str(score), WHITE, # Define un tipo de texto en la fuente, 20 de grande y color blanco
                         mystery.rect.x + 20, mystery.rect.y + 6)
        self.timer = time.get_ticks() # Guarda el tiempo de la explosion

    def update(self, current_time, *args):
        passed = current_time - self.timer
        if passed <= 200 or 400 < passed <= 600:
            self.text.draw(game.screen) # Muestra el texto en 2 intervalos; 0 - 200 , 400 - 600 milesegundos
        elif 600 < passed:
            self.kill() # Luego de 600 milisegundo elimina el texto

class ShipExplosion(sprite.Sprite): # Explosion de la nave propia
    def __init__(self, ship, *groups):
        super(ShipExplosion, self).__init__(*groups)
        self.image = IMAGES['ship']
        self.rect = self.image.get_rect(topleft=(ship.rect.x, ship.rect.y))
        self.timer = time.get_ticks() # Guarda el tiempo de la explosion

    def update(self, current_time, *args):
        passed = current_time - self.timer
        if 300 < passed <= 600:
            game.screen.blit(self.image, self.rect) # Durante 300 milisegundo dibuja de nuevo la nave
        elif 900 < passed:
            self.kill() # Luego de 900 milisegundo la elimina

class Life(sprite.Sprite): 
    def __init__(self, xpos, ypos):
        sprite.Sprite.__init__(self)
        self.image = IMAGES['ship']
        self.image = transform.scale(self.image, (23, 23)) # Carga la imagen pero la dimensiona mas pequeña
        self.rect = self.image.get_rect(topleft=(xpos, ypos)) # Define la posicion inicial en pantalla

    def update(self, *args):
        game.screen.blit(self.image, self.rect) # Dibuja la imagen cada vez que se actualiza el juego

class Text(object):
    def __init__(self, textFont, size, message, color, xpos, ypos):
        self.font = font.Font(textFont, size)
        self.surface = self.font.render(message, True, color)
        self.rect = self.surface.get_rect(topleft=(xpos, ypos))

    def draw(self, surface):
        surface.blit(self.surface, self.rect) # Dibuja el texto sobre la superficie

class SpaceInvaders(object): # Codigo del Juego
    def __init__(self):
        mixer.pre_init(44100, -16, 1, 4096) # Es recomendado para las persona que usan Linux
        init()
        self.clock = time.Clock() # Timer
        self.caption = display.set_caption('Space Invaders') # Titulo
        self.screen = SCREEN # Pantalla
        self.background = image.load(IMAGE_PATH + 'background.jpg').convert() # Cargar fondo
        self.background = transform.scale(self.background, (1000, 800))
        self.startGame = False # Iniciar el juego
        self.mainScreen = True # El menu principal
        self.gameOver = False # Controla si el juego termino
        self.enemyPosition = ENEMY_DEFAULT_POSITION # Llama a la funcion para poder colocar a los enemigos
        self.titleText = Text(FONT, 50, 'Space Invaders', WHITE, 274, 205)  # Centrado más arriba
        self.titleText2 = Text(FONT, 25, 'Press any key to continue', WHITE, 300, 285)
        self.gameOverText = Text(FONT, 50, 'Game Over', WHITE, 375, 360)  # Centrado
        self.nextRoundText = Text(FONT, 50, 'Next Round', WHITE, 365, 360)
        self.enemy1Text = Text(FONT, 25, '   =   10 pts', GREEN, 468, 370)
        self.enemy2Text = Text(FONT, 25, '   =  20 pts', BLUE, 468, 420)
        self.enemy3Text = Text(FONT, 25, '   =  30 pts', PURPLE, 468, 470)
        self.enemy4Text = Text(FONT, 25, '   =  ?????', RED, 468, 520)
        self.scoreText = Text(FONT, 20, 'Score', WHITE, 5, 5)
        self.livesText = Text(FONT, 20, 'Lives ', WHITE, 820, 5)  # Ajustado para pantalla de 1000px

        self.life1 = Life(894, 3)  # Posiciones ajustadas
        self.life2 = Life(928, 3)
        self.life3 = Life(961, 3)
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
        for row in range(4): # Cada bloque tendra 4 * 9 secciones
            for column in range(9):
                blocker = Blocker(10, RED, row, column)
                blocker.rect.x = 50 + (200 * number) + (column * blocker.width)
                blocker.rect.y = BLOCKERS_POSITION + (row * blocker.height)
                blockerGroup.add(blocker)
        return blockerGroup

    def create_audio(self): # Guarda los sonidos de cada actualizacion
        self.sounds = {} # Crea un diccionario para acceder de forma mas facil a los sonidos
        for sound_name in ['shoot', 'shoot2', 'invaderkilled', 'mysterykilled',
                           'shipexplosion']: # La lista de los sonidos
            self.sounds[sound_name] = mixer.Sound( # Funcion de Pygame para encontrar el archivo
                SOUND_PATH + '{}.wav'.format(sound_name)) # Construlle el nombre completo del sonido
            self.sounds[sound_name].set_volume(0.2) # Setear volumen

        self.musicNotes = [mixer.Sound(SOUND_PATH + '{}.wav'.format(i)) for i
                           in range(4)] # Crea un lista con los sonido 0,1,2 y 3.wav
        for sound in self.musicNotes:
            sound.set_volume(0.5)

        self.noteIndex = 0 # Se crea un indice para las notas

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

    def check_input(self): # Checkiar los valores de entrada
        self.keys = key.get_pressed() # Evalua la presion de una tecla para las otras funciones
        for e in event.get(): # Recorre todo lo que ocurrio en el ultimo ciclo
            if self.should_exit(e):
                sys.exit() # Si el evento es el QUIT se cierra el juego
            if e.type == KEYDOWN: # Si una tecla es presionada
                if e.key == K_SPACE: # Si es el espacio
                    if len(self.bullets) == 0 and self.shipAlive: # Solo si no hay balas en el grupo
                        if self.score < 1000: # Si tiene menos de 1000 puntos 
                            bullet = Bullet(self.player.rect.x + 23,
                                            self.player.rect.y + 5, -1,
                                            15, 'laser', 'center') # Se le da un valor una bala
                            self.bullets.add(bullet) # Se agrega a la lista de las balas
                            self.allSprites.add(self.bullets) # Que sea actualizada y dibujada
                            self.sounds['shoot'].play() # Se reproduce el sonido del disparo
                        else: # Si tiene mas de 1000 puntos se activa el modo avnazado
                            leftbullet = Bullet(self.player.rect.x + 8,
                                                self.player.rect.y + 5, -1,
                                                15, 'laser', 'left')
                            rightbullet = Bullet(self.player.rect.x + 38,
                                                 self.player.rect.y + 5, -1,
                                                 15, 'laser', 'right') # Dipara dos lasers, uno de cada lado 
                            self.bullets.add(leftbullet) # Se agraga el disparo izquierdo a su lista
                            self.bullets.add(rightbullet) # Se agrega el disparo derecho a su lista
                            self.allSprites.add(self.bullets)
                            self.sounds['shoot2'].play() # Se reproduce otro sonido

    def make_enemies(self): # Crear los enemigos
        enemies = EnemiesGroup(15, 5) # Se agregan los anemigos a los grupos de enemigos 
        for row in range(5):
            for column in range(15):
                enemy = Enemy(row, column)
                enemy.rect.x = 120 + (column * 50)
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
        self.enemy1 = IMAGES['enemy3_1'] # Coloca un enemigo en cada posicion asignada
        self.enemy1 = transform.scale(self.enemy1, (40, 40)) # Crea la escala de la imagen
        self.enemy2 = IMAGES['enemy2_2']
        self.enemy2 = transform.scale(self.enemy2, (40, 40))
        self.enemy3 = IMAGES['enemy1_2']
        self.enemy3 = transform.scale(self.enemy3, (40, 40))
        self.enemy4 = IMAGES['mystery']
        self.enemy4 = transform.scale(self.enemy4, (80, 40))
        self.screen.blit(self.enemy1, (418, 370))
        self.screen.blit(self.enemy2, (418, 420))
        self.screen.blit(self.enemy3, (418, 470))
        self.screen.blit(self.enemy4, (399, 520))

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

        if self.enemies.bottom >= 718: # Si los enemigos decendieron demasiado
            sprite.groupcollide(self.enemies, self.playerGroup, True, True) # Si el enemigo toca a la nave
            if not self.player.alive() or self.enemies.bottom >= 800: # Si llegan al final
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

    def main2(self): # Definiendo el menu
        while True:
            if self.mainScreen: # Si se encuentra en la pantalla del menu
                self.screen.blit(self.background, (0, 0)) # Se carga el fondo
                self.titleText.draw(self.screen) # Se carga el titulo
                self.titleText2.draw(self.screen) # Se carga el segundo texto
                self.enemy1Text.draw(self.screen) # Se carga la imagen del primer enemigo
                self.enemy2Text.draw(self.screen) # Se carga la imagen del segundo enemigo
                self.enemy3Text.draw(self.screen) # Se carga la imagen del tercer enemigo
                self.enemy4Text.draw(self.screen) # Se carga la imagen de la nave especial
                self.create_main_menu()
                for e in event.get(): # Dentro de los eventos
                    if self.should_exit(e): # Si es de QUIT
                        sys.exit() # Sale automaticamente
                    if e.type == KEYUP: # Si es de dejar de presionar una tecla 
                        # Solo crea bloques en una nueva partida, no una nueva ronda
                        self.allBlockers = sprite.Group(self.make_blockers(0), 
                                                        self.make_blockers(1),
                                                        self.make_blockers(2),
                                                        self.make_blockers(3),
                                                        self.make_blockers(4)) # Crea los 5 bloques
                        self.livesGroup.add(self.life1, self.life2, self.life3) # Se añaden las vidas del jugador
                        self.reset(0) # Se resetea el estado del juego
                        self.startGame = True
                        self.mainScreen = False # Sale del menu

            elif self.startGame: # Cuando se ejecuta el juego
                if not self.enemies and not self.explosionsGroup: # Si no hay enemigos ni coliciones
                    currentTime = time.get_ticks() # Se guarda el tiempo
                    if currentTime - self.gameTimer < 3000: # Durante los 3 segundos
                        self.screen.blit(self.background, (0, 0)) # Muestra fondo
                        self.scoreText2 = Text(FONT, 20, str(self.score), 
                                               GREEN, 85, 5) # Textos
                        self.scoreText.draw(self.screen)
                        self.scoreText2.draw(self.screen)
                        self.nextRoundText.draw(self.screen)
                        self.livesText.draw(self.screen)
                        self.livesGroup.update()
                        self.check_input()
                    if currentTime - self.gameTimer > 3000: # Luego de los 3 segundos
                        self.enemyPosition += ENEMY_MOVE_DOWN # Se posicionan los enemigos mas abajo
                        self.reset(self.score) 
                        self.gameTimer += 3000
                    self.allSprites.update(self.keys, currentTime,)
                else: # Si no, se ejecuta el juego normalmente
                    currentTime = time.get_ticks() # Se guarda el tiempo
                    self.play_main_music(currentTime) # Se ejecuta el sonido
                    self.screen.blit(self.background, (0, 0)) # Se grafica le fondo
                    self.allBlockers.update(self.screen) # Se actualizan los bloques
                    self.scoreText2 = Text(FONT, 20, str(self.score), GREEN,
                                           85, 5) # Se fibujan los textos
                    self.scoreText.draw(self.screen)
                    self.scoreText2.draw(self.screen)
                    self.livesText.draw(self.screen)
                    self.check_input() # Se recive el imput del jugador
                    self.enemies.update(currentTime) # Se actualiza a los jugadores
                    self.allSprites.update(self.keys, currentTime)
                    self.explosionsGroup.update(currentTime) # Se actualizan las explosiones
                    self.check_collisions() # Se actializan las coliciones
                    self.create_new_ship(self.makeNewShip, currentTime)
                    self.make_enemies_shoot() # Los enemigos comienzan a disparar

            elif self.gameOver: # Si se perdio
                currentTime = time.get_ticks() # Se guarda el tiempo
                # Resetea enemigos a posicion incial
                self.enemyPosition = ENEMY_DEFAULT_POSITION
                self.create_game_over(currentTime) # Se llama a la funcion de perdida

            display.update() # Se actualiza la pantalla
            self.clock.tick(60) # Se limita el sistema a 60 FPS

game = SpaceInvaders()
game.main2()