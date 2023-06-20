from game.components.powers.power import Power
from game.utils.constants import LIFE, LIFE_TYPE

class Life(Power):
    POWER_SPEED = 5
    def __init__(self):
        super().__init__(LIFE, LIFE_TYPE)