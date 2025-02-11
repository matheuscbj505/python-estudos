class restaurante ():
    def __init__(self, restaurante_nome, tipo_cozinha):
        self.restaurante_nome = restaurante_nome
        self.tipo_cozinha = tipo_cozinha 
    def restaurante_decricao (self):
        print (f'O restaurante {self.restaurante_nome.title()} trabalha com a culinária {self.tipo_cozinha.title()}')
    def restaurante_aberto (self):
        print (f'O restaurante {self.restaurante_nome.title()} esta aberto')
 
restaurante1 = restaurante ('bar do marcin', 'buteco')
restaurante1.restaurante_decricao ()
restaurante1.restaurante_aberto ()

restaurante2 = restaurante ('la garça', 'comida espanhola')
restaurante2.restaurante_decricao ()

restaurante3 = restaurante ('le mondieu', 'comida francesa')
restaurante3.restaurante_decricao ()
