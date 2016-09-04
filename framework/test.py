import pygame
import g
from pygame.locals import *
import numpy as np

ctrl_keys = {pygame.K_a:(-1,0),\
    pygame.K_d:(1,0),\
    pygame.K_w:(0,-1),\
    pygame.K_s:(0,1)} 

class Object:
    def __init__(self, img_path = None):
        if img_path:
            self.img = pygame.image.load(img_path)
        else:
            self.img = None
        self.pos = np.array([100., 100.])
        self.speed = 300
    def draw(self):
        pos = [int(x) for x in self.pos]
        if self.img:
            g.screen.blit(self.img, pos)
        else:
            pygame.draw.circle(g.screen, [0,0,255], pos, 10)
    def move(self, direction):
        self.pos += direction * self.speed * g.dt

player = Object()#"C:/Users/liyong11/Pictures/avatar.png")

def draw():
    player.draw()

def update():
    move_direction = np.array([0.,0.])
    for key in ctrl_keys.iterkeys():
        if g.key_down[key]:
            move_direction += ctrl_keys[key]

    player.move(move_direction)



g.main(update, draw)
