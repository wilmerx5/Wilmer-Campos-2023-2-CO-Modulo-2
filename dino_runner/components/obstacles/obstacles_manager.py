
import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import DEFAULT_TYPE, SHIELD_TYPE, SMALL_CACTUS, LARGE_CACTUS,BIRD


class ObstacleManager:
    def __init__(self):
        self.obstacles=[]
    def update(self,game):
        
        if len(self.obstacles)==0:
            choice_obstacle =random.randint(0,1)
            choice_cactus= random.randint(0,1)
            bird= Bird(BIRD)
            cactus=Cactus(SMALL_CACTUS) if choice_cactus==0 else Cactus(LARGE_CACTUS)
            self.obstacles.append(cactus) if choice_obstacle==0 else self.obstacles.append(bird)
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed,self.obstacles)

    
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.type !=  SHIELD_TYPE:

                    game.death_count+=1
                    game.game_score.update()
           
                    game.power_up_manager.hammer=[]
                    game.player.type=DEFAULT_TYPE
                    game.playing=False
                    break
                else:
                    # game.power_up_manager.reset_power_ups()
                    
                    self.reset_obstacles()
                    
                
            if len(game.power_up_manager.hammer)==1:
                if obstacle.rect.colliderect(game.power_up_manager.hammer[0].rect):
                    self.reset_obstacles()
                    game.power_up_manager.hammer=[]
                




    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    
    def reset_obstacles(self):
        self.obstacles=[]