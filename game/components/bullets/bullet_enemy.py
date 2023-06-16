import random
import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET_ENEMY

class BulletEnemy(Bullet):
    WIDTH = 9
    HEIGHT = 20
    SPEED = [10,13,15,17,20]

    def __init__(self, center):
        self.image = BULLET_ENEMY
        self.image = pygame.transform.scale(self.image, (self.WIDTH,self.HEIGHT))
        super().__init__(self.image,center)

    def update(self,player,enemy_handler):
        self.rect.y += random.choice(self.SPEED)
        if self.rect.colliderect(player.rect):
            player.is_alive = False
