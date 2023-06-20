import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET, BULLET_SHIP_DAMAGE

class BulletShip(Bullet):
    WIDTH = 9
    HEIGHT = 32
    SPEED = 25

    def __init__(self, center):
        self.image = BULLET
        self.image = pygame.transform.scale(self.image, (self.WIDTH,self.HEIGHT))
        super().__init__(self.image,center)

    def update(self, player, enemy_handler, bullet_handler, bullet):
        self.rect.y -= self.SPEED
        for i in range(0,len(enemy_handler.enemies)):
            if self.rect.colliderect(enemy_handler.enemies[i].rect):
                enemy_handler.enemies[i].LIFE -= player.damage
                try:
                    bullet_handler.bullets.remove(bullet)
                except:
                    pass
                if enemy_handler.enemies[i].LIFE <= 0:
                    enemy_handler.enemies[i].is_alive = False
                    enemy_handler.number_enemy_destroyed += 1
