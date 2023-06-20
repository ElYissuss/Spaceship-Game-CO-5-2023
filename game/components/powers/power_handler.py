import random
import pygame
from game.components.powers.shield import Shield
from game.components.powers.life import Life
from game.components.powers.damage import Damage
from game.utils.constants import SPACESHIP_SHIELD, SHIELD_TYPE, DAMAGE_TYPE, LIFE_TYPE, SCREEN_HEIGHT, LIFE_AUDIO, DAMAGE_AUDIO, SHIELD_AUDIO, CHANNEL_1
from game.components import text_utils

class PowerHandler:
    def __init__(self):
        self.powers = []
        self.when_appears = random.randint(7000,10000)
        self.duration = random.randint(4,5)
        self.show_message = False

    def select_power(self):
        power_list = (Shield(),Damage(),Life())
        power_selected = random.choice(power_list)
        return power_selected

    def generate_power(self):
        power = self.select_power()
        self.powers.append(power)
        self.when_appears += random.randint(7000,10000)

    def update(self,player):
        current_time = pygame.time.get_ticks()

        if current_time >= self.when_appears:
            self.generate_power()

        self.get_power(player)

    def get_power(self, player):
        for power in self.powers:
            power.update()
            if player.rect.colliderect(power.rect):
                if power.type == SHIELD_TYPE:
                    self.shield_audio()
                    power.start_time = pygame.time.get_ticks()
                    player.power_type = power.type
                    player.has_power = True
                    player.power_time = power.start_time + (self.duration * 1000)
                    player.set_power_image(SPACESHIP_SHIELD)
                    self.powers.remove(power)
                elif power.type == DAMAGE_TYPE:
                    if player.damage < 30:
                        player.damage += 10
                        self.damage_audio()
                        self.powers.remove(power)
                    else:
                        pass
                elif power.type == LIFE_TYPE:
                    if player.life < 100:
                        player.life += 10
                        self.life_audio()
                        self.powers.remove(power)
                    else:
                        pass

    def draw(self, screen):
        for power in self.powers:
            power.draw(screen)

    def remove_power(self, power):
        if power.rect.y >= SCREEN_HEIGHT:
            self.powers.remove(power)

    def reset(self):
        self.powers = []
    
    def life_audio(self,):
        audio = LIFE_AUDIO
        audio.set_volume(1)
        CHANNEL_1.play(audio)
    
    def damage_audio(self):
        audio = DAMAGE_AUDIO
        audio.set_volume(1)
        CHANNEL_1.play(audio)
    
    def shield_audio(self):
        audio = SHIELD_AUDIO
        audio.set_volume(1)
        CHANNEL_1.play(audio)
