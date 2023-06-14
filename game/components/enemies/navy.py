import pygame

from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_2

class Navy(Enemy):
    SPEED_X = 5
    SPEED_Y = 2
    INTERVAL = [50,100,150,200,250]

    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image,(self.WIDHT,self.HEIGHT))
        super().__init__(self.image)