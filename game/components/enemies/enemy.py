import random
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_ENEMY_TYPE

class Enemy:
    WIDHT = 40
    HEIGHT = 60
    X_POS_LIST = [50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000]
    Y_POS = 0
    LEFT = 'left'
    RIGHT = 'right'
    MOV_X = [LEFT,RIGHT]
    SHOOTING_TIME = 30


    def __init__(self,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.mov_x = random.choice(self.MOV_X)
        self.index = 0
        self.is_alive = True
        self.shooting_time = 0
        # self.is_destroyed = False
    
    def update(self,bullet_handler,player):
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
        self.shooting_time += 1
        self.move()
        self.shoot(bullet_handler)
        if self.rect.colliderect(player.rect):
            player.is_alive = False
        # if not self.is_destroyed():
        #     self.is_destroyed = False

    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def move(self):
        self.rect.y += self.SPEED_Y

        if self.mov_x == self.LEFT:
            self.rect.x -= self.SPEED_X
            if self.index > random.choice(self.INTERVAL) or self.rect.x <= 0:
                self.mov_x = self.RIGHT
                self.index = 0
        else:
            self.rect.x += self.SPEED_X
            if self.index > random.choice(self.INTERVAL) or self.rect.x >= SCREEN_WIDTH - self.rect.width:
                self.mov_x = self.LEFT
                self.index = 0
        self.index += 1

    def shoot(self, bullet_handler):
        if self.shooting_time % self.SHOOTING_TIME == 0:
            bullet_handler.add_bullet(BULLET_ENEMY_TYPE,self.rect.center)