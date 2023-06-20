import pygame

from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2

class Navy(Enemy):
    Y_POS = 20
    SPEED_X = 4
    SPEED_Y = 0
    INTERVAL = [1060]
    LIFE = 20

    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image,(self.WIDHT,self.HEIGHT))
        super().__init__(self.image)