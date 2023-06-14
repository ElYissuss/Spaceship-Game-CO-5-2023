import pygame

from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_3

class Aircraft(Enemy):
    SPEED_X = 2
    SPEED_Y = 5
    INTERVAL = [50,100,200]

    def __init__(self):
        self.image = ENEMY_3
        self.image = pygame.transform.scale(self.image,(self.WIDHT,self.HEIGHT))
        super().__init__(self.image)