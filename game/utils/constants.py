import pygame
import os

pygame.mixer.init()

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 120
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
DAMAGE = pygame.image.load(os.path.join(IMG_DIR, 'Other/damage.png'))
LIFE = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
DAMAGE_TYPE = 'damage'
LIFE_TYPE = 'life'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
BULLET_BOSS = pygame.image.load(os.path.join(IMG_DIR, "Bullet/boss_bullet.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_3.png"))
BOSS = pygame.image.load(os.path.join(IMG_DIR, "Enemy/boss.png"))

LIFE_AUDIO = pygame.mixer.Sound('C:\\Users\\Yissus\\Documents\\GitHub\\Spaceship-Game-CO-5-2023\\game\\assets\\Sound\\Powers\\lifesound.mpeg')
DAMAGE_AUDIO = pygame.mixer.Sound('C:\\Users\\Yissus\\Documents\\GitHub\\Spaceship-Game-CO-5-2023\\game\\assets\\Sound\\Powers\\damagesound.mpeg')
SHIELD_AUDIO = pygame.mixer.Sound('C:\\Users\\Yissus\\Documents\\GitHub\\Spaceship-Game-CO-5-2023\\game\\assets\\Sound\\Powers\\shieldsound.mpeg')
PLAYING_AUDIO = pygame.mixer.Sound('C:\\Users\\Yissus\\Documents\\GitHub\\Spaceship-Game-CO-5-2023\\game\\assets\\Sound\\Background\\playing.mp3')
MENU_AUDIO = pygame.mixer.Sound('C:\\Users\\Yissus\\Documents\\GitHub\\Spaceship-Game-CO-5-2023\\game\\assets\\Sound\\Background\\menu.mp3')
MENU2_AUDIO =  pygame.mixer.Sound('C:\\Users\\Yissus\\Documents\\GitHub\\Spaceship-Game-CO-5-2023\\game\\assets\\Sound\\Background\\menu_2.mp3')
SHOOT_AUDIO =  pygame.mixer.Sound('C:\\Users\\Yissus\\Documents\\GitHub\\Spaceship-Game-CO-5-2023\\game\\assets\\Sound\\Powers\\shootaudio.mpeg')
DAMAGE_AUDIO =  pygame.mixer.Sound('C:\\Users\\Yissus\\Documents\\GitHub\\Spaceship-Game-CO-5-2023\\game\\assets\\Sound\\Powers\\damageaudio.mpeg')
LOSE_AUDIO =  pygame.mixer.Sound('C:\\Users\\Yissus\\Documents\\GitHub\\Spaceship-Game-CO-5-2023\\game\\assets\\Sound\\Powers\\loseaudio.mpeg')


FONT_STYLE = 'freesansbold.ttf'

BLACK_COLOR = (0,0,0)
WHITE_COLOR = (255,255,255)

BULLET_ENEMY_TYPE = "enemy"
BULLET_SHIP_TYPE = "ship"
BULLET_BOSS_TYPE = "boss"

BULLET_SHIP_DAMAGE = 10

CHANNEL_1 = pygame.mixer.Channel(0)
CHANNEL_2 = pygame.mixer.Channel(1)
CHANNEL_3 = pygame.mixer.Channel(2)
CHANNEL_4 = pygame.mixer.Channel(3)
CHANNEL_5 = pygame.mixer.Channel(4)
CHANNEL_6 = pygame.mixer.Channel(5)
