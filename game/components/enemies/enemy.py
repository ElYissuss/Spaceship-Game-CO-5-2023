import random
from game.utils.constants import SCREEN_WIDTH

class Enemy:
    WIDHT = 40
    HEIGHT = 60
    X_POS_LIST = [50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000]
    Y_POS = [0,20,40,60,80,100,120,140]
    LEFT = 'left'
    RIGHT = 'right'
    MOV_X = [LEFT,RIGHT]


    def __init__(self,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = random.choice(self.Y_POS)
        self.mov_x = random.choice(self.MOV_X)
        self.index = 0
    
    def update(self):
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
        
        if self.rect.y >= 600:
            self.rect.y = -40

    def draw(self,screen):
        screen.blit(self.image,self.rect)