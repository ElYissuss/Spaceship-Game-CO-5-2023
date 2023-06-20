import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, WHITE_COLOR, DEFAULT_TYPE, MENU_AUDIO, PLAYING_AUDIO, CHANNEL_2, CHANNEL_3, LOSE_AUDIO, CHANNEL_6
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.bullets.bullet_handler import BulletHandler
from game.components.powers.power_handler import PowerHandler
from game.components import text_utils


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_handler = EnemyHandler()
        self.bullet_handler = BulletHandler()
        self.power_handler = PowerHandler()
        self.score = 0
        self.high_score = 0
        self.number_death = 0

    def run(self):
        self.menu_audio()
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            elif event.type == pygame.KEYDOWN and not self.playing:
                user_input = pygame.key.get_pressed()
                if user_input[pygame.K_RETURN]:
                    CHANNEL_2.stop()
                    self.playing_audio()
                    self.playing = True
                    self.reset()

    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            user_input_shoot = pygame.key.get_pressed()
            user_input_2 = pygame.key.get_pressed()
            self.player.update(user_input,user_input_2,user_input_shoot,self.bullet_handler)
            self.enemy_handler.update(self.bullet_handler,self.player)
            self.bullet_handler.update(self.player,self.enemy_handler, self.bullet_handler)
            self.score = self.enemy_handler.number_enemy_destroyed
            self.power_handler.update(self.player)
            if not self.player.is_alive:
                pygame.time.delay(300)
                self.playing = False
                self.number_death += 1
                self.lose_audio()

    def draw(self):
        self.draw_background()
        if self.playing:
            self.clock.tick(FPS)
            self.player.draw(self.screen)
            self.enemy_handler.draw(self.screen)
            self.bullet_handler.draw(self.screen)
            self.power_handler.draw(self.screen)
            self.draw_score()
            self.draw_power_time()
        else:
            self.draw_menu()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def draw_menu(self):
        if self.number_death == 0:
            text, text_rect = text_utils.get_message("Press return to start",30,WHITE_COLOR)
            self.screen.blit(text,text_rect)
        else:
            CHANNEL_3.stop()
            if self.high_score < self.score:
                self.high_score = self.score
            text, text_rect = text_utils.get_message("Press return to restart",30,WHITE_COLOR,height = (SCREEN_HEIGHT//2)-20)
            try_number, try_number_rect = text_utils.get_message(f"Try number: {self.number_death} ",20,WHITE_COLOR,height = (SCREEN_HEIGHT//2)+50)
            score, score_rect = text_utils.get_message(f"Your score is: {self.score} ",20,WHITE_COLOR,height = (SCREEN_HEIGHT//2)+100)
            high_score, high_score_rect = text_utils.get_message(f"High score: {self.high_score} ",20,WHITE_COLOR,height = (SCREEN_HEIGHT//2)+150)
            self.screen.blit(try_number, try_number_rect)
            self.screen.blit(text,text_rect)
            self.screen.blit(score,score_rect)
            self.screen.blit(high_score,high_score_rect)
    
    def draw_score(self):
        score, score_rect = text_utils.get_message(f"your score is: {self.score} ",20,WHITE_COLOR,1000,40)
        life, life_rect = text_utils.get_message(f"life left: {self.player.life} ",20,WHITE_COLOR,1000,60)
        damage, damage_rect = text_utils.get_message(f"Actual damage: {self.player.damage} ",20,WHITE_COLOR,1000,80)
        self.screen.blit(score, score_rect)
        self.screen.blit(life, life_rect)
        self.screen.blit(damage, damage_rect)

    def draw_power_time(self):
        if self.player.has_power:
            power_time = round((self.player.power_time - pygame.time.get_ticks()) / 1000)
            if power_time >= 0:
                text, text_rect = text_utils.get_message(f"{self.player.power_type.capitalize()} is enabled for {power_time} ",20,WHITE_COLOR,150,50)
                self.screen.blit(text, text_rect)
            else:
                self.player.has_power = False
                self.player.power_type = DEFAULT_TYPE
                self.player.set_default_image()

    def reset(self):
        self.player.reset()
        self.bullet_handler.reset()
        self.enemy_handler.reset()
        self.power_handler.reset()

    def menu_audio(self):
        audio = MENU_AUDIO
        audio.set_volume(0.2)
        CHANNEL_2.play(audio)

    def playing_audio(self):
        audio = PLAYING_AUDIO
        audio.set_volume(0.1)
        CHANNEL_3.play(audio)
    
    def lose_audio(self):
        audio = LOSE_AUDIO
        audio.set_volume(0.1)
        CHANNEL_6.play(audio)
