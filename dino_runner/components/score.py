from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT
import pygame

class Score():
    def __init__(self,game):
        self.game=game
        self.score=0
        self.current_score=self.score
        self.scores=[self.current_score]
        self.font= pygame.font.Font(FONT_STYLE,30)
        
    def update(self):
        self.current_score=self.score
        self.scores.append(self.score)
        self.score=0
        pygame.display.update()
    
    def draw(self ,screen):
        if not self.game.playing: 
            self.text= self.font.render(f"Score: {self.current_score} | Max-Score: {max(self.scores)}",True, (65,162,0))
            self.text_rect= self.text.get_rect()
            self.text_rect.center=(550,(SCREEN_HEIGHT//2)+50)
            screen.blit(self.text,self.text_rect)
        else:
            self.text= self.font.render(f"Score: {self.score}",True, (255,130,115))
            self.text_rect= self.text.get_rect()
            self.text_rect.center=(1000,50)
            screen.blit(self.text,self.text_rect)

    def update_score(self):
        self.score+=1
        if self.score%100==0 and self.game.game_speed<50:
            self.game.game_speed+=5
        

