
from dino_runner.components.power_ups.power_up import PowerUp

from dino_runner.utils.constants import HAMMER ,  HAMMER_TYPE, SCREEN_WIDTH


class Hammer(PowerUp):
    def __init__(self):
        self.launched_hammer=False

        
        super().__init__(HAMMER, HAMMER_TYPE)
    

    def udapte_hammer_launched(self,game_speed,hammer):
        self.rect.x+=game_speed

        # if self.rect.x>SCREEN_WIDTH:
        #     print("hola")
            # hammer.pop()
    # def launch_hammer(self):
    #     while self.launch_hammer:
    #         print("hola")