from dino_runner.components.obstacles.obstacle import Obstacle

from dino_runner.utils.constants import  LARGE_CACTUS, SMALL_CACTUS
import random

class Cactus(Obstacle):

    def __init__(self, image):
        self.type=random.randint(0,2)

        super().__init__(image,self.type)
        self.rect.y=330 if self.image==LARGE_CACTUS else 325

      

