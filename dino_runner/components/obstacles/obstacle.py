import pygame
from pygame.sprite import Sprite
import random

from dino_runner.utils.constants import BIRD, SCREEN_WIDTH

class Obstacle(Sprite):

    def __init__(self,image,obstacle_type) :
        self.flutter_index=0
        #lista
        self.image=image
        #indice
        self.obstacle_type=obstacle_type
        self.rect=self.image[self.obstacle_type].get_rect()
        self.rect.x= SCREEN_WIDTH
        self.current_x=self.rect.x
        self.range_bird=[270,200,150]
        self.current_y= random.choice(self.range_bird)

    def update(self,game_speed,obstacles):
        self.current_x-=game_speed
        self.flutter_index+=1

        self.rect.x-=game_speed
        if self.rect.x< -self.rect.width:
            obstacles.pop()

        if self.image==BIRD:
            self.obstacle_type=0  if self.flutter_index<5 else 1
            self.rect=self.image[self.obstacle_type].get_rect()
            self.rect.x=self.current_x
            self.rect.y=self.current_y

        if self.flutter_index>10:
            self.flutter_index=0

        
        
            

    def draw(self,screen):
        screen.blit(self.image[self.obstacle_type],(self.rect.x,self.rect.y))
        