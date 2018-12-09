#space invader BOYOND beta 0.8.7 
#fix bullet bug and fix collision 
from pygame import*
import sys 
from random import randint, randrange

init()

##display##
dis_width = 800
dis_height = 600
screen = display.set_mode((dis_width, dis_height))
display.set_caption('Space Invader BEYOND')
clock = time.Clock()
font_name = font.match_font('arial')
###########

##base color##
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
##############

##import image##
ship = image.load('player.png')
bg = image.load('background.png').convert()
comet = image.load('comet.png')
striker = image.load('inv03.png')
ranger = image.load('inv01.png')
bullet = image.load('bullet.png')
enbullet = image.load('enbullet.png')

def wait():
    keys = True
    while keys:
        clock.tick(120)
        for evt in event.get():
            if evt.type == QUIT:
                quit()
                sys.exit()
            if evt.type == KEYUP:
                keys = False
                if evt.key == K_ESCAPE:
                    quit()
                    sys.exit()


##make a Text##
def draw_text(text, size, color, x, y):
    fonts = font.Font(font_name, size)
    text_surface = fonts.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

#check collision#
def collisions(x1, y1, w1, h1, x2, y2, w2, h2):
    if (y2<=y1+h1 and y2>=y1) or (y2+h2<=y1+h1 and y2+h2>=y1):
        if (x2<=x1+w1 and x2>=x1) or (x2+w2<=x1+w1 and x2+w2>=x1):
            return True
    return False

#crate start screen#
def start_screen():
    screen.blit(bg, (0, 0))
    draw_text('SPACE INVADER BEYOND', 48, white, dis_width / 2, 100)
    draw_text('press any button', 22, red, dis_width / 2, dis_height * (4 / 5))
    display.flip()
    wait()

#crate gameover screen#
def game_over(score):
    screen.blit(bg, (0, 0))
    draw_text('GAME OVER', 48, white, dis_width / 2, 100)
    draw_text('Your score is: ' + str(score), 30, green, dis_width / 2, dis_height / 2)
    draw_text('press any button to go to main menu', 22, red, dis_width / 2, dis_height * (4/5))
    display.flip()
    wait()

#random type of enemy#
def rand_enemy():
    species = randint(1, 3)
    #[1:type, 2:x axis, 3:y axis]#
    if species == 1:
        return [1, randint(50, dis_width - (50 + 62)), -(randint(200, 600)), True , 62, 62]
    if species == 2:
        return [2, randint(50, dis_width - (50 + 74)), -74, True, 37, 45]
    if species == 3:
        return [3, randrange(100, dis_width - (100 + 39), 50), 20, True, 39, 34]

#main game loop#
def game_loop(score):
    #enemy setting#
    enemy_box = []
    bullet_box = []
    num_enemy = 0
    max_enemy = 3
    #player setting#
    ply_spd = 0 
    ply_x = 350
    ply_y = 488
    ply_width = 62
    #background setting#
    rel_y = 0
    bg_y = 600

    timer = time.get_ticks()

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
                if evt.key == K_SPACE:
                    bullet_box.append([ply_x + 41, ply_y + 16])
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


        #add enemy to list#
        if num_enemy != max_enemy:
            for i in range(num_enemy, max_enemy):
                enemy_box.append(rand_enemy())
            num_enemy = 3
        ###################

        #check if enemy go off the screen#
        else:
            for i in range(len(enemy_box)-1, -1, -1):
                if enemy_box[i][2] > dis_height:
                    num_enemy -= 1
                    del enemy_box[i]
        ##################################
                
        #blit enemy & return score if you died#
            for i in enemy_box:
                if collisions(ply_x, ply_y, ply_width, ply_width, i[1], i[2], i[4], i[5]):
                        return score
                ###comet###
                if i[0] == 1:
                    i[2] += 5
                    screen.blit(comet, (i[1], i[2]))
                ###########

                ##striker##
                if i[0] == 2:
                    if i[3]:
                        i[2] += 1
                        if i[1] > ply_x:
                            i[1] -= 1
                        elif i[1] < ply_x:
                            i[1] += 1
                        elif i[1] >= ply_x and i[1] <= ply_x + 93:
                            i[3] = False
                    elif not i[3]:
                        i[2] += 4
                    screen.blit(striker, (i[1], i[2]))
                ###########

                ##ranger##
                if i[0] == 3:
                    screen.blit(ranger, (i[1], i[2]))
                ##########

        ######################################

        for i in range(len(bullet_box)-1, -1, -1):
            for j in range(len(enemy_box)-1, -1, -1):
                bullet_box[i][1] -= 3
                screen.blit(bullet, (bullet_box[i][0], bullet_box[i][1]))
                if collisions(enemy_box[j][1], enemy_box[j][2], enemy_box[j][4], enemy_box[j][5], bullet_box[i][0], bullet_box[i][1], 10, 16):
                    if enemy_box[j][0] == 1:
                        score += 60
                    elif enemy_box[j][0] == 2:
                        score += 100
                    elif enemy_box[j][0] == 3:
                        score += 30
                    del enemy_box[j]
                    del bullet_box[i]
                    num_enemy -= 1
                    break

        #blit player to screen#
        screen.blit(ship, (ply_x, ply_y))
        if ply_x > dis_width - (ply_width+40) or ply_x < 50:
            ply_spd = 0
        #######################
        
        draw_text("SCORE: " + str(score), 22, white, 60, 20)
        display.update()
        clock.tick(120)

def main_game():
    score = 0
    while True:
        start_screen()
        score = game_loop(0)
        game_over(score)


main_game()
