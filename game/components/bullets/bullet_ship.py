import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET

class BulletShip(Bullet):
    WIDTH = 9
    HEIGHT = 32
    SPEED = 25

    def __init__(self, center):
        self.image = BULLET
        self.image = pygame.transform.scale(self.image, (self.WIDTH,self.HEIGHT))
        super().__init__(self.image,center)

    def update(self, player,enemy_handler):
        self.rect.y -= self.SPEED
        for i in range(0,len(enemy_handler.enemies)):
            if self.rect.colliderect(enemy_handler.enemies[i].rect):
                enemy_handler.enemies[i].is_alive = False
                enemy_handler.number_enemy_destroyed += 1
