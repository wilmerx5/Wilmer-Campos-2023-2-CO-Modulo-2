from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.menu import Menu
from dino_runner.components.obstacles.obstacles_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.score import Score
import pygame

from dino_runner.utils.constants import BG, DEFAULT_TYPE, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DUCKING


class Game:
    GAME_SPEED=20
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.player=Dinosaur(self)
        self.playing = False
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.obstacle_manager=ObstacleManager()
        self.power_up_manager=PowerUpManager()
        
        self.running=False
        self.menu= Menu(self.screen,"Press any key to start")
        self.game_score=Score(self)
        self.death_count=0

    def run(self):
        # Game loop: events - update - draw
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.game_speed=self.GAME_SPEED
        self.playing = True
        self.player.reset()
        while self.playing:
            self.events()
            self.update()
            self.draw()
        # self.reset_game()

    def execute(self):
        self.running=True
        while self.running:
            if not self.playing:
                self.menu.show_menu(self)
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input=pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.game_score.update_score()
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up()
        self.game_score.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()   

        

    def draw_background(self):
        image_width = BG.get_width()
        # self.screen.fill((2555,100,100))
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_power_up(self):
        if self.player.has_power_up:
            time_to_show= round((self.player.power_up_time-pygame.time.get_ticks())/1000,2)
            if time_to_show>0:
                font= pygame.font.Font(FONT_STYLE,30)
                text= font.render(f"{self.player.type} enable for {time_to_show} seconds",True, (0,213,192))
                text_rect= text.get_rect()
                # text_rect.center=(half_screen_witdh,self.half_screen_height)
                # self.menu.draw(self.screen,f"{self.player.type} enable for {time_to_show} seconds",500,50)
                self.screen.blit(text,(400,60))
            
            else:
                self.player.has_power_up=False
                self.player.type=DEFAULT_TYPE
    # def reset_game(self):
    #     # self.player.dino_run=False
    #     self.game_speed=self.GAME_SPEED
    #     self.player.reset()
        # self.player.dino_jump=False
    # def show_menu(self):
    #     self.menu.reset_screen_color(self.screen)
    #     half_screen_witdh = SCREEN_WIDTH//2
    #     half_screen_height = SCREEN_HEIGHT//2
    #     self.screen.blit(ICON,(half_screen_witdh-50,half_screen_height-140 ))
    #     if self.death_count==0:
    #         self.menu.draw(self.screen)
    #     else:
    #         self.menu.update_message(f"Dino has died :( | Dies:{self.death_count} ")
    #         self.menu.draw(self.screen)
    #         self.game_score.draw(self.screen)
    #     self.menu.update(self)


    

    
        
