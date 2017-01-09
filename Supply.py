import os
import sys
import pygame
import random
class Supply(pygame.sprite.Sprite):
    def __init__(self,bg_size,image):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(image).convert_alpha()
        self.active=False
        self.rect=self.image.get_rect()
        self.width,self.height=bg_size[0],bg_size[1]
        self.rect.left,self.rect.bottom=random.randint(0,self.width-self.rect.width),-100
        self.mask=pygame.mask.from_surface(self.image)
        self.speed=2
    def move(self):
        if self.rect.top > self.height:
            self.active=False
        else:
            self.rect.top+=self.speed


    def reset(self):
        self.active=True
        self.rect.left,self.rect.bottom=random.randint(0,self.width-self.rect.width),-100


class Bullet_Supply(Supply):
    def __init__(self,bg_size):
        Supply.__init__(self,bg_size,"shoot/ufo1.png")

class Bomb_Supply(Supply):
    def __init__(self,bg_size):
        Supply.__init__(self,bg_size,"shoot/ufo2.png")
