
import random

from game.components.enemies.ship import Ship
from game.components.enemies.navy import Navy
from game.components.enemies.aircraft import Aircraft

class EnemyHandler:
    def __init__(self):
        self.enemies = []
        for i in range(8):
            self.election()

    def election(self):
        ships = [Navy(),Ship(),Aircraft()]
        ship = random.choice(ships)
        self.enemies.append(ship)

    def update(self):
        for enemy in self.enemies:
            enemy.update()

    def draw(self,screen):
        for enemy in self.enemies:
            enemy.draw(screen)