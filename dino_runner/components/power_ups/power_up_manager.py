import random
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.shield import Shield
from dino_runner.utils.constants import DEFAULT_TYPE, HAMMER_TYPE, SHIELD_TYPE
import pygame


class PowerUpManager():
    def __init__(self):
       self.power_ups=[]
       self.hammer=[]
       
       
       self.duration=random.randint(3,4)
       self.appears_when= random.randint(60,80)

    def update(self,game,input_press):
        if len(self.power_ups)==0 and self.appears_when ==game.game_score.score:
            choice_power_up=random.randint(0,1)
            self.appears_when+=random.randint(150,210)
            # powerUp=Shield() if choice_power_up==1 else Hammer()
            powerUp=Hammer()

            self.power_ups.append(powerUp)
        


        if len(self.hammer)==1:
            self.hammer[0].udapte_hammer_launched(game.game_speed,self.hammer)

        if game.player.type == HAMMER_TYPE and input_press[pygame.K_SPACE]:
            game.player.type=DEFAULT_TYPE
            self.hammer[0].launched_hammer=True
            self.hammer[0].rect.x= game.player.X_POS
            self.hammer[0].rect.y= game.player.dino_rect.y
            
        
        
         
        
            
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                power_up.start_time=pygame.time.get_ticks()
                game.player.has_power_up=True
                game.player.type=power_up.type
                if game.player.type == HAMMER_TYPE:
                    self.hammer.append(Hammer())
                game.player.power_up_time= power_up.start_time+(self.duration*1000)
                self.power_ups.remove(power_up)
        
           
                

    
    def draw(self,screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
        
        print(len(self.hammer))
        
        if len(self.hammer)==1:
            if self.hammer[0].launched_hammer:
                self.hammer[0].draw(screen)
                

        

    def reset_power_ups(self):
        self.power_ups=[]
        self.hammer=[]
        self.appears_when =random.randint(60,80)