import random
from dino_runner.components.power_ups.shield import Shield
from dino_runner.utils.constants import SHIELD_TYPE
import pygame


class PowerUpManager():
    def __init__(self):
       self.power_ups=[]
       self.duration=random.randint(3,4)
       self.appears_when= random.randint(60,80)

    def update(self,game):
        if len(self.power_ups)==0 and self.appears_when ==game.game_score.score:
            self.appears_when+=random.randint(150,210)
            powerUp= Shield()
            self.power_ups.append(powerUp)
        
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                power_up.start_time=pygame.time.get_ticks()
                game.player.has_power_up=True
                game.player.type=SHIELD_TYPE
                game.player.power_up_time= power_up.start_time+(self.duration*1000)
                self.power_ups.remove(power_up)

    
    def draw(self,screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups=[]
        self.appears_when =random.randint(60,80)