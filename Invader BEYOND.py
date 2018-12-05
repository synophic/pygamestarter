#space invader BOYOND beta 0.3.2 make many monster
from pygame import*
import sys 
from random import randint, randrange

init()

#score & displaysize
score = 0
dis_width = 800
dis_height = 600

#set display!
screen = display.set_mode((dis_width, dis_height))
display.set_caption('Space Invader BEYOND')
clock = time.Clock()

#base color
black = (0, 0, 0)

#player info
ship = image.load('player.png')
bg = image.load('background.png').convert()
comet = image.load('comet.png')
stk = image.load('inv03.png')
rng = image.load('inv01.png')

#check collision#
def collisions(x1, y1, w1, h1, x2, y2, w2, h2):
    if (x2+w2>=x1>=x2 and y2+h2>=y1>=y2) or (x2+w2>=x1+w1>=x2 and y2+h2>=y1>=y2) or (x2+w2>=x1>=x2 and y2+h2>=y1+h1>=y2) or (x2+w2>=x1+w1>=x2 and y2+h2>=y1+h1>=y2) :
        return True
    return False

#main game loop
def game_loop():
    
    enemy_box = []
    num_enemy = 0
    max_enemy = 3
    
    ply_spd = 0 
    ply_x = 350
    ply_y = 488
    ply_width = 93

    rel_y = 0
    bg_y = 600

    while True:
        #check keyboard input
        for evt in event.get():
            if evt.type == QUIT:
                quit()
                sys.exit()
            if evt.type == KEYDOWN:
                if evt.key == K_LEFT:
                    ply_spd = -3
                if evt.key == K_RIGHT:
                    ply_spd = 3
                if evt.key == K_ESCAPE:
                    quit()
                    sys.exit()
            if evt.type == KEYUP:
                if evt.key == K_RIGHT or evt.key == K_LEFT:
                    ply_spd = 0

        ply_x += ply_spd
        screen.fill(black)

        #scrolling background#
        rel_y = (bg_y % bg.get_rect().width)
        screen.blit(bg, (0, (rel_y - bg.get_rect().width)))
        if rel_y < dis_height:
            screen.blit(bg, (0, rel_y))
        bg_y += 1
        #####################

        if num_enemy != max_enemy:
            for i in range(max_enemy):
                enemy_box.append([randint(50, dis_width - (62 + 50)), -600])
            num_enemy = 3

        else:
            for i in range(len(enemy_box)-1, -1, -1):
                if enemy_box[i][1] > dis_height:
                    num_enemy -= 1
                    del enemy_box[i]
                
            for i in enemy_box:
                i[1] += 5
                screen.blit(comet, (i[0], i[1]))

        #blit player to screen#
        screen.blit(ship, (ply_x, ply_y))
        ###############################

        if ply_x > dis_width - (ply_width+40) or ply_x < 50:
            ply_spd = 0
            
        display.update()
        clock.tick(120)

game_loop()
