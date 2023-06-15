import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT

class Spaceship:
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = 500
    SPEED = 10

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image,(40,60))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.velocity = self.SPEED
        self.is_alive = True
    
    def update(self,user_input):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move_left(self):
        self.rect.x -= self.velocity
        if self.rect.x == -30:
            self.rect.x = 1070
    
    def move_right(self):
        self.rect.x += self.velocity
        if self.rect.x == 1080:
            self.rect.x = -30
    
    def move_up(self):
        if self.rect.y > 0:
            self.rect.y -= self.velocity
    
    def move_down(self):
        if self.rect.y < (SCREEN_HEIGHT)-60:
            self.rect.y += self.velocity
