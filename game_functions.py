import pygame
import sys

def handle_events():
    '''Function that checks for events'''
    
    #event listener loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
def update_screen(settings,screen,ship):
    '''Update images on screen using settings and the gaming componets(aliens,ship)'''
    
    #background colour
    screen.fill(settings.bg_color)
        
    #draw ship on screen
    ship.blitShip()
    