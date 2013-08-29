import pygame

class Button:
        def __init__( self, over_pic, normal_pic):
                self.over_img = pygame.image.load( over_pic)
                self.normal_img = pygame.image.load( normal_pic)
                self.render_img = self.normal_img
                self.x = self.y = 0
                self.mouse_on_btn = False
        def Update( self, mouse_x, mouse_y):
                if mouse_x > self.x and mouse_x < self.x + self.render_img.get_width() \
                   and mouse_y > self.y and mouse_y < self.y + self.render_img.get_height():
                        mouse_on_btn = True
                        self.render_img = self.over_img
                else:
                        mouse_on_btn = False
                        self.render_img = self.normal_img
                return mouse_on_btn
        def Render( self, screen, x = -1, y = -1):
                if x != -1:
                        self.x = x
                if y != -1:
                        self.y = y
                screen.blit( self.render_img, ( self.x, self.y))
        
