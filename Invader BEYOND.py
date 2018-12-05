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
ply_width = 93

bg = image.load('background.png').convert()

comet = image.load('comet.png')

stk = image.load('inv03.png')


def striker(shape, stk_x, stk_y):
    screen.blit(shape, (stk_x, stk_y))

#blit player to screen
def play(x, y):
    screen.blit(ship, (x, y))

#main game loop
def game_loop():

    ply_spd = 0 
    ply_x = 350
    ply_y = 488

    rel_y = 0
    bg_y = 600

    thg_srtx = randrange(50, dis_width - 50)
    thg_srty = -300

    stk_wid = 74
    stk_spd = 1
    stk_high = 90
    findenemy = True

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

        if findenemy:
            if thg_srtx < ply_x:
                thg_srtx += stk_spd
                thg_srty += stk_spd
            elif thg_srtx > ply_x:
                thg_srtx -= stk_spd
                thg_srty += stk_spd
            elif thg_srtx == ply_x or thg_srtx + stk_wid == ply_x:
                findenemy = False
        elif not findenemy:
            thg_srty += 3

        if thg_srty > dis_height:
            thg_srty = 0 - stk_high
            thg_srtx = randrange(50, dis_width - 50)
            findenemy = True

        ply_x += ply_spd
        screen.fill(black)


        rel_y = (bg_y % bg.get_rect().width)
        screen.blit(bg, (0, (rel_y - bg.get_rect().width)))
        if rel_y < dis_height:
            screen.blit(bg, (0, rel_y))
        bg_y += 1

        striker(stk, thg_srtx, thg_srty)
        play(ply_x, ply_y)

        if ply_x > dis_width - (ply_width+40) or ply_x < 50:
            ply_spd = 0

            
        display.update()
        clock.tick(120)

game_loop()
