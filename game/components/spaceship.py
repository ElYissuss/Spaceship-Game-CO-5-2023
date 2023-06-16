import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_SHIP_TYPE

class Spaceship:
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = 500
    SPEED = 10
    DIAGONAL_SPEED = 5
    lAST_K_TIME = 0
    DELAY = 250

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image,(40,60))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.speed = self.SPEED
        self.diagonal_speed = self.DIAGONAL_SPEED
        self.is_alive = True
    
    def update(self,user_input,user_input_2,user_input_shoot,bullet_handler):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()

        if user_input[pygame.K_LEFT] and user_input_2[pygame.K_UP]:
            self.move_up_left()
        elif user_input[pygame.K_RIGHT] and user_input_2[pygame.K_UP]:
            self.move_up_right()
        elif user_input[pygame.K_LEFT] and user_input_2[pygame.K_DOWN]:
            self.move_down_left()
        elif user_input[pygame.K_RIGHT] and user_input_2[pygame.K_DOWN]:
            self.move_down_right()

        if user_input_shoot[pygame.K_a] and pygame.time.get_ticks() - self.lAST_K_TIME > self.DELAY:
            self.shoot(bullet_handler)
            self.lAST_K_TIME = pygame.time.get_ticks()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move_left(self):
        self.rect.x -= self.speed
        if self.rect.x == -30:
            self.rect.x = 1070
    
    def move_right(self):
        self.rect.x += self.speed
        if self.rect.x == 1080:
            self.rect.x = -30
    
    def move_up(self):
        if self.rect.y > 0:
            self.rect.y -= self.speed
    
    def move_down(self):
        if self.rect.y < (SCREEN_HEIGHT)-60:
            self.rect.y += self.speed
    
    def move_up_left(self):
        if self.rect.y > -30:
            self.rect.y -= self.diagonal_speed
            self.rect.x -= self.diagonal_speed
            if self.rect.x == -30:
                self.rect.x = 1070

    def move_up_right(self):
        if self.rect.y > 0:
            self.rect.y -= self.diagonal_speed
            self.rect.x += self.diagonal_speed
            if self.rect.x == 1080:
                self.rect.x = -30

    def move_down_left(self):
        if self.rect.y < (SCREEN_HEIGHT)-60:
            self.rect.y += self.diagonal_speed
            self.rect.x -= self.diagonal_speed
            if self.rect.x == -30:
                self.rect.x = 1070

    def move_down_right(self):
        if self.rect.y < (SCREEN_HEIGHT)-60:
            self.rect.y += self.diagonal_speed
            self.rect.x += self.diagonal_speed
            if self.rect.x == 1080:
                self.rect.x = -30

    def shoot(self,bullet_handler):
            bullet_handler.add_bullet(BULLET_SHIP_TYPE,self.rect.center)

    def reset(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
