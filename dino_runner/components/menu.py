import pygame
from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH
class Menu:
    def __init__(self,screen,message):
        half_screen_witdh=SCREEN_WIDTH//2
        half_screen_height=SCREEN_HEIGHT//2
        screen.fill((255,255,255))
        self.font= pygame.font.Font(FONT_STYLE,30)
        self.text= self.font.render(message,True, (0,0,0))
        self.text_rect= self.text.get_rect()
        self.text_rect.x= self.half_screen_witdh
        self.text_rect.y=self.half_screen_height

    
    def update(self):
        pass

    
    def draw(self):
        pass