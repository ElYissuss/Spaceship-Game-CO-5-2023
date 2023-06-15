import random

from game.components.enemies.ship import Ship
from game.components.enemies.navy import Navy
from game.components.enemies.aircraft import Aircraft

class EnemyHandler:
    def __init__(self):
        self.enemies = []

    def election(self):
        ships = [Navy(),Ship(),Aircraft()]
        ship = random.choice(ships)
        return ship

    def update(self,bullet_handler):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(bullet_handler)
            if not enemy.is_alive:
                self.remove_enemy(enemy)

    def draw(self,screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 7:
            self.enemies.append(self.election())

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)