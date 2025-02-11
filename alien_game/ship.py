import pygame 

class Ship (): 
    def __init__(self, ai_settings, screen):
        #inicializa a espaçonave e define sua posição inicial
        self.screen = screen
        self.ai_settings = ai_settings
        #carrega a imagem da espaçonave e obtem seu rect
        self.image = pygame.image.load ('images/ship.bmp')
        #trabalha com a "retangularização" da nave e da tela 
        self.rect = self.image.get_rect ()
        self.screen_rect = screen.get_rect ()
        #sincroniza a posição da imagem com a posição da tela 
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom 

        self.moving_right = False 
        self.moving_left = False 

    def update (self): 
        #atualiza a posição de acordo com a flag de movimento  
        if self.moving_right:
            self.rect.centerx += self.ai_settings.ship_speed_factor 
        if self.moving_left: 
            self.rect.centerx -= self.ai_settings.ship_speed_factor 

    def blitme (self):
        #desenha a nave em sua posição atual
        self.screen.blit (self.image, self.rect)



