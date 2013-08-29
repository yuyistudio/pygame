# from snack.h

import pygame
import random


class Snack:
    def __init__( self, w, rs, cs):
        self.changeDir = False
        self.rows = rs
        self.cols = cs
        self.width = w
        self.InitSnack( self.width * 2, self.width * 2)
        self.eat_snd = pygame.mixer.Sound( "resources/audio/eat.wav")      # load sounds
        self.eat_snd.set_volume( 0.1)
        self.move_snd = pygame.mixer.Sound( "resources/audio/move.wav")
        self.move_snd.set_volume( 0.1)
    Direction = { "up":0, "right":1, "down":2, "left":3}
    def ChangeDirection( self, dir):
        if self.changeDir == False:
            if abs( self.Direction[ dir] - self.Direction[ self.Dir]) != 2:
                self.Dir = dir
            self.changeDir = True
    def InitSnack( self, x, y):
        self.snack_list = []
        self.bonus_list = []
        self.snack_list.insert( len( self.snack_list), ( x, y))
        self.Dir = "down"
        self.GenBonus()
    # if return false, game over
    def Update( self, dt):
        # control moving speed
        self.dx += 1.0 * dt * self.speed / 1000
        if self.dx < 1:
            return True
        self.dx = 0
        self.move_snd.play()
        self.changeDir = False
        # recourd the pos of tail and head
        tail = self.snack_list[ 0]
        head = self.snack_list[ len( self.snack_list) - 1]
        # check if eating bonus
        for bonus in self.bonus_list:
            if head == bonus:   # if eating bonus
                self.eat_snd.play()
                self.bonus_list.pop()
                self.GenBonus()
                break
        else:
            # remove tail if not eating bonus
            del self.snack_list[0]
        # cal new head pos
        head = list( head)
        if self.Dir == "up":
            head[ 1] -= self.width
        elif self.Dir == "down":
            head[ 1] += self.width
        elif self.Dir == "right":
            head[ 0] += self.width
        elif self.Dir == "left":
            head[ 0] -= self.width
        # check if crash its body
        for body_node in self.snack_list:
            if head == list( body_node):    # crashed!
                return False
        # add new head
        head[ 0] = divmod( head[ 0], self.cols * self.width)[ 1]
        head[ 1] = divmod( head[ 1], self.rows * self.width)[ 1]
        self.snack_list.insert( len( self.snack_list), tuple( head))
        return True
    def RenderSnack( self):
        for pos in self.snack_list:
            yield pos
    def RenderBonus( self):
        for pos in self.bonus_list:
            yield pos
    def GenBonus( self):
        while True:
            bonus_pos = ( random.randint( 0, 10) * self.width, random.randint( 0, 10) * self.width)
            for node_pos in self.snack_list:
                if node_pos == bonus_pos:
                    break   # break 'for', but continue 'while'
            else:
                break   # break 'while', coz we've found a valide position
        self.bonus_list.insert( 0, bonus_pos)
    snack_list = []
    speed = 5
    dx = 0.1
    rows = cols = 0
    width = 40
    bonus_list = []
    Dir = "down"

