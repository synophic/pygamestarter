#Space invader BEYOND beta ver 0.0.1
#space invader BEYOND beta var 0.1.1 creat game screen & exit button
#import everything that need for project
from pygame import *
import sys
from random import randint, choice
from os.path import abspath, dirname

#import file  filename.xxx from /folder/
base_path = abspath(dirname(__file__))
img_path = base_path + '/images/'

#set color (R, G, B)
black = (0, 0, 0)

#set size of screen
screen_width = 800
screen_height = 600

game_end = False

#setup game screen
SCREEN = display.set_mode((screen_width, screen_height))

#lets import image
#use list to make it easier to call
img_name = ['inv01-1', 'player']
IMAGES = {name:image.load(img_path + '{}.png'.format(name)) 
            for name in img_name}

class SpaceInvaders(object):
    def __init__(self):
        self.screen = SCREEN
        
    def should_exit(evt):
        return evt.type == QUIT or (evt.type == KEYUP and evt.ket == K_ESCAPE)

    def input_check(self):
        self.keys = key.get_pressed()
        for e in event.get():
            if e.type == QUIT:
                sys.exit()
                

    #main game loop
    def game_loop(self):
        while not game_end:
            self.screen.fill(black)    
            self.input_check()

if __name__ == '__main__':
    game = SpaceInvaders()
    game.game_loop()
    
