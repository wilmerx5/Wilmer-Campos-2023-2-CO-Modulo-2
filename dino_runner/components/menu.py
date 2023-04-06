import pygame
from dino_runner.utils.constants import FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH
class Menu:
    half_screen_witdh=SCREEN_WIDTH//2
    half_screen_height=SCREEN_HEIGHT//2
    def __init__(self,screen,message):
        
        screen.fill((255,255,255))
        self.font= pygame.font.Font(FONT_STYLE,30)
        self.text= self.font.render(message,True, (0,213,192))
        self.text_rect= self.text.get_rect()
        self.text_rect.center=(self.half_screen_witdh,self.half_screen_height)
    
    def update(self,game):
        self.handle_events_on_menu(game)
        pygame.display.update()
    
    def draw(self,screen):
        screen.blit(self.text,self.text_rect)
    
    
    def handle_events_on_menu(self,game):
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                game.running=False
                game.playing=False

            elif event.type==pygame.KEYDOWN:
                # game.player.dino_jump=False
                # game.player.dino_rect.y=game.player.Y_POST
                
                game.run()

    def update_message(self,message):
        self.text= self.font.render(message,True, (185,0,0))
        self.text_rect= self.text.get_rect()
        self.text_rect.center=(self.half_screen_witdh,self.half_screen_height)

    
    def show_menu(self,game):
        game.screen.fill((255,255,255))
        half_screen_witdh = SCREEN_WIDTH//2
        half_screen_height = SCREEN_HEIGHT//2
        game.screen.blit(ICON,(half_screen_witdh-50,half_screen_height-140 ))
        if game.death_count==0:
            game.screen.blit(self.text,self.text_rect)

        else:
            self.update_message(f"Dino has died :( | Dies:{game.death_count} ")
            game.screen.blit(self.text,self.text_rect)
            game.game_score.draw(game.screen)
        self.update(game)