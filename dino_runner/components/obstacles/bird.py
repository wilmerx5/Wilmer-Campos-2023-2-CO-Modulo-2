# from dino_runner.utils.constants import BIRD
import pygame

from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self,image):
        super().__init__(image,1)
        
      