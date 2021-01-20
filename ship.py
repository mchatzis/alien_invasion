import pygame

class Ship:
    
    def blitShip(self):
        self.screen.blit(self.image,self.rect)
        
    
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
    
            
        
        