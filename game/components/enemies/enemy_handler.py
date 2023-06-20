import random

from game.components.enemies.ship import Ship
from game.components.enemies.navy import Navy
from game.components.enemies.aircraft import Aircraft

class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.number_enemy_destroyed = 0

    def election(self):
        ships = [Navy(),Ship(),Aircraft()]
        ship = random.choice(ships)
        return ship

    def update(self,bullet_handler,player):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(bullet_handler,player)
            if not enemy.is_alive:
                self.remove_enemy(enemy)

    def draw(self,screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        number = [7,8,9,10]
        if len(self.enemies) < random.choice(number):
            self.enemies.append(self.election())

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def reset(self):
        self.enemies = []
        self.number_enemy_destroyed = 0
    
    def stop(self):
        self.enemies = []
