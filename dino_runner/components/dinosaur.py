# from dino_runner.components.power_ups.hammer import Hammer
import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import DEFAULT_TYPE, HAMMER_TYPE,SHIELD_TYPE, RUNNING,RUNNING_HAMMER,RUNNING_SHIELD , JUMPING,JUMPING_HAMMER,JUMPING_SHIELD, DUCKING,DUCKING_HAMMER,DUCKING_SHIELD,HAMMER


RUN_IMAGE={DEFAULT_TYPE:RUNNING, HAMMER_TYPE:RUNNING_HAMMER,SHIELD_TYPE:RUNNING_SHIELD}
DUCK_IMAGE={DEFAULT_TYPE:DUCKING, HAMMER_TYPE:DUCKING_HAMMER,SHIELD_TYPE:DUCKING_SHIELD}
JUMP_IMAGE={DEFAULT_TYPE:JUMPING, HAMMER_TYPE:JUMPING_HAMMER,SHIELD_TYPE:JUMPING_SHIELD}

class Dinosaur(Sprite):
    X_POS=80
    Y_POST=310
    JUMP_SPEED=8.5
    def __init__(self,game):
        self.game=game
        self.type= DEFAULT_TYPE
        self.image=RUN_IMAGE[self.type][0]
        self.dino_rect= self.image.get_rect()
        self.dino_rect.x=self.X_POS
        self.dino_rect.y= self.Y_POST
        self.dino_run=True
        self.step_index=0
        self.dino_jump=False
        self.jump_speed=self.JUMP_SPEED
        self.dino_duck=False
        self.has_power_up=False
        self.power_up_time=0
        self.image_hammer=HAMMER

    def update(self,user_input,game):


        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()

        # if self.type == HAMMER_TYPE:
        #     if user_input[pygame.K_SPACE]:
        #         self.type=DEFAULT_TYPE
        if user_input[pygame.K_UP] and not self.dino_jump :
            self.dino_jump=True
            self.dino_run=False
        
        
                
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck=True
            self.dino_run=False

        elif not self.dino_jump:
            self.dino_jump=False
            self.dino_run=True
        
    

        if self.step_index>9:
            self.step_index=0

    def draw(self,screen,game, user_input):
        screen.blit(self.image,(self.dino_rect.x,self.dino_rect.y))


    def run(self):
        self.image=RUN_IMAGE[self.type][self.step_index//5]
        self.dino_rect=self.image.get_rect()
        self.dino_rect.x=self.X_POS
        self.dino_rect.y=self.Y_POST
        self.step_index+=1
    
    def jump(self):
        self.image=JUMP_IMAGE[self.type]
        self.dino_rect.y-=self.jump_speed*4
        self.jump_speed-=0.8
        if self.jump_speed<-self.JUMP_SPEED:
            self.dino_rect.y=self.Y_POST
            self.dino_jump=False
            self.jump_speed=self.JUMP_SPEED

    def duck(self):
        self.image=DUCK_IMAGE[self.type][self.step_index//5]
        self.dino_rect=self.image.get_rect()
        self.dino_rect.x=self.X_POS
        self.dino_rect.y=self.Y_POST+35
        self.step_index+=1

    def reset(self):
        self.dino_rect.x= self.X_POS
        self.dino_rect.y= self.Y_POST
        self.step_index=0
        self.dino_run=True
        self.dino_jump=False
        self.dino_duck=False
        self.jump_speed= self.JUMP_SPEED
    
#agacharse