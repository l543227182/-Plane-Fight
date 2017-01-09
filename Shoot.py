import  os
import sys
import pygame
class Shoot(pygame.sprite.Sprite):
    def __init__(self,image,position,speed=12):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(image).convert_alpha()
        self.rect=self.image.get_rect()
        self.active=True
        self.speed=speed
        self.rect.left,self.rect.top=position

    def move(self):
        self.rect.top-=self.speed
        if self.rect.top<0:
            self.active=False
    def reset(self,position):
        self.active=True
        self.rect.left,self.rect.top=position

class bullet1(Shoot):
    def __init__(self,position):
        Shoot.__init__(self,"shoot/bullet1.png",position)

class bullet2(Shoot):
    def __init__(self,position):
        Shoot.__init__(self,"shoot/bullet2.png",position)
