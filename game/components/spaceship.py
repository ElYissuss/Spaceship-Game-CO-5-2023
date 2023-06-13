import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT

class Spaceship:
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = 500

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image,(40,60))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
    
    def update(self,user_input):
        if user_input[pygame.K_LEFT]:
            self.move_left()
            if self.rect.x == 0:
                self.rect.x = 1060
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
            if self.rect.x == 1060:
                self.rect.x = 0
        elif user_input[pygame.K_UP]:
            self.move_up()
            if self.rect.y == 0:
                self.rect.y = 540
        elif user_input[pygame.K_DOWN]:
            self.move_down()
            if self.rect.y == 540:
                self.rect.y = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= 10
    
    def move_right(self):
        if self.rect.x < (SCREEN_WIDTH)-40:
            self.rect.x += 10
    
    def move_up(self):
        if self.rect.y > 0:
            self.rect.y -= 10
    
    def move_down(self):
        if self.rect.y < (SCREEN_HEIGHT)-60:
            self.rect.y += 10