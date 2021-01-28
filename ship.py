import pygame

class Ship:

    def __init__(self,screen):
        '''Import ship image and set the ship's initial position'''
        
        self.screen = screen
        
        #Load ship image and get its rectangle
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load('res/images/spaceship.bmp')
        self.rect = self.image.get_rect()
        
        #Position the ship at the bottom middle of the screen 
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #Movement state
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
            
    def blitShip(self):
        self.screen.blit(self.image,self.rect)
        
    def update(self):
        '''Update position of the ship (remember top-left is the origin (0,0) )'''
        
        if self.moving_right == True:
            self.rect.centerx += 1
        if self.moving_left == True:
            self.rect.centerx -=1
        if self.moving_up == True:
            self.rect.bottom -= 1
        if self.moving_down == True:
            self.rect.bottom += 1
        
    
            
        
        