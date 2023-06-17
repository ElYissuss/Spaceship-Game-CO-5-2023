from game.utils.constants import BULLET_ENEMY_TYPE, BULLET_SHIP_TYPE
from game.components.bullets.bullet_enemy import BulletEnemy
from game.components.bullets.bullet_ship import BulletShip

class BulletHandler:
    def __init__(self):
        self.bullets = []

    def update(self, player, enemy_handler, bullet_handler):
        for bullet in self.bullets:
            bullet.update(player, enemy_handler, bullet_handler, bullet)

    def draw(self,screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, type, center):
        if type == BULLET_ENEMY_TYPE:
            self.bullets.append(BulletEnemy(center))
        elif type == BULLET_SHIP_TYPE:
            self.bullets.append(BulletShip(center))

    def reset(self):
        self.bullets = []