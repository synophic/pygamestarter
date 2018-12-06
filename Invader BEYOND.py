#space invader BOYOND beta 0.5.7 random enemy
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
striker = image.load('inv03.png')
ranger = image.load('inv01.png')

#check collision#
def collisions(x1, y1, w1, h1, x2, y2, w2, h2):
    if (x2+w2>=x1>=x2 and y2+h2>=y1>=y2) or (x2+w2>=x1+w1>=x2 and y2+h2>=y1>=y2) or (x2+w2>=x1>=x2 and y2+h2>=y1+h1>=y2) or (x2+w2>=x1+w1>=x2 and y2+h2>=y1+h1>=y2) :
        return True
    return False

#random type of enemy#
def rand_enemy():
    species = randint(1, 3)
    #[1:type, 2:x axis, 3:y axis]#
    if species == 1:
        return [1, randint(50, dis_width - (50 + 62)), -(randint(200, 600)), True]
    if species == 2:
        return [2, randint(50, dis_width - (50 + 74)), -74, True]
    if species == 3:
        return [3, randrange(51, dis_width - (50+79), 124), 20, True]

#main game loop#
def game_loop():
    #enemy setting#
    enemy_box = []
    num_enemy = 0
    max_enemy = 3
    #player setting#
    ply_spd = 0 
    ply_x = 350
    ply_y = 488
    ply_width = 93
    #background setting#
    rel_y = 0
    bg_y = 600

    findply = True
    speed = 0


    while True:
        #check keyboard input#
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
        ######################


        #scrolling background#
        rel_y = (bg_y % bg.get_rect().width)
        screen.blit(bg, (0, (rel_y - bg.get_rect().width)))
        if rel_y < dis_height:
            screen.blit(bg, (0, rel_y))
        bg_y += 1
        #####################


        if num_enemy != max_enemy:
            for i in range(num_enemy, max_enemy):
                enemy_box.append(rand_enemy())
            num_enemy = 3

        else:
            for i in range(len(enemy_box)-1, -1, -1):
                if enemy_box[i][2] > dis_height:
                    num_enemy -= 1
                    del enemy_box[i]
                
            for i in enemy_box:
                if i[0] == 1:
                    i[2] += 5
                    screen.blit(comet, (i[1], i[2]))

                if i[0] == 2:
                    if i[3]:
                        i[2] += 1
                        if i[1] > ply_x:
                            i[1] -= 1
                        elif i[1] < ply_x:
                            i[1] += 1
                        elif i[1] == ply_x or i[1] + 74 == ply_x:
                            i[3] = False
                    elif not i[3]:
                        i[2] += 4

                    screen.blit(striker, (i[1], i[2]))
                if i[0] == 3:
                    if i[1] < 50:
                        speed = 3
                    elif i[1] > dis_width - (78 + 50):
                        speed = -3
                    i[1] += speed
                    screen.blit(ranger, (i[1], i[2]))




        #blit player to screen#
        screen.blit(ship, (ply_x, ply_y))

        if ply_x > dis_width - (ply_width+40) or ply_x < 50:
            ply_spd = 0
        #######################
            
        display.update()
        clock.tick(120)

game_loop()
