import pygame
from settings import Settings
from ship import Ship
import game_functions as functs

def run_game():
    
    #initialize game window
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #create Ship and aliens
    ship = Ship(screen)
    
    #main game loop
    while True:
        
        functs.handle_events()
        
        #update screen
        functs.update_screen(settings,screen,ship)
        
        #render screen
        pygame.display.flip()
    

if __name__ == "__main__":
    run_game()