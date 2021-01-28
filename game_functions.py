import pygame
import sys
    
def handle_events(ship):
    '''Function that checks for events'''
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.KEYDOWN:            
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
            if event.key == pygame.K_UP:
                ship.moving_up = True
            if event.key == pygame.K_DOWN:
                ship.moving_down = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
            if event.key == pygame.K_UP:
                ship.moving_up = False
            if event.key == pygame.K_DOWN:
                ship.moving_down = False
    
def update_screen(settings,screen,ship):
    '''Update images on screen using settings and the gaming componets(aliens,ship)'''
    
    #background colour
    screen.fill(settings.bg_color)
        
    #draw ship on screen
    ship.blitShip()
    