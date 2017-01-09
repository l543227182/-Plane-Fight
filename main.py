# -*- coding: utf-8 -*-
import os
import  sys
from pygame.locals import  *
import  pygame
from Myplane import Myplane
import Enemy
from Shoot import bullet1,bullet2
import Supply
import random
pygame.init()
pygame.mixer.init()
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
bg_size=width,height=480,600
screen=pygame.display.set_mode(bg_size)
pygame.display.set_caption("PlaneGame")
background=pygame.image.load("shoot_background/background.png").convert()

pygame.mixer.music.load("sound/game_music.mp3")
pygame.mixer.music.set_volume(0.2)

bullet_sound=pygame.mixer.Sound("sound/bullet.wav")
bullet_sound.set_volume(0.2)

bomb_sound=pygame.mixer.Sound("sound/use_bomb.wav")
bomb_sound.set_volume(0.2)
#supply
supply_sound=pygame.mixer.Sound("sound/out_porp.wav")
supply_sound.set_volume(0.2)

get_bomb_sound=pygame.mixer.Sound("sound/get_bomb.wav")
get_bomb_sound.set_volume(0.2)

get_bullet_sound=pygame.mixer.Sound("sound/get_double_laser.wav")
get_bullet_sound.set_volume(0.2)

#upgrade
get_bullet_sound=pygame.mixer.Sound("sound/achievement.wav")
get_bullet_sound.set_volume(0.2)

#
enemy3_fly_sound=pygame.mixer.Sound("sound/big_spaceship_flying.wav")
enemy3_fly_sound.set_volume(0.2)

enemy1_down_sound=pygame.mixer.Sound("sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.1)

enemy2_down_sound=pygame.mixer.Sound("sound/enemy2_down.wav")
enemy2_down_sound.set_volume(0.2)

enemy3_down_sound=pygame.mixer.Sound("sound/enemy3_down.wav")
enemy3_down_sound.set_volume(0.5)

me_down_sound=pygame.mixer.Sound("sound/game_over.wav")
me_down_sound.set_volume(0.2)


def add_small_plane(group1,group2,num):
    for i in range(num):
        enemy=Enemy.EnemyNum1(bg_size)
        while pygame.sprite.spritecollide(enemy,group2,False,pygame.sprite.collide_mask):
            enemy.reset()

        group1.add(enemy)
        group2.add(enemy)
def add_middle_plane(group1,group2,num):
    for i in range(num):
        enemy=Enemy.EnemyNum2(bg_size)
        while pygame.sprite.spritecollide(enemy,group2,False,pygame.sprite.collide_mask):
            enemy.reset()
        group1.add(enemy)
        group2.add(enemy)
def add_big_plane(group1,group2,num):
    for i in range(num):
        enemy=Enemy.EnemyNum3(bg_size)
        while pygame.sprite.spritecollide(enemy,group2,False,pygame.sprite.collide_mask):
            enemy.reset()
        group1.add(enemy)
        group2.add(enemy)
def SupplyDraw(Supply,screen,myplane):
    Supply.move();
    screen.blit(Supply.image,Supply.rect)
    return pygame.sprite.collide_mask(Supply,myplane)
def main():

    #播放背景音乐
    pygame.mixer.music.play(-1);
    running=True
    clock=pygame.time.Clock()
    myplane=Myplane(bg_size)

    #图片转换
    switch_image=False

    #生成敌人飞机
    enemies=pygame.sprite.Group()

    #敌人数量
    enemiesNum=[15,20,2]

    #得分
    score=0
    score_font=pygame.font.Font("shoot/1979.ttf",26)

    #玩家生命
    life=3
    life_font=pygame.font.Font("shoot/1979.ttf",26)
    #普通子弹
    norm_bullet=[]
    bullet_index=0
    BULLETNUM=4
    for each in range(BULLETNUM):
        norm_bullet.append(bullet1(myplane.rect.midtop))
        #print(myplane.rect.midtop)
        #print(bullets[each].rect," ",each)
    #超级子弹
    super_bullet=[]
    super_bullet_index=0
    SUPPEBULLETRNUM=8
    DOUBLEBULLET=USEREVENT+1
    for each in range(SUPPEBULLETRNUM//2):
        super_bullet.append(bullet2(((myplane.rect.centerx-33),myplane.rect.centery)))
        super_bullet.append(bullet2(((myplane.rect.centerx+33),myplane.rect.centery)))
    ISDouble_Bullet=False
    #补给包
    supply_bomb=Supply.Bomb_Supply(bg_size)
    supply_bullet=Supply.Bullet_Supply(bg_size)
    SUPPLY_TIME=USEREVENT
    pygame.time.set_timer(SUPPLY_TIME,30*1000)
    #摧毁敌人图片索引
    DestroyMe_index=0
    DestroySmall_index=0
    DestroyMiddle_index=0
    DestroyBig_index=0

    #设置等级
    level=1

    #炸弹图片
    bomb_num=3
    bomb_image=pygame.image.load("shoot/bomb.png").convert_alpha()
    bomb_rect=bomb_image.get_rect()
    bomb_rect.left,bomb_rect.top=10,height-bomb_rect.height-10

    #暂停按钮
    paused=False
    game_pause_nor=pygame.image.load("shoot/game_pause_nor.png").convert_alpha()
    game_pause_pressed=pygame.image.load("shoot/game_pause_pressed.png").convert_alpha()
    game_resume_nor=pygame.image.load("shoot/game_resume_nor.png").convert_alpha()
    game_resume_pressed=pygame.image.load("shoot/game_resume_pressed.png").convert_alpha()
    paused_rect=game_pause_nor.get_rect()
    paused_rect.left,paused_rect.top=width-paused_rect.width-10,10
    pause_image=game_pause_nor
    #按钮图标
    game_again=pygame.image.load("shoot/game_again.png").convert_alpha()
    game_again_over=pygame.image.load("shoot/game_again.png").convert_alpha()

    game_again_rect=game_again.get_rect()
    game_again_over_rect=game_again_over.get_rect()


    game_again_rect.top,game_again_rect.left=height//2-50,(width-game_again_rect.width)//2
    game_again_over_rect.left,game_again_over_rect.top=(game_again_rect.left ,game_again_rect.top+160)

    game_continue=pygame.image.load("shoot/game_continue.png").convert_alpha()
    game_continue_rect=game_continue.get_rect()
    game_continue_rect.top,game_continue_rect.left=height//2-110,(width-game_continue_rect.width)//2
    game_over=pygame.image.load("shoot/game_over.png").convert_alpha()
    game_over_over=pygame.image.load("shoot/game_over.png").convert_alpha()
    game_over_over_rect=game_over_over.get_rect()
    game_over_rect=game_over.get_rect()
    game_over_rect.top,game_over_rect.left=height//2+10,(width-game_over_rect.width)//2
    game_over_over_rect.left,game_over_over_rect.top=(game_over_rect.left ,game_over_rect.top+160)
    #小飞机
    SmallEnemies=pygame.sprite.Group()
    add_small_plane(SmallEnemies,enemies,enemiesNum[0])

    #中飞机
    MiddleEnemies=pygame.sprite.Group()
    add_middle_plane(MiddleEnemies,enemies,enemiesNum[1])

    #大飞机
    BigEnemies=pygame.sprite.Group()
    add_big_plane(BigEnemies,enemies,enemiesNum[2])
    delay=100
    #最高分
    readScore=False
    Game_Over=False
    while running:
        for  event in pygame.event.get():
            if event.type==QUIT:
                sys.exit()
            elif event.type==SUPPLY_TIME:
                supply_sound.play()
                if random.choice([True,False]):
                    supply_bomb.reset()
                else:
                    supply_bullet.reset()
            elif event.type==DOUBLEBULLET:
                ISDouble_Bullet=False
                pygame.time.set_timer(DOUBLEBULLET,0)
            elif event.type==MOUSEBUTTONDOWN:
                #print(event.pos)
                if event.button==1 and paused_rect.collidepoint(event.pos):
                    paused= not  paused
                    pause_image = pasedAction(SUPPLY_TIME, game_pause_pressed, game_resume_pressed, pause_image, paused)
                if  event.button==1 and (game_over_rect.collidepoint(event.pos) or \
                                         game_over_over_rect.collidepoint(event.pos))and  paused:
                    sys.exit()

                if  event.button==1 and game_continue_rect.collidepoint(event.pos)and  paused:
                    paused=False
                    pause_image = pasedAction(SUPPLY_TIME, game_pause_pressed, game_resume_pressed, pause_image, paused)

                if  event.button==1 and(game_again_rect.collidepoint(event.pos)or\
                                                game_again_over_rect.collidepoint(event.pos))and  paused:
                    for each in enemies:
                        each.reset()
                    for each in bullets:
                        each.active=False
                    myplane.reset()
                    paused=False
                    score=0
                    life=3
                    Game_Over=False
                    pause_image = pasedAction(SUPPLY_TIME, game_pause_pressed, game_resume_pressed, pause_image, paused)
            elif event.type==MOUSEMOTION:
                if paused_rect.collidepoint(event.pos):
                    if paused:
                        pause_image=game_resume_pressed
                    else:
                        pause_image=game_pause_pressed
                else:
                    if paused:
                        pause_image=game_resume_nor
                    else:
                        pause_image=game_pause_nor
            elif event.type==KEYDOWN:
                if not paused and event.key==K_SPACE:
                    if bomb_num:
                        bomb_num-=1
                        bomb_sound.play()
                        for each in enemies:
                            if not isinstance(each,Enemy.EnemyNum3):
                                each.active=False
                            else:
                                each.energy-=(Enemy.EnemyNum3.energy//3)

        #背景
        screen.blit(background,(0,0))

        if not paused :
            if myplane.active==True:
                keypressed=pygame.key.get_pressed()
                if keypressed[K_w] or keypressed[K_UP]:
                    myplane.moveUp()
                if keypressed[K_s] or keypressed[K_DOWN]:
                    myplane.moveDown()
                if keypressed[K_a] or keypressed[K_LEFT]:
                    myplane.moveLeft()
                if keypressed[K_d] or keypressed[K_RIGHT]:
                    myplane.moveRight()
                if keypressed[K_SPACE] or keypressed[K_j]:
                    pass


            #碰撞检测
            if myplane.active:
                Destroylist=pygame.sprite.spritecollide(myplane,enemies,False,pygame.sprite.collide_mask)
                if Destroylist :
                    for each in Destroylist:
                        if each.active:
                            myplane.active=False
                        each.active=False

            #玩家飞机
            if myplane.active:
                if switch_image:
                    screen.blit(myplane.image,myplane.rect)
                else:
                    screen.blit(myplane.image2,myplane.rect)
            else:
                if DestroyMe_index==0:
                    me_down_sound.play()
                if not(delay % 25):
                        screen.blit(myplane.destroy_image[DestroyMe_index],myplane.rect)
                        DestroyMe_index=(DestroyMe_index+1)%4
                        if DestroyMe_index==0:
                            if life>=1:
                                life-=1;
                                myplane.reset()
                            else:
                                Game_Over=True
                                paused=True

            #补给
            if supply_bullet.active:
                if SupplyDraw(supply_bullet,screen,myplane):
                    get_bullet_sound.play();
                    #发射超级子弹
                    pygame.time.set_timer(DOUBLEBULLET,18*1000)
                    ISDouble_Bullet=True
                    #
                    supply_bullet.active=False
            if supply_bomb.active:
                if SupplyDraw(supply_bomb,screen,myplane):
                    get_bomb_sound.play()
                    supply_bomb.active=False
                    if bomb_num<3:
                        bomb_num+=1;


            #调整发射子弹位置
            if not(delay%10 ) and myplane.active:
                if ISDouble_Bullet:
                    bullets=super_bullet
                    bullets[super_bullet_index].reset((myplane.rect.centerx-33,myplane.rect.centery))
                    bullets[super_bullet_index+1].reset((myplane.rect.centerx+33,myplane.rect.centery))
                    super_bullet_index=(super_bullet_index+2)%SUPPEBULLETRNUM
                else:
                    bullets=norm_bullet
                    bullets[bullet_index].reset(myplane.rect.midtop)
                    bullet_index=(bullet_index+1)%BULLETNUM
            #子弹检测是否击中
            for each in bullets:
                if each.active:
                    each.move()
                    bullet_sound.play()
                    screen.blit(each.image,each.rect)
                    hitList=pygame.sprite.spritecollide(each,enemies,False,pygame.sprite.collide_mask)
                    if hitList:
                        each.active=False
                        for hit in hitList:
                            if hit in MiddleEnemies or hit in BigEnemies:
                                hit.energy-=1

                                hit.IsHit=True
                                if hit.energy<0:
                                    hit.active=False
                            else:
                                hit.active=False
            #敌人飞机
                #大飞机
            for each in BigEnemies:
                if each.active:
                    if not each.IsHit:
                        if switch_image:
                            screen.blit(each.image,each.rect)
                        else:
                            screen.blit(each.image2,each.rect)
                    else:
                        screen.blit(each.imageHit3,each.rect)
                        each.IsHit=False
                    if each.rect.bottom==-50:
                        enemy3_fly_sound.play(-1)
                    each.move()
                    #血槽
                    pygame.draw.line(screen,BLACK,(each.rect.left,each.rect.top-5),(each.rect.right,each.rect.top-5),2)
                    energy_remain=each.energy/Enemy.EnemyNum3.energy
                    if energy_remain<0.2:
                        pygame.draw.line(screen,RED,(each.rect.left,each.rect.top-5),\
                                         (each.rect.left+each.rect.width*energy_remain,each.rect.top-5),2)
                    else:
                        pygame.draw.line(screen,GREEN,(each.rect.left,each.rect.top-5),\
                                         (each.rect.left+each.rect.width*energy_remain,each.rect.top-5),2)

                   #大型敌人摧毁
                else:

                    if not(delay % 3):
                        if DestroyBig_index==0:
                            score+=3000
                            enemy3_down_sound.play()
                        screen.blit(each.destroy_image[DestroyBig_index],each.rect)
                        DestroyBig_index=(DestroyBig_index+1)%6
                        if DestroyBig_index==0:
                            enemy3_fly_sound.stop()
                            each.reset()





                #小飞机
            for each in SmallEnemies:
                if each.active:
                    screen.blit(each.image,each.rect)
                    each.move()
                    #血槽

                else:

                    if not(delay % 10):
                        if DestroySmall_index==0:
                            enemy1_down_sound.play()
                            score+=1000
                        screen.blit(each.destroy_image[DestroySmall_index],each.rect)
                        DestroySmall_index=(DestroySmall_index+1)%4
                        if DestroySmall_index==0:
                            each.reset()

                #中型飞机
            for each in MiddleEnemies:
                if each.active:
                    if not each.IsHit:
                        screen.blit(each.image,each.rect)

                    else:
                        screen.blit(each.imageHit,each.rect)
                        each.IsHit=False

                    each.move()
                    pygame.draw.line(screen,BLACK,(each.rect.left,each.rect.top-5),(each.rect.right,each.rect.top-5),2)

                    energy_remain=each.energy/Enemy.EnemyNum2.energy

                    if energy_remain<=0.2:
                        pygame.draw.line(screen,RED,(each.rect.left,each.rect.top-5),\
                                         (each.rect.left+each.rect.width*energy_remain, each.rect.top-5),2)
                    else:
                        pygame.draw.line(screen,GREEN,(each.rect.left,each.rect.top-5),\
                                         (each.rect.left+each.rect.width*energy_remain,each.rect.top-5),2)

                else:
                    if DestroyMiddle_index==0:
                        score+=2000
                        enemy2_down_sound.play()
                    if not(delay % 3):
                        screen.blit(each.destroy_image[DestroyMiddle_index],each.rect)
                        DestroyMiddle_index=(DestroyMiddle_index+1)%4
                        if DestroyMiddle_index==0:
                            each.reset()


            #绘制炸弹数量
            screen.blit(bomb_image,bomb_rect)
            text=score_font.render(" X %s"%str(bomb_num),True,WHITE)
            screen.blit(text,(bomb_rect.right,height-bomb_rect.height+10))
            #子弹
            if  delay%5:
                switch_image=not switch_image
            if not delay:
                delay=100
            delay-=1;

        elif Game_Over:
            finishbackground=pygame.image.load("shoot_background/gameover.png").convert_alpha()
            pygame.time.set_timer(SUPPLY_TIME,0)
            pygame.mixer.music.pause()
            pygame.mixer.pause()
            screen.blit(finishbackground,(0,0))
            text=score_font.render("%s"%str(score),True,WHITE)
            screen.blit(text,(game_continue_rect.left+100 ,game_again_rect.top+110))


            screen.blit(game_again_over,game_again_over_rect)
            #game_again_rect.left,game_again_rect.top=(game_again_rect.left ,game_again_rect.top+160)
            #game_over_rect.left,game_over_rect.top=(game_continue_rect.left ,game_again_rect.top+160)
            screen.blit(game_over_over,(game_over_over_rect))
            #第一次读取记录文件
            if not readScore:
                with open("record.ini","r") as f:
                    topScore=f.read()
                    readScore=True
                    if not topScore.isdigit():
                        topScore=0
                        #print(topScore)


            if int(topScore)<=score:
                topScore=score;
                print(topScore)
                with open("record.ini","w") as f:
                    f.write(str(topScore))
                    #print(topScore)

            text=score_font.render("%s"%str(topScore),True,WHITE)
            screen.blit(text,(135,42))
        else:
            #game_again_rect.top,game_again_rect.left=height//2-50,(width-game_again_rect.width)//2
            #game_continue_rect.top,game_continue_rect.left=height//2-110,(width-game_continue_rect.width)//2
            screen.blit(game_continue,game_continue_rect)
            screen.blit(game_again,game_again_rect)
            screen.blit(game_over,game_over_rect)
         #得分显示
        if not Game_Over:
            screen.blit(pause_image,paused_rect)
            text=score_font.render("score :%s"%str(score),True,WHITE)
            screen.blit(text,(10,5))
            life_num=life_font.render("LIFE :%s"%str(life),True,WHITE)
            screen.blit(life_num,((width-150,height-bomb_rect.height+10)))
        pygame.display.flip()
        clock.tick(60)


def pasedAction(SUPPLY_TIME, game_pause_pressed, game_resume_pressed, pause_image, paused):
    if paused:
        pause_image = game_resume_pressed
        pygame.time.set_timer(SUPPLY_TIME, 0)
        pygame.mixer.music.pause()
        pygame.mixer.pause()
    else:
        pygame.time.set_timer(SUPPLY_TIME, 30 * 1000)
        pygame.mixer.music.unpause()
        pygame.mixer.unpause()
        pause_image = game_pause_pressed
    return pause_image


if __name__ == '__main__':
    try:
        main()

    except SystemExit:
        pass
    except:
        pygame.quit()
        input()






