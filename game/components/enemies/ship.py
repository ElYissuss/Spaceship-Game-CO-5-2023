import pygame

from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1

class Ship(Enemy):
    SPEED_X = 5
    SPEED_Y = 5
    INTERVAL = [25,50,75,100,125,150,175,200]
    LIFE = 10

    def __init__(self):
        self.image = ENEMY_1
        self.image = pygame.transform.scale(self.image,(self.WIDHT,self.HEIGHT))
        super().__init__(self.image)