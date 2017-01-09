import  pygame
import random
class SuperEnemy(pygame.sprite.Sprite):
    def __init__(self,bg_size,image,speed,energy):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(image).convert_alpha()
        self.mask=pygame.mask.from_surface(self.image)
        self.active=True
        self.destroy_image=[]
        self.rect=self.image.get_rect()
        self.width,self.height=bg_size[0],bg_size[1]
        self.speed=speed
        self.energy=energy
    def move(self):
        if self.rect.top<self.height:
            self.rect.top+=self.speed
        else:
            self.reset()
    def reset(self):
        pass
class EnemyNum1(SuperEnemy):
    energy=5
    def __init__(self,bg_size):
        try:
            SuperEnemy.__init__(self,bg_size,"shoot/enemy1.png",speed=2,energy=5)
            self.destroy_image.extend([\
                pygame.image.load("shoot/enemy1_down1.png").convert_alpha(),
                pygame.image.load("shoot/enemy1_down2.png").convert_alpha(),
                pygame.image.load("shoot/enemy1_down3.png").convert_alpha(),
                pygame.image.load("shoot/enemy1_down4.png").convert_alpha()
                ])
            self.rect.top,self.rect.left=random.randint(-5*self.height,0),\
                                         random.randint(0,(self.width-self.rect.width))
        except Exception as e:
            raise  e;
            print (e)
    def reset(self):
        self.active=True
        self.rect.top,self.rect.left=random.randint(-5*self.height,0),\
                                     random.randint(0,(self.width-self.rect.width))


class EnemyNum2(SuperEnemy):
    energy=8
    def __init__(self,bg_size):
        SuperEnemy.__init__(self,bg_size,"shoot/enemy2.png",2,EnemyNum2.energy)
        self.imageHit=pygame.image.load("shoot/enemy2_hit.png").convert_alpha()
        self.destroy_image.extend([\
            pygame.image.load("shoot/enemy2_down1.png").convert_alpha(),
            pygame.image.load("shoot/enemy2_down2.png").convert_alpha(),
            pygame.image.load("shoot/enemy2_down3.png").convert_alpha(),
            pygame.image.load("shoot/enemy2_down4.png").convert_alpha()
            ])
        self.rect.top,self.rect.left=random.randint(-15*self.height,-5*self.height),\
                                     random.randint(0,(self.width-self.rect.width))
        self.IsHit=False
    def reset(self):
        self.IsHit=False
        self.active=True
        self.energy=EnemyNum2.energy
        self.rect.top,self.rect.left=random.randint(-15*self.height,-5*self.height),\
                                     random.randint(0,(self.width-self.rect.width))

class EnemyNum3(SuperEnemy):
    energy=15
    def __init__(self,bg_size):
        SuperEnemy.__init__(self,bg_size,"shoot/enemy3_n1.png",1,EnemyNum3.energy)
        self.image2=pygame.image.load("shoot/enemy3_n2.png").convert_alpha()
        self.imageHit1=pygame.image.load("shoot/enemy3_n1.png").convert_alpha()
        self.imageHit3=pygame.image.load("shoot/enemy3_hit.png").convert_alpha()
        self.imageHit2=pygame.image.load("shoot/enemy3_n2.png").convert_alpha()
        #self.shoot=pygame.image.load("shoot")
        self.destroy_image.extend([\
            pygame.image.load("shoot/enemy3_down1.png").convert_alpha(),
            pygame.image.load("shoot/enemy3_down2.png").convert_alpha(),
            pygame.image.load("shoot/enemy3_down3.png").convert_alpha(),
            pygame.image.load("shoot/enemy3_down4.png").convert_alpha(),
            pygame.image.load("shoot/enemy3_down5.png").convert_alpha(),
            pygame.image.load("shoot/enemy3_down6.png").convert_alpha()
            ])
        self.rect.top,self.rect.left=random.randint(-15*self.height,-5*self.height),\
                                     random.randint(0,(self.width-self.rect.width))
        self.IsHit=False

    def reset(self):
        self.active=True
        self.IsHit=False
        self.energy=EnemyNum3.energy
        self.rect.top,self.rect.left=random.randint(-15*self.height,-5*self.height),\
                                     random.randint(0,(self.width-self.rect.width))