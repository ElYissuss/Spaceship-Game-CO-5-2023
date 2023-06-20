from game.components.powers.power import Power
from game.utils.constants import DAMAGE, DAMAGE_TYPE

class Damage(Power):
    POWER_SPEED = 12
    def __init__(self):
        super().__init__(DAMAGE, DAMAGE_TYPE)