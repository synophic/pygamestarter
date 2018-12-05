#space invader BOYOND beta 0.2.2 scrolling background
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

def target(x1, w1, x2, w2):
    if(x2+w2>=x1>=x2) or (x2+w2>=x1+w1>=x2) or (x2+w2>=x1>=x2) or (x2+w2>=x1+w1>=x2):
        return True
    return False

def enemy(enemy_box, ply_x, ply_width, num_enemy, max_enemy, findply):
    rand_enemy(enemy_box, num_enemy, max_enemy)
    for i in enemy_box:
        if i[1] == 1:
            striker(stk, i[2], i[3], ply_x, ply_width, findply)
        if i[1] == 2:
            commet(comet, i[2], i[3])
        if i[1] == 3:
            ranger(rng, i[2], i[3])
    for i in range(len(enemy_box)-1, -1, -1):
        if enemy_box[i][3] > dis_height:
            del enemy_box[i]

def rand_enemy(enemy_box, num_enemy, max_enemy):
    stk_y = -74
    stk_x = randint(50, dis_width-(74+50))

    com_y = -200
    com_x = randint(50, dis_width-(62+50))

    rng_y = 0
    rng_x = randint(50, dis_width-(78+50))

    if num_enemy < max_enemy:
        for i in range(num_enemy, max_enemy):
            enemy_type = randrange(1, 3)
            if enemy_type == 1:
                enemy_box.append([stk, 1, stk_x, stk_y])
            elif enemy_type == 2:
                enemy_box.append([comet, 2, com_x, com_y])
            elif enemy_type == 3:
                enemy_box.append([rng, 3, com_x, com_y])
            num_enemy += 1
        return num_enemy

def commet(img, x, y):
    wid = 62
    spd = 3
    high = 62
    screen.blit(img, (x, y - spd))

def ranger(img, x, y):
    wid = 78
    high = 68
    spd = 1
    if x < 50:
        spd = 1
    elif x > dis_width - (wid + 50):
        spd = -1
    screen.blit(img, (x + spd, y))


def striker(img, x, y, p_x, p_w, findply):
    wid = 74
    spd = 5
    high = 90
    if findply:
        if x > p_x:
            x -= 2
            y += 1
        if x < p_x:
            x += 2
        elif target(x, wid, p_x, p_w):
            findply = False

    else:
        st_y += spd

    screen.blit(img, (x, y))

#main game loop
def game_loop():
    
    enemy_box = []
    num_enemy = 0
    max_enemy = 3
    
    findply = True
    ply_spd = 0 
    ply_x = 350
    ply_y = 488
    ply_width = 93
    rel_y = 0
    bg_y = 600

    thg_srtx = randrange(50, dis_width - 50)
    thg_srty = 0

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
        enemy(enemy_box, ply_x, ply_width, num_enemy, max_enemy, findply)

        rel_y = (bg_y % bg.get_rect().width)
        screen.blit(bg, (0, (rel_y - bg.get_rect().width)))
        if rel_y < dis_height:
            screen.blit(bg, (0, rel_y))
        bg_y += 1

        screen.blit(ship, (ply_x, ply_y))

        if ply_x > dis_width - (ply_width+40) or ply_x < 50:
            ply_spd = 0

            
        display.update()
        clock.tick(120)

game_loop()
