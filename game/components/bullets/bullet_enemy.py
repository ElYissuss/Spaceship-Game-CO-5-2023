import random
import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET_ENEMY, SHIELD_TYPE, DAMAGE_AUDIO, CHANNEL_5

class BulletEnemy(Bullet):
    WIDTH = 9
    HEIGHT = 20
    SPEED = [10,13,15,17,20]

    def __init__(self, center):
        self.image = BULLET_ENEMY
        self.image = pygame.transform.scale(self.image, (self.WIDTH,self.HEIGHT))
        super().__init__(self.image,center)

    def update(self, player, enemy_handler, bullet_handler, bullet):
        self.rect.y += random.choice(self.SPEED)
        if self.rect.colliderect(player.rect) and player.has_power == True and player.power_type == SHIELD_TYPE :
            self.damage_audio()
            player.is_alive = True
            try:
                bullet_handler.bullets.remove(bullet)
            except:
                pass
        elif self.rect.colliderect(player.rect) and player.has_power == False:
            self.damage_audio()
            try:
                bullet_handler.bullets.remove(bullet)
            except:
                pass
            player.life -= 10
            if player.life == 0:
                player.is_alive = False
                player.life = 50

    def damage_audio(self):
        audio = DAMAGE_AUDIO
        audio.set_volume(0.2)
        CHANNEL_5.play(audio)