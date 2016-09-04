from collections import defaultdict
import pygame
from pygame.locals import *
 
key_down = defaultdict(bool)
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
dt = 0

def update(up_fn):
    global dt
    dt = clock.tick(60) / 1000. # 30FPS
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type == pygame.KEYDOWN:
            key_down[event.key] = True
        elif event.type == pygame.KEYUP:
            key_down[event.key] = False
        elif event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0)
    up_fn()

def draw(draw_fn):
    draw_fn()

def main(update_fn, draw_fn):
    while True:
        screen.fill(0)
        draw(draw_fn)
        pygame.display.flip()
        update(update_fn)
