# load pygame module
import pygame
from pygame.locals import *

# load third part module

# load user module
import snack
import button

# global vars
mouse_click = False
key = None
dt , fps = None, None
width, height = 400, 400
debug = False

# init pygame
pygame.init()       # pygame.Display.init() is called
pygame.mixer.init() # for sound
pygame.font.init()  # for text
screen = pygame.display.set_mode( ( width, height)) # init a window
clock = pygame.time.Clock() # for time
pygame.display.set_caption( "test_game")

# load resources
image_path = "resources/images/"
audio_path = "resources/audio/"
bonus_img = pygame.image.load( image_path + "bonus.png")     # load images
body_img = pygame.image.load( image_path + "body.png")

#pygame.mixer.music.load( "resources/audio/bk.wav") # load music
#pygame.mixer.music.play(-1, 0.0)
#pygame.mixer.music.set_volume(1)

# game vars
game_proc = "menu"
img_pos = [ 10, 10]
box_width = body_img.get_width() - 10
snack = snack.Snack( box_width, height / box_width + 1, width / box_width + 1)
font = pygame.font.Font( None, 30)
start_btn = button.Button( image_path + "start2.jpg", image_path + "start.jpg")
exit_btn = button.Button( image_path + "exit2.jpg", image_path + "exit.jpg")

# game functions


# main game functions
def quit_game():
    pygame.mixer.quit()
    pygame.font.quit()
    pygame.quit()
    exit( 0)
def Render():
    if game_proc == "menu":
        txt = font.render( "Eat Snack", True, ( 10, 10, 233))
        rect = txt.get_rect()
        rect.centery = height / 4
        rect.centerx = width / 2
        screen.blit( txt, rect)
        start_btn.Render( screen, width / 2 - 60, height / 2 - 50)
        exit_btn.Render( screen, width / 2 - 60, height / 2 + 20)
    elif game_proc == "run":
        for pos in snack.RenderBonus():
            screen.blit( bonus_img, pos)
        for pos in snack.RenderSnack():
            screen.blit( body_img, pos)
    elif game_proc == "over":
        txt = font.render( "game over", True, ( 10, 10, 233))
        rect = txt.get_rect()
        rect.centerx = width / 2
        rect.centery = height / 2
        screen.blit( txt, rect)
    elif game_proc == "pause":
        pass
    
def Update():
    global game_proc
    if game_proc == "menu":
        if start_btn.Update( pygame.mouse.get_pos()[ 0], pygame.mouse.get_pos()[ 1]):
            if mouse_click:
                game_proc = "run"
        elif exit_btn.Update( pygame.mouse.get_pos()[ 0], pygame.mouse.get_pos()[ 1]):
            if mouse_click:
                quit_game()
    elif game_proc == "run":
        if key != None:
            if key == K_w:
                snack.ChangeDirection( "up")
            elif key == K_s:
                snack.ChangeDirection( "down")
            elif key == K_a:
                snack.ChangeDirection( "left")
            elif key == K_d:
                snack.ChangeDirection( "right")
        if snack.Update( dt) == False:
            game_proc = "over"
    elif game_proc == "over":
        pass
        
def SysRender():
    # clear screen to black
    screen.fill( 0)
    # user render
    Render()
    # sys render
    if debug:
        txt = font.render( "fps:" + str( fps), True, ( 255, 0, 0))
        rect = txt.get_rect()
        screen.blit( txt, rect)
        txt = font.render( "direction:" + str( snack.Dir), True, ( 255, 0, 0))
        rect = txt.get_rect()
        rect.top = 35
        screen.blit( txt, rect)
        txt = font.render( "mouse:" + str( pygame.mouse.get_pos()), True, ( 255, 0, 0))
        rect = txt.get_rect()
        rect.top = 70
        screen.blit( txt, rect)
    # update screen
    pygame.display.flip()   # flip back-screen to current-screen
    
def SysUpdate():
    global dt, fps
    # handle sys keys
    if key == K_F11:
        pygame.display.toggle_fullscreen()
    # sys update
    clock.tick()    # update clock
    # sys vars
    dt = clock.get_time()   # get delta time of last frame
    fps = clock.get_fps()   # get FPS
    # game update
    Update()        # update game before render


# game loop
while True:
    # get input
    mouse_click = False
    key = None
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            key = e.key
        elif e.type == pygame.QUIT:
            quit_game()
        elif e.type == pygame.MOUSEBUTTONDOWN:
            mouse_click = True
    # update game
    SysUpdate()
    # render game
    SysRender()
