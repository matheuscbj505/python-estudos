import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf 

def run_game (): 

    #incializa o jogo e cria um objeto para tela 
    pygame.init () 
    ai_settings  = Settings ()
    screen = pygame.display.set_mode ((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship (ai_settings, screen)
    pygame.display.set_caption ("Alien Invasion")

    #principal laço do jogo 
    while True: 
        gf.check_events (ship)
        ship.update ()
        gf.update_screen (ai_settings, screen, ship)
    
run_game ()

