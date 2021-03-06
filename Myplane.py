import  pygame

class Myplane(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        self.image=pygame.image.load("shoot/hero2.png")
        self.image2=pygame.image.load("shoot/hero1.png")
        self.rect=self.image.get_rect()
        self.width,self.height=bg_size[0],bg_size[1]
        self.destroy_image=[]
        self.active=True
        self.destroy_image.extend([\
            pygame.image.load("shoot/hero_blowup_n1.png").convert_alpha(),
            pygame.image.load("shoot/hero_blowup_n2.png").convert_alpha(),
            pygame.image.load("shoot/hero_blowup_n3.png").convert_alpha(),
            pygame.image.load("shoot/hero_blowup_n4.png").convert_alpha()
            ])
        self.rect.top,self.rect.left=self.height-self.rect.height-60,\
                                     (self.width-self.rect.width)//2
        self.speed=10
        self.mask=pygame.mask.from_surface(self.image)

    def moveUp(self):
        if self.rect.top>0:
            self.rect.top-=self.speed;
        else:
            self.rect.top=0;

    def moveDown(self):
        if self.rect.bottom<self.height:
            self.rect.bottom+=self.speed;
        else:
            self.rect.bottom=self.height-60

    def moveLeft(self):
        if self.rect.left>0:
            self.rect.left-=self.speed;
        else:
            self.rect.left=0
    def moveRight(self):
        if self.rect.right<self.width:
            self.rect.right+=self.speed
        else:
            self.rect.right=self.width;
    def reset(self):
        self.active=True
        self.rect.top,self.rect.left=self.height-self.rect.height-60,\
                                     (self.width-self.rect.width)//2